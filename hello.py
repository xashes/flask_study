from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap

from tt.data import get_positions

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/stock/positions')
def positions():
    positions = get_positions().to_html()
    return render_template('positions.html', positions=positions)

@app.route('/stock/<code>')
def lookup_stcok_on_xueqiu(code):
    return redirect('https://xueqiu.com/S/{}'.format(code))

if __name__ == '__main__':
    app.run(debug=True)
