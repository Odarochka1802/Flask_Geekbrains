from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


app.secret_key = "rrgtqeyq43t43t45t4qter"

@app.get('/submit')
def submit_get():
    context = {
        'login': 'Авторизация'
    }
    return render_template('form.html', **context)


@app.post('/submit')
def submit_post():
    session['login'] = request.form.get('login')
    session['email'] = request.form.get('email')
    return redirect(url_for('success'))


@app.route('/success/', methods=['GET', 'POST'])
def success():
    if 'login' in session:
        context = {
            'login': session['login'],
            'email': session['email'],
            'title': 'Добро пожаловать'
        }
        if request.method == 'POST':
            session.pop('login', None)
            session.pop('email', None)
            return redirect(url_for('submit_get'))
        return render_template('success.html', **context)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)


