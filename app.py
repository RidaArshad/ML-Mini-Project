from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict_message

# ---------- APP ----------
app = FastAPI()

# ---------- CORS FIX ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- TEMPLATES ----------
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    text: str

# ---------- HOME ROUTE ----------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/predict")
def predict(msg: Message):
    print("Received:", msg.text)  

    category, confidence = predict_message(msg.text)

    return {
        "category": category,
        "confidence": confidence
    }