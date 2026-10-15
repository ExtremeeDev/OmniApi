from api import create_app
from config import Config

app = create_app()

if __name__ == '__main__':
    print(f"🔥 OmniApi is running on http://{Config.HOST}:{Config.PORT} by @ExtremeeDev")
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
