from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.set("ime","123")
    redis.set("ime2","Marko")
    imena="First name: %s \n" %redis.get("ime")+"Second name: %s" %redis.get("ime2")
    return imena

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)