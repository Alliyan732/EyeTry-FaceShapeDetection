from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from utility.image_utility import save_image, delete_image
from utility.predict import predict
from utility.face_prediction import isFace, isFaceAlt

import torch
import torch.nn as nn
from torchvision.models import efficientnet_b4

# device = "cuda" if torch.cuda.is_available() else "cpu"
device = torch.device("cpu")

app = Flask(__name__)
CORS(app)

model = efficientnet_b4()
num_classes = 5
model.classifier = nn.Sequential(
    nn.Dropout(p=0.3, inplace=True),
    nn.Linear(model.classifier[1].in_features, num_classes)
)
model.load_state_dict(torch.load('model/face_detect_model.pth', map_location=device))
model.to(device)
model.eval()
    
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'status': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'No selected files'}), 400

    if file:
        image_path = save_image(file)

        isFacePresent = isFaceAlt(image_path)

        if (isinstance(isFacePresent, tuple)):
            return jsonify({'status': 'error', 'message': "No face is detected in the image"}), 400

        result = predict(image_path, model)
        delete_image(image_path)
        return jsonify({'status': 'success', 'prediction': result}), 200   
    
    return jsonify({'status': 'error'}), 400


@app.route('/test')
def test():
    return jsonify({'status': 'success'}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4444)