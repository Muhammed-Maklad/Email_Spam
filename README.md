# 📧 Email Classification App

A user-friendly Streamlit application to classify emails as **Spam** or **Not Spam** using a pre-trained machine learning model.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [File Structure](#file-structure)
7. [Model Details](#model-details)
8. [Screenshots](#screenshots)
9. [License](#license)

---

## Introduction

The **Email Classification App** allows users to classify email content as either "Spam" or "Not Spam" using a machine learning model. Simply paste the email text into the app and receive an instant classification with a relevant visual indicator.

---

## Features

- Intuitive user interface built with Streamlit.
- Pre-trained machine learning model for text classification.
- Easy-to-follow instructions and seamless integration.
- Visual feedback based on the classification result.

---

## Requirements

- Python 3.8+
- Required libraries:
  - `streamlit`
  - `joblib`
  - `scipy`
  - `Pillow`

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Muhammed-Maklad/Email_Spam.git
   cd email-classification-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the following files in the project directory:
   - **`model.pkl`**: Pre-trained machine learning model.
   - **`vectorizer.pkl`**: Text vectorizer.
   - Images for classification results in the `images` folder:
     - `Important.png`
     - `Spam.png`

---

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Follow these steps:
   - Enter the email text in the text area.
   - Click the **Classify** button.
   - View the classification result and corresponding image.

---

## File Structure

```
email-classification-app/
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── model.pkl             # Pre-trained model
├── vectorizer.pkl        # Text vectorizer
├── images/
│   ├── Important.png     # Image for "Not Spam"
│   └── Spam.png          # Image for "Spam"
└── README.md             # Project documentation
```

---

## Model Details

- The machine learning model was trained on a spam dataset using features extracted via a vectorizer.
- The app uses a **Support Vector Machine (SVM)** for classification.

---

## Screenshots

### 1. App Home Page
![App Home Page](images/home.png)

### 2. Classification Result
![Classification Result](images/result.png)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Enjoy classifying your emails with ease!
