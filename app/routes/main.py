# TODO: Main Interface
## User Info -> Movie -> Labeling -> Feedback
import os
import pandas as pd
from fastapi import APIRouter, Request
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

# CSV 저장 디렉토리 설정
CSV_DIR = "survey_results"
os.makedirs(CSV_DIR, exist_ok=True)  # 폴더가 없으면 자동 생성

@router.post("/submit")
async def submit(request: Request):
    form_data = await request.form()  # 모든 폼 데이터를 가져옴
    data_dict = dict(form_data)  # Starlette MultiDict → 일반 dict 변환

    print("\n📩 **폼 응답 데이터 수신:**")
    for key, value in data_dict.items():
        print(f"{key}: {value}")

    # `name` 필드 확인 (없으면 기본값 지정)
    name = data_dict.get("name", "unknown").replace(" ", "_")  # 공백 제거

    # CSV 파일 경로 설정
    csv_filename = f"survey_results_{name}.csv"
    csv_filepath = os.path.join(CSV_DIR, csv_filename)

    # DataFrame 생성 및 저장
    df = pd.DataFrame([data_dict])  # 단일 응답을 CSV에 저장
    df.to_csv(csv_filepath, mode="a", index=False, header=not os.path.exists(csv_filepath), encoding="utf-8-sig")

    print(f"✅ CSV 파일 저장 완료: {csv_filepath}")

    return JSONResponse(content={"message": "폼이 성공적으로 제출되었습니다!", "file": csv_filepath})