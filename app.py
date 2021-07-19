from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'testing':
            return render_template('stream_static.html')
        else:
            return render_template('index.html', message='wrong or empty password')

@app.route('/static', methods=['POST'])
def play():
    return render_template('static.html')

@app.route('/stream', methods=['POST'])
def stream():
    return render_template('stream.html')

@app.route('/stream_stati', methods=['POST'])
def back():
    return render_template('stream_static.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run()
