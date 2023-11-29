import os
import random
import string

def generate_random_filename():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

def save_image(file):
    random_filename = generate_random_filename()
    _, file_extension = os.path.splitext(file.filename)
    image_path = f"static/images/{random_filename}{file_extension}"
    file.save(image_path)
    return image_path

def delete_image(image_path):
    if os.path.exists(image_path):
        os.remove(image_path)
        return f"Image at {image_path} deleted successfully."
    else:
        return f"Image at {image_path} does not exist."