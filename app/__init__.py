from flask import Flask, render_template, request, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from admin import admin

app = Flask('app')
app.config.update(
    DEBUG=True,
    SQLALCHEMY_DATABASE_URI='sqlite:///../database.db'
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

app.register_blueprint(admin, url_prefix='/admin')

@app.route('/')
def home():
    return 'Breaking News Banners go here'
