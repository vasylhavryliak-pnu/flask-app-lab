from flask import request, redirect, url_for, render_template, abort
from . import app

@app.route('/')
def resume():
    return render_template('resume.html', title='Резюме — Василь Гавриляк')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Контакти')

@app.route('/homepage')
def home():
    """View for the Home page of your website."""
    agent = request.user_agent
    return render_template('homepage.html', title='Homepage', agent=agent)