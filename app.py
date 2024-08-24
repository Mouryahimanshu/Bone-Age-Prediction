from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf
import joblib
import gradio as gr
import pandas as pd

# Load the pre-trained model
model = joblib.load("bone_age_model.pkl")

mean_bone_age = 127.3207517246848
std_bone_age = 41.182021399396326


def load_and_prep_image(filename, img_shape=224, rescale=True):
    img = image.load_img(filename, target_size=(img_shape, img_shape))
    img = image.img_to_array(img)
    
    if img.shape[-1] == 4:  # Remove alpha channel if present
        img = img[..., :3]
    
    if rescale:
        img = img / 255. 
    
    return img

def predict_bone_age(model, img, mean_bone_age, std_bone_age):
    img = load_and_prep_image(img)
    
    # Make a prediction
    pred = model.predict(tf.expand_dims(img, axis=0))
    pred = mean_bone_age + std_bone_age * pred
    pred_years = np.round(pred[0][0] / 12.0)
    
    # Return the prediction and the image
    return f"Predicted Bone Age: {pred_years} years", img


# Gradio Interface
iface = gr.Interface(
    fn=lambda filepath: predict_bone_age(model, filepath, mean_bone_age, std_bone_age),
    inputs=gr.Image(type="filepath", label="Upload an Image"),
    outputs=[
        gr.Textbox(label="Prediction"),
        gr.Image(type="numpy", label="Processed Image")
    ],
    title="Bone Age Prediction",
    description="Upload an X-ray image to predict the bone age."
)

# Launch the app
iface.launch()
   
