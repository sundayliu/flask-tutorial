# -*- coding:utf-8 -*-

from flask import Flask,render_template,session,redirect,url_for
from flask import request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
    
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 505
    
if __name__ == '__main__':
    #print(__name__)
    app.run(debug=True)
    #manager.run()