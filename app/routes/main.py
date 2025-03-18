# TODO: Main Interface
## User Info -> Movie -> Labeling -> Feedback
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse(
        name="form.html",
        request=request
    )

@router.post("/submit")
async def submit(request: Request):
    form_data = await request.form()  # 모든 폼 데이터를 가져옴
    data_dict = dict(form_data)  # Starlette MultiDict → 일반 dict 변환

    print("\n📩 **폼 응답 데이터 수신:**")
    for key, value in data_dict.items():
        print(f"{key}: {value}")

    return JSONResponse(content={"message": "폼이 성공적으로 제출되었습니다!", "data": data_dict})