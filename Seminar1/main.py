from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/categories/')
def categories():
    categories_list = {"clothes": "clothes.html", "shoes": "shoes.html", "sports": "sports.html",
                       "accessories": "accessories.html"}
    return render_template('categories.html', categories_list=categories_list)


@app.route('/clothes/')
def clothes():
    clothes_list = [
        {'name': 'Футболка', 'price': 169.99},
        {'name': 'Джинсы', 'price': 339.99},
        {'name': 'Платье', 'price': 349.99}
    ]
    return render_template('clothes.html', list=clothes_list)


@app.route('/shoes/')
def shoes():
    shoes_list = [
        {'name': 'Кроссовки', 'price': 196.99},
        {'name': 'Кеды', 'price': 369.99},
        {'name': 'Туфли', 'price': 469.99}
    ]
    return render_template('shoes.html', list=shoes_list)


@app.route('/sports/')
def sports():
    sports_list = [
        {'name': 'Форма', 'price': 78519.99},
        {'name': 'Тренажер', 'price': 3439.99},
        {'name': 'Гантеля', 'price': 479.99}
    ]
    return render_template('sports.html', list=sports_list)


@app.route('/accessories')
def accessories():
    accessories_list = [
        {'name': 'Серьги', 'price': 196.99},
        {'name': 'Кольцо', 'price': 398.99},
        {'name': 'Подвеска', 'price': 4999.99}
    ]
    return render_template('accessories.html', list=accessories_list)


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
