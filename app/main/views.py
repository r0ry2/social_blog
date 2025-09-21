from flask import render_template
from flask_login import login_required, current_user
from app.main import main   # استيراد blueprint

@main.route('/')
def index():
    # استدعاء القالب index.html من داخل templates/main/
    return render_template("main/index.html")

@main.route('/create')
@login_required
def create_post():
    return f"Hello {current_user.username}, write your post here!"
