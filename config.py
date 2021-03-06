import os 
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zproject_demo'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,
	    HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

TESTING = True