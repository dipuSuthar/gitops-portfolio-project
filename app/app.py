import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)


REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))


redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route('/')
def hello():
    try:
        count = redis_client.incr('visitor_count')
        return f"Hello, DevOps! 🚀 You are visitor number {count}."
    except redis.RedisError:
        return "Hello! (Database connection failed) 🚨", 500


@app.route('/healthz')
def healthz():
    return jsonify({"status": "healthy"}), 200


@app.route('/ready')
def ready():
    try:
        redis_client.ping()
        return jsonify({"status": "ready", "database": "connected"}), 200
    except redis.RedisError:
        return jsonify({"status": "not ready", "database": "disconnected"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)