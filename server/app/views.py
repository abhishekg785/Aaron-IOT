"""
    author : abhishek goswami
    abhishekg785@gmail.com

    views.py : handling the routes
"""
from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'hello'