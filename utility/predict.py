import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def predict_face_shape(image_path, model):
    img = Image.open(image_path)
    img = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(img)
        _, predicted = torch.max(output, 1)
        return predicted.item()


def predict(image_path, model):
    labels_dict = {0: 'Heart', 1: 'Oblong', 2: 'Oval', 3: 'Round', 4: 'Square'}

    predicted_label = predict_face_shape(image_path, model)
    predicted_shape = labels_dict.get(predicted_label, "Unknown")
    # print(f"Predicted face shape: {predicted_shape}")
    return predicted_shape