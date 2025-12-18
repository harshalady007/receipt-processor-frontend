import streamlit as st
import boto3
import os

# --- CONFIGURATION ---
BUCKET_NAME = "smart-doc-processor-yourname-2025" # <--- YOUR BUCKET NAME
REGION = "ap-south-1" # <--- YOUR REGION
# ---------------------

st.title("🧾 AI Receipt Scanner")
st.write("Upload a receipt image. The AI will extract data and email you the Excel file.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Show the image
    st.image(uploaded_file, caption='Uploaded Receipt', use_column_width=True)
    
    if st.button('Process Receipt'):
        with st.spinner('Uploading to AWS...'):
            # 1. Connect to S3
            # (Streamlit uses your local AWS credentials automatically)
            s3 = boto3.client('s3', region_name=REGION)
            
            # 2. Upload file
            file_key = f"input/{uploaded_file.name}"
            try:
                s3.upload_fileobj(uploaded_file, BUCKET_NAME, file_key)
                st.success(f"✅ Upload successful! Check your email in 1 minute.")
            except Exception as e:
                st.error(f"Error: {e}")