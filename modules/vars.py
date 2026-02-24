#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "31445635"))
API_HASH = environ.get("API_HASH", "15c057ca3aa85360ac3d63de52368718")
BOT_TOKEN = environ.get("BOT_TOKEN", "8261884293:AAFmSfI-zE2rduTKIdaQhdlWINvBM03VNz0")

OWNER = int(environ.get("OWNER_ID", "8441048952"))
CREDIT = environ.get("CREDIT", "😇")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', environ.get("OWNER_ID", "8441048952")).split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER if user_id.strip().isdigit()]

AUTH_USER = os.environ.get('AUTH_USERS', environ.get("OWNER_ID", "8441048952")).split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER if user_id.strip().isdigit()]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
# api_url = "http://master-api-v3.vercel.app/"
# api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.







