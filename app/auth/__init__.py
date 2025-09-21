from flask import Blueprint

auth = Blueprint("auth", __name__, template_folder="templates")

# ✅ استيراد مطلق
from app.auth import views
