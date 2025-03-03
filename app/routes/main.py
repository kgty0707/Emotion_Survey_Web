# TODO: Main Interface
## User Info -> Movie -> Labeling -> Feedback
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse(
        name="form.html",
        request=request
    )