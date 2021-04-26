from flask import Flask

app = Flask(__name__)


@app.route('/image_mars')
def image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/img/MARS.png" alt="пикча(">
                        <p>Вот она какая, красная планета.</p>
                    </body>
                  </head>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')