from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/api/signin', methods=['POST'])
def signin():
    email = request.form['email']
    password = request.form['password']

    return jsonify({
        'email': email,
        'password': password
    })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)