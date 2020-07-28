from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'cnt4713!':
            return render_template('menu.html')
        else:
            return render_template('index.html', message='Incorrect or empty password submitted!')

@app.route('/static', methods=['POST'])
def play():
    return render_template('static.html')

@app.route('/stream', methods=['POST'])
def stream():
    return render_template('stream.html')

@app.route('/menu', methods=['POST'])
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.debug = True
    app.run()