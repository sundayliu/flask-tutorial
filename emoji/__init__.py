# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, flash, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap

# Create the Flask application
app = Flask(__name__)

# Create the Flask-SQLAlchemy object
db = SQLAlchemy(app)

# Create Bootstrap object
bootstrap = Bootstrap(app)

# Config database uri
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:123456@127.0.0.1:3306/emoji?charset=utf8mb4'
# config secret key
app.config['SECRET_KEY'] = 'kd8273f784jkkdjkj(jdj3'


class Info(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.Unicode(40), nullable=False)


class InfoForm(Form):
    content = StringField('content', validators=[Required()])
    submit = SubmitField('submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        info = Info(content=form.content.data)
        db.session.add(info)
        db.session.commit()
        flash(u'添加成功')
        return redirect(url_for('index'))
    infos = [{"content": info.content} for info in Info.query.order_by(Info.id.desc())]
    return render_template('test.html', form=form, infos=infos)


if __name__ == '__main__':
    app.run(debug=True)