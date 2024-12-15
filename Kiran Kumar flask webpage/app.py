from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '_main_':
    app.run(debug=True)