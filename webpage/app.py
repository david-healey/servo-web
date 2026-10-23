from flask import Flask, send_file, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html') as f:
        return Response(f.read(), mimetype='text/html')

@app.route('/image')
def image():
    return send_file('colby.jpeg', mimetype='image/jpeg')

@app.route('/open', methods=['POST'])
def open_servo():
    try:
        requests.post('http://servo:8081/open', timeout=2)
    except Exception as e:
        print("Error contacting servo:", e)
    return '', 204

@app.route('/close', methods=['POST'])
def close_servo():
    try:
        requests.post('http://servo:8081/close', timeout=2)
    except Exception as e:
        print("Error contacting servo:", e)
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
