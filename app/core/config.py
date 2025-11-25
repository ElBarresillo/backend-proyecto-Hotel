import os
import jwt
import datetime
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
