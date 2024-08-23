import streamlit as st
from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf

mean_bone_age = 127.3207517246848
std_bone_age = 41.182021399396326


model = tf.keras.models.load_model(r"C:\Users\himan\Downloads\best_model.keras") 

def load_and_prep_image(filename, img_shape=224, rescale=True):
    img = image.load_img(filename, target_size=(img_shape, img_shape))
    img = image.img_to_array(img)
    
    if img.shape[-1] == 4:  # Remove alpha channel if present
        img = img[..., :3]
    
    if rescale:
        img = img / 255. 
    
    return img

def pred_and_display(model, filename, mean_bone_age, std_bone_age):
    img = load_and_prep_image(filename)
    
    # Make a prediction
    pred = model.predict(tf.expand_dims(img, axis=0))
    pred = mean_bone_age + std_bone_age * pred
    pred_years = np.round(pred[0][0] / 12.0)
    
    # Display the image
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    # Display the prediction in bold
    st.markdown(f"**Predicted Bone Age: {pred_years} years**")

# Streamlit App Code
st.title("Bone Age Prediction")

# Upload an image
uploaded_file = st.file_uploader(f"**Choose an image**", type="png")

if uploaded_file is not None:
    st.write(f"**Calculating bone age**")
    pred_and_display(model, uploaded_file, mean_bone_age, std_bone_age)
