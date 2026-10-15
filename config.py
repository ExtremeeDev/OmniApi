import os

class Config:
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 5000))
