from flask import Flask
import datetime

now = datetime.datetime.now()

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/Santiago')
def Santiago():
    return "Santiago"

@app.route('/helloworld')
def helloworld():
    return "Hello, world"

@app.route('/currentservertime')
def currentservertime():
    return now.strftime("%Y%m%dT%H%M%S")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
