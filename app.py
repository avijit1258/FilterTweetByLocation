from flask import Flask
from flask import request
from flask import render_template
app = Flask('app')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return "Hello World"
    else:
        return render_template('home.html')


app.run(host='0.0.0.0', port=8082)
