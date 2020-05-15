import os
from flask import Flask, request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return "Go on /put route to put data, and on /get to read your data"

@app.route('/put', methods=['GET', 'POST'])
def put():
    if request.method == 'POST':
        data = request.form["putdata"]
        redis.append("ime2",data+" ")
    return '''
        <form method="post">
        <p><input type=text name=putdata>
        <p><input type=submit value=Putdata>
        </form>
    '''
@app.route('/get')
def get():
    data = redis.get("ime2")
    return data
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)