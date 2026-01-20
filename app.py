import streamlit as st
import pandas as pd
import time

# Import functions from predict.py
from predict import predict_url, extract_features

st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🛡️",
    layout="centered"
)

# Header and Logo
st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=80)
st.title("🛡️ Phishing URL Detection System")
st.markdown("""
This system uses Machine Learning (**Random Forest**) to analyze URLs and detect potential phishing threats.
""")

st.markdown("---")

# Sidebar - Project Info
with st.sidebar:
    st.header("ℹ️ About the Project")
    st.info("Developed for Senior Capstone Project.")
    st.write("**Model:** Random Forest Classifier")
    st.write("**Training Data:** 11,000+ Websites")
    st.markdown("---")
    st.warning("⚠️ For educational purposes only.")

# Input Area
url_input = st.text_input("Enter URL to Analyze:", placeholder="https://example-site.com")

# Analyze Button
if st.button("🚀 Analyze URL", type="primary"):
    if not url_input:
        st.warning("Please enter a URL to proceed!")
    else:
        # Auto-add http protocol if missing
        if not url_input.startswith(("http://", "https://")):
            target_url = "http://" + url_input
        else:
            target_url = url_input

        # Loading Spinner
        with st.spinner("🤖 AI is analyzing the URL..."):
            time.sleep(1)  # Short delay for visual effect

            try:
                # 1. Get Prediction
                result_text = predict_url(target_url)

                # 2. Display Result
                if "SAFE" in result_text:
                    st.success(f"## {result_text}")
                    st.balloons()
                elif "PHISHING" in result_text:
                    st.error(f"## {result_text}")
                else:
                    st.warning(f"## {result_text}")

                # 3. Feature Breakdown Table
                st.markdown("---")
                st.subheader("🔍 Feature Analysis Breakdown")

                features = extract_features(target_url)

                # Column names in English
                columns = [
                    'Has IP Address?', 'URL Length', 'Shortening Service?',
                    '@ Symbol?', 'Double Slash Redirect?', 'Hyphen (-) in Domain?',
                    'Subdomain Count', 'HTTPS in Domain?'
                ]

                # Create DataFrame for better visualization
                df_features = pd.DataFrame(features, columns=columns)

                # Display DataFrame
                st.dataframe(df_features)
                st.caption("*Values: 1 (Safe), 0 (Suspicious), -1 (Phishing)*")

            except Exception as e:
                st.error("An error occurred during analysis!")
                st.code(e)
                st.info("Tip: Ensure 'predict.py' and 'phishing_model.pkl' are in the same directory.")