from flask import render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/locations')
def locations():
    return render_template('locations.html', title='Locations', content=True)


@app.route('/data')
def data():
    return render_template('data.html', title='Data Entry', content=True)

@app.route('/accounts')
def accounts():
    return render_template('accounts.html', title='Manage Accounts', content=True)

@app.route('/appsetup')
def appsetup():
    return render_template('appsetup.html', title='Setup App', content=True)