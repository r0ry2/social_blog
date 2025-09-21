from flask import Blueprint

# تعريف الـ blueprint مع تحديد مجلد القوالب
main = Blueprint("main", __name__, template_folder="templates")

# لازم نستورد views بعد تعريف الـ blueprint
from app.main import views
