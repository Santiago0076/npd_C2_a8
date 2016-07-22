from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/Santiago')
def Santiago():
    return "Santiago"

@app.route('/helloworld')
def helloworld():
    return "Hello, world"

@app.route('/currentservertime')
def currentservertime():
    currentservertime = datetime.datetime.now()
    return currentservertime

if __name__ == '__main__':
    app.run(port=5000, debug=True)
