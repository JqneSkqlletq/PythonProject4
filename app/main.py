from pydoc import describe
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.forms import KupitForm
from app.database import Config
from app.forms import LoginForm, TovarForm

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = KupitForm()
    from models import Tovar, Category

    tovars = Tovar.query.filter(Tovar.price < 300).order_by(Tovar.name).all()

    category = Category.query.filter_by(name="Electronics").first()
    if category:
        electronics = category.tovars.all()
        print("Электроника:", electronics)

    laptop = Tovar.query.filter_by(name="Laptop").one_or_none()
    if laptop:
        print("Товар 'Laptop':", laptop.name, laptop.price)

    first_tovar = Tovar.query.filter(Tovar.ostatok > 100).first()
    if first_tovar:
        print("Первый товар с остатком больше 100:", first_tovar.name, first_tovar.ostatok)

    if form.validate_on_submit():
        print(form.kolvo.data)
        print(type(form.kolvo.data))
        return render_template('index.html', tovars=tovars, form=form)
    else:
        return render_template('index.html', tovars=tovars, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form3 = LoginForm()
    if form3.validate_on_submit():
        from models import User
        name = form3.username.data
        proverka = User.query.filter_by(name=name).one_or_none()
        print(proverka)
        if proverka is None:
            data = User(name=form3.username.data, password=form3.pasword.data, is_active=True)
            db.session.add(data)
            db.session.commit()

            flash('YES')
            flash('User ' + name + ' Registered')
        else:
            flash('User ' + name + ' Already Exists')
        return redirect(url_for('login'))
    return render_template('login.html', form2=form3)

@app.route('/tovar_add', methods=['GET', 'POST'])
def tovar_add():
    form = TovarForm()
    if form.validate_on_submit():
        from models import Tovar
        name = form.name.data
        price = form.price.data
        ostatok = form.ostatok.data
        data = Tovar(name=name, price=int(price), ostatok=int(ostatok))
        db.session.add(data)
        db.session.commit()
        flash('Товар Добавлен')
        return redirect('index')
    return render_template('tovar_add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5001)







