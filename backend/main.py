from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Lunch Menu API", version="0.1.0")

menus = [
    "김치찌개",
    "된장찌개",
    "비빔밥",
    "제육볶음",
    "돈까스",
    "순두부찌개",
    "칼국수",
    "쌀국수",
    "초밥",
    "샐러드",
    "포케",
    "샌드위치",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/menus")
def get_menus() -> dict[str, list[str]]:
    return {"menus": menus}


@app.get("/api/menus/random")
def get_random_menu() -> dict[str, str]:
    return {"menu": random.choice(menus)}
