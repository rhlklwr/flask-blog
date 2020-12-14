import os

class Config():
    SECRET_KEY = '0def4e83ebac03fca5434e7a8a30644b'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = "emailwithpython8@gmail.com"
    MAIL_PASSWORD = "rahultemp@123"