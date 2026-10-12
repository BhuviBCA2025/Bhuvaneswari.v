from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "result": ""
        }
    )


@app.post("/ask", response_class=HTMLResponse)
def ask(request: Request, question: str = Form(...)):

    question = question.strip()

    if not question:
        result = "Please enter a question."

    elif "ocean" in question.lower():
        result = "The Pacific Ocean is the largest ocean in the world."

    elif "python" in question.lower():
        result = "Python is a popular programming language used for web development, AI, data science and automation."

    else:
        result = "EduGenie: Please ask an educational question."

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "result": result
        }
    )