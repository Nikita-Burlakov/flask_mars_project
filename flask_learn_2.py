from flask import Flask, url_for, request, render_template

app = Flask(__name__)


prof_list = ["инженер-исследователь",
             "пилот",
             "строитель",
             "экзобиолог",
             "врач",
             "инженер по терраформированию",
             "климатолог",
             "специалист по радиационной защите",
             "астрогеолог",
             "гляциолог",
             "инженер жизнеобеспечения",
             "метеоролог",
             "оператор марсохода",
             "киберинженер",
             "штурман",
             "пилот дронов"]


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


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    params = {"prof_list": prof_list,
              "href": url_for('static', filename='css/style.css')}

    if list_type != "ol" and list_type != "ul":
        return "Неправильный формат списка"
    elif list_type == "ul":
        return render_template("index_2.html", ul_list=True, **params)
    return render_template("index_2.html", ul_list=False, **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
