from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/index/')
def test_render():
    param = dict()
    param['username'] = "Ученик"
    param['title'] = 'Домашняя страница'
    return render_template('index_old.html', **param)


@app.route('/base_page')
def base_render():
    return render_template("base.html")


@app.route('/child_page/<title>')
def child_render(title):
    return render_template("index.html", title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
