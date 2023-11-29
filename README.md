# EyeTry-FaceShapeDetection

EyeTry-FaceShapeDetection is part of the EyeTry which detect user face shape based on an image. User upload an image and server returns the face shape of a person.

## Requirements

Install the required packages using:

```
pip install torch torchvision pillow matplotlib numpy scikit-learn
```

or

```
pip install -r requirements.txt
```

## Running the App

0. Activating Python Virtual Environment

```
    Scripts\activate
```

1. Setting the Environment Variables

```bash
  set FLASK_APP=main.py
  set FLASK_ENV=development
```

2. Running the App

```bash
    flask run -p port
```

## Endpoints:

```
method: POST
route: /upload
parameters: file

returns:
{
    "prediction": <face shape>,
    "status": "success"
}

method: GET
route: /test

returns:
{
    "status": "success"
}
```
