import time
import platform
import psutil
from fastapi import APIRouter

router = APIRouter()

START_TIME = time.time()

def format_uptime(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}h {minutes}m {seconds}s"

@router.get("/health")
def health_check():
    uptime_seconds = int(time.time() - START_TIME)

    return {
        "status": "healthy",
        "uptime": format_uptime(uptime_seconds),
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "memory_usage": f"{psutil.virtual_memory().percent}%",
        "python_version": platform.python_version(),
        "os": platform.system(),
        "os_version": platform.release(),
    }