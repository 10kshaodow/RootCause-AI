from datetime import datetime, timedelta
from pathlib import Path

def generate_logs():
    events = [
        ("INFO", "Server started"),
        ("INFO", "Database connected"),
        ("WARN", "Memory usage reached 85%"),
        ("WARN", "Memory usage reached 96%"),
        ("ERROR", "Memory allocation failed"),
        ("CRITICAL", "Worker process terminated")
    ]

    Path("logs").mkdir(exist_ok=True)
    start = datetime.now()

    with open("logs/system.log", "w") as file:
        for index, (level, message) in enumerate(events):
            timestamp = start + timedelta(seconds=index * 2)
            file.write(
                f"{timestamp.isoformat()} "
                f"[{level}] {message}\n"
            )

if __name__ == "__main__":
    generate_logs()
    print("System log generated.")