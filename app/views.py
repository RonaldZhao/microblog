from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ronald Zhao'}
    comments = [
        {
            'user': 'user1',
            'content': 'flask is very good.'
        },
        {
            'user': 'user2',
            'content': 'python is very good.'
        },
        {
            'user': 'user2',
            'content': 'python is very good.'
        },
        {
            'user': 'user2',
            'content': 'python is very good.'
        },
        {
            'user': 'user2',
            'content': 'python is very good.'
        },
        {
            'user': 'user2',
            'content': 'python is very good.'
        }
    ]
    # return 'Hello, world!'
    return render_template(
        'index.html',
        title='Home',
        user=user,
        comments=comments
    )
