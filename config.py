import os 
basedir = os.path.abspath(os.pathdirname(__file__))

class Config():
    FLASk_APP = os.environ.get('FLASK_APP')
    FLASK_ENV  = os.environ.get('FLASK_ENV')