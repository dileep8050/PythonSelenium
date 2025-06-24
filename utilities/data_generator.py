import random
import string
from datetime import datetime

def generate_random_gmail():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    email = f"testuser_{random_str}_{timestamp}@gmail.com"
    return email
