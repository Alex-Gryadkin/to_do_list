import os
basedir = os.path.abspath(os.path.dirname(__file__))


#  defends the app form Cross-Site Requests Forgery (CSRF - 'seasurf')
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '!34341232zoweuyqriouy132894723fd2389ery9123ye23gd2g3dr789123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False