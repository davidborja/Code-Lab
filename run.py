import os

from app import create_app

flask_env = os.environ.get("FLASK_ENV")

if not flask_env:
    flask_env = "local"


app = create_app(flask_env)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
