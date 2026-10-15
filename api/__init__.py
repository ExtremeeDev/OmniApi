# @ ExtremeeDev On Telegram 

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Routes ko register kar rahe hain
    from .routes import api_bp
    app.register_blueprint(api_bp)
    
    return app
