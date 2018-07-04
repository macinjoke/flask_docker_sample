from flask import Flask
from config import config
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask with Docker!"

if __name__ == "__main__":
    app.run(host=config['host'])
