from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def headers():
    headers = request.headers
    return '<br>'.join([f'{key}: {value}' for key, value in headers.items()])

if __name__ == '__main__':
    app.run(debug=True)
