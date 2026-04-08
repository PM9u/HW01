# 빌드 최적화를 위해 slim 기반 이미지 사용
FROM python:3.11-slim

# 환경 변수 설정 (바이트코드 생성 방지 및 버퍼링 비활성화)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 작업 디렉토리 생성 및 설정
WORKDIR /app

# 의존성 파일 먼저 복사 (Docker 캐시 레이어 활용을 위해)
COPY requirements.txt /app/

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY ./app /app/app

# 서버를 실행할 포트 지정
EXPOSE 8000

# 컨테이너 시작 시 실행될 명령어 (uvicorn 사용)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
