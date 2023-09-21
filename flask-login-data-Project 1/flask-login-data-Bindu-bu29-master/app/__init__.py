"""This is the app demonstrates logging_config configuration and unit testing"""
import logging
import os

from flask import Flask, render_template, flash, request, redirect, url_for, session
from app import logging_config
from app.config import Config
import pandas as pd


def create_app(test_config=None):
    logging_config.logging_setup()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        debug=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/about/')
    def about():
        return render_template("about.html")

    @app.route('/portfolio/')
    def portfolio():
        return render_template("portfolio.html")

    @app.route('/thanks/')
    def thanks():
        return render_template("thanks.html")

    @app.route('/logout/')
    def logout():
        session['admin'] = "False"
        return render_template("index.html")

    @app.route('/show_contacts/')
    def show_contacts():
        if 'admin' in session and session['admin'] == "True":
            data = pd.read_csv(os.path.join(Config.LOG_DIR, "contact_log.log"), delimiter=";", header=None)
            data.columns = ['Time', 'Email', 'Name', 'Message']
            return render_template('show_contacts.html', tables=[data.to_html()], titles=['Time', 'Email', 'Name', 'Message'])
        return redirect(url_for('login'))

    @app.route('/contact/', methods=('GET', 'POST'))
    def contact():
        if request.method == 'POST':
            email = request.form['email']
            message = request.form['message']
            name = request.form['name']
            if not name:
                flash('Name is Required')
            elif not email:
                flash('Email is Required')
            elif not message:
                flash('Message is Required')
            else:
                contact_logger = logging.getLogger("contact_log")
                contact_logger.info(f"{email};{name};{message}")
                return redirect(url_for('thanks'))

        return render_template("contact.html")

    @app.route('/login/', methods=('GET', 'POST'))
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if not username:
                flash('Username is Required')
            elif username != "admin":
                flash('Invalid Username')
            elif not password:
                flash('Password is Required')
            elif password != "password":
                flash('Invalid password')
            else:
                session['admin'] = "True"
                return redirect(url_for('show_contacts'))

        return render_template("login.html")

    return app
