#  Smart Message Classifier

A lightweight Machine Learning web application that classifies messages into categories such as **Spam**, **Important**, and **Normal** using **Natural Language Processing (NLP)** and a **Naive Bayes Classification Model**.

Built using:

- Python
- FastAPI
- Scikit-learn
- HTML/CSS/JavaScript

The project demonstrates how Machine Learning models can be integrated with modern web frameworks to create real-time intelligent applications.

---

#  Features

- Real-time message classification
- Detects:
  - Spam Messages
  - Important Messages
  - Normal Messages
- Confidence score prediction
- REST API using FastAPI
- Interactive frontend interface
- Lightweight and beginner-friendly ML architecture

---

#  Machine Learning Concept Used

The application uses:

- CountVectorizer for text vectorization
- Multinomial Naive Bayes for classification

The model is trained on sample text data and predicts the category of user-entered messages.

---

# 📂 Project Structure

```bash
ml_project_rida/
│
├── app.py                 # Main FastAPI application
├── model.py               # ML model training and prediction logic
│
├── templates/
   └── index.html         # Frontend UI
```

---

# ⚙️ Installation & Setup

---

## Install Dependencies

```bash
pip install fastapi uvicorn scikit-learn jinja2
```

---

## Run the Application

```bash
uvicorn app:app --reload
```

---

##  Open in Browser

```bash
http://127.0.0.1:8000
```

---

#  API Endpoint

## POST `/predict`

Predicts the category of a message.

### Request Body

```json
{
  "text": "Win a free iPhone now"
}
```

### Response

```json
{
  "category": "Spam",
  "confidence": 98.45
}
```

---

#  File Explanation

## `app.py`

Handles:

- FastAPI server setup
- API routes
- Frontend rendering
- Prediction requests

---

## `model.py`

Contains:

- Training dataset
- Text preprocessing
- CountVectorizer
- Naive Bayes model
- Prediction function

---

## `templates/index.html`

Frontend interface built using:

- HTML
- CSS
- JavaScript Fetch API

Allows users to enter messages and view predictions dynamically.

---

#  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend & ML |
| FastAPI | Web Framework |
| Scikit-learn | Machine Learning |
| HTML/CSS | Frontend Design |
| JavaScript | API Communication |


#  Learning Outcomes

Through this project, concepts learned include:

- Machine Learning model integration
- NLP basics
- REST API development
- Frontend-backend communication
- FastAPI architecture
- Real-time prediction systems

# ⭐ Conclusion

This project is a simple yet effective demonstration of how Machine Learning can be combined with web technologies to create intelligent applications capable of real-time text classification.
