# Lunch Picker (Vue 3 + Python)

가볍게 점심 메뉴를 추천받는 웹앱입니다.

## 기술 스택
- Frontend: Vue 3 (CDN 방식)
- Backend: Python FastAPI + Uvicorn

## 프로젝트 구조
- `frontend/index.html`: Vue 3 화면
- `backend/main.py`: FastAPI API 서버

## 실행 방법
### 1) 백엔드 실행
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

### 2) 프론트엔드 실행
새 터미널에서:
```bash
python3 -m http.server 5173 --directory frontend --bind 0.0.0.0
```

### 3) 접속
- 로컬: `http://localhost:5173`
- 모바일(같은 네트워크): `http://<내PC-IP>:5173`

## API
- `GET /api/health`
- `GET /api/menus`
- `GET /api/menus/random`
