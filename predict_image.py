from keras.layers import DepthwiseConv2D
from tensorflow.keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Patch DepthwiseConv2D.__init__ to ignore 'groups' argument during deserialization
original_init = DepthwiseConv2D.__init__

def patched_init(self, *args, **kwargs):
    kwargs.pop('groups', None)  # Remove 'groups' if it exists
    original_init(self, *args, **kwargs)

DepthwiseConv2D.__init__ = patched_init


# Load the model
model = load_model(r"c:\Users\abdul\Downloads\task1\converted_keras\keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open(r"C:\Users\abdul\Downloads\task1\converted_keras\pic\night\test.jpg").convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)
load_model