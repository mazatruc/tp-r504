from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@172.19.0.2/newuserdb'
db = SQLAlchemy(app)

from app import routes, models

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
