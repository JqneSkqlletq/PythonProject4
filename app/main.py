from flask import Flask, render_template, flash, redirect, url_for
import os
from app.forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form3 = LoginForm()
    if form3.validate_on_submit():
        print(form3.username.data)
        print(form3.pasword.data)
        print(form3.remember_me.data)

        flash('YES')
        return redirect(url_for('login'))
    return render_template('login.html', form2=form3)


if __name__ == '__main__':
    app.run(debug=True,port=5001)