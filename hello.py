from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('Informe seu nome:', validators=[DataRequired()])
    lastname = StringField('Informe seu sobrenome:', validators=[DataRequired()])
    EducationIntitute = StringField('Informe sua instituição de ensino:', validators=[DataRequired()])
    subject = SelectField('Informe sua instituição de ensino:', choices= [('dswa5', 'DSWA5'), ('dwba4', 'DWBA4'), ('gpsa5', 'Gestão de projetos')])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_lastname = session.get('lastname')
        old_EducationIntitute = session.get('EducationIntitute')
        old_subject = session.get('subject')
        session['name'] = form.name.data
        session['lastname'] = form.lastname.data
        session['EducationIntitute'] = form.EducationIntitute.data
        session['subject'] = form.subject.data
        
        return redirect(url_for('index'))
    
    url = request.remote_addr
    ip = request.host_url

    return render_template('index.html', form=form, name=session.get('name'), lastname=session.get('lastname'), EducationIntitute=session.get('EducationIntitute'), subject=session.get('subject'), url=url, ip=ip, current_time=datetime.utcnow() )



       



    #Coewmntaiosd