from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello world!"


if __name__ == "__main__":
    app.run()




# <link rel="icon" type="image/png" sizes="16x16" href="/favicon.ico">