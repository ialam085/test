from flask import Flask
app = Flask(__name__)

@app.route('/login')
def login():
    return "Login Successful"

if __name__ == '__main__':
    app.run(host='0.0.0.0')