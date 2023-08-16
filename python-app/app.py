from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_answer():
    return 'This is from Python app :42 \n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
