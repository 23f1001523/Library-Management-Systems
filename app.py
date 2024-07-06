from flask import Flask, render_template, request, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy
import time,os

from controllers import *

app = Flask(__name__, template_folder='templates')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lms.sqlite3"

db.init_app(app)

app.app_context().push()

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
