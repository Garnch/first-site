from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("inderx.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f"User page: {name} - {id}"


if __name__ == '__main__':
    app.run(debug=True)
