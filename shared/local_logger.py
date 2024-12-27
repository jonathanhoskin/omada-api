from datetime import datetime

def log(message):
  now = datetime.now().isoformat()
  print(f"[{now}] {message}")
