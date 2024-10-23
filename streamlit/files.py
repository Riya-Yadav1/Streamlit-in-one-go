import streamlit as st
import pandas as pd
st.subheader("Loading the CSV file")

df=st.file_uploader("Upload the CSV file: ",type=['pdf','jpg'])

df= pd.read_csv("C:/Users/DELL/OneDrive/Desktop/streamlit/Products.csv")
if df is not None:
    st.table(df.head())


st.subheader("Dealimg with images")
st.image("C:/Users/DELL/Downloads/pexels-pixabay-355465.jpg")

st.subheader("Dealimg with images while uploading")
img_file= st.file_uploader("Upload the image file: ", type=['png','jpg'])
if img_file is not None:
    st.image(img_file)

st.subheader("Working with videos")
video_file= st.file_uploader("Upload the image file: ", type=['mp4','mkv'])
if video_file is not None:
    st.video(video_file,start_time=1)


st.subheader("Working with Audios file")
audio_file= st.file_uploader("Upload the image file: ", type=['mp3','wav'])
if audio_file is not None:
    st.video(audio_file.read())
