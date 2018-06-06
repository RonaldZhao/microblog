from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data +
              '", remember_me=' + str(form.remember_me.data))
        return redirect('/')
    return render_template(
        'login.html',
        title='Sign In',
        form=form,
        providers=app.config['OPENID_PROVIDERS']
    )
