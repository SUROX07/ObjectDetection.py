from flask import Flask, render_template, Response
import subprocess
app =Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    # Start the Python game here
    subprocess.Popen(['python', 'camera.py'])
    return 'Starting Detection program....'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug= True)