from flask import Flask, url_for

app = Flask(__name__)

text = '''Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!'''
text = text.split('\n')


@app.route('/')
def home():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "</br>".join(text)


@app.route('/image_mars')
def show_picture():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars_small.png')}"></br>
                    Вот она какая, красная планета.
                  </body>
                </html>"""


########
########


@app.route('/test_page')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                    <h2>lmao bottom text</h2>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
