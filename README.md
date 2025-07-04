# Image Classification Model

This project provides a Keras deep learning model for image classification, along with utilities to perform predictions on new images and classify it as day or night.

This repository includes:
- A pre-trained Keras model (`keras_Model.h5`)
- A Python script (`predict_image.py`) to load the model and run predictions
- A text file (`labels.txt`) that containing the classes

# Requirements

Make sure you have Python installed (Python 3.8–3.10 recommended).  
Install the following packages:

- TensorFlow 2.19.0
- Keras 3.10.0
- NumPy
- Pillow (for image processing)


You can install them via pip:

(bash)
pip install tensorflow==2.19.0 keras==3.10.0 numpy pillow


Example Output:

Class: day
Confidence Score: 0.91559476
