import streamlit as st
import joblib
from scipy.sparse import csr_matrix
from PIL import Image

st.set_page_config(page_title="Email Classifier", page_icon="📧")

MODEL_PATH = "model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"
IMPORTANT_IMAGE_PATH = "images/Important.png"
SPAM_IMAGE_PATH = "images/Spam.png"

# Load the model and vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# Email classification function
def classify_email(email_text):
    if not email_text.strip():
        raise ValueError("Input text cannot be empty.")
    
    # Transform the input text using the trained vectorizer
    message = vectorizer.transform([email_text])
    if not isinstance(message, csr_matrix):
        message = csr_matrix(message)
    
    # Predict using the model
    prediction = model.predict(message)[0]
    
    return 1 if prediction == 'ham' else 0

# App Header
st.title("📧 Email Classification App")
st.markdown(
    """A simple app to classify emails as **Spam** or **Not Spam**.
    Simply enter the email text below and press **Classify** to get the result."""
)

# Sidebar for additional information
st.sidebar.header("📝Instructions")
st.sidebar.info(
    """1. Enter the email content in the provided text box.
    
    2. Click the **Classify** button.
    
    3. The app will display the classification along with a relevant image.
    
    4. Ensure the model and vectorizer files are correctly placed."""
)

# Main input section
st.subheader("Enter Email Text")
email_text = st.text_area(
    "Type or paste your email content below:",
    placeholder="e.g., Congratulations! You have won a free iPhone."
)

# Classify button with feedback
if st.button("Classify"):
    if model is None or vectorizer is None:
        st.error("Model or vectorizer is not loaded. Please resolve the issue and try again.")
    elif email_text.strip():
            result = classify_email(email_text)
            if result == 1:
                st.image(r"imag\Important.png")
            else:
                st.image(r"imag\Spam.png")

    else:
        st.error("Please enter some text to classify.")

