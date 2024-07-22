from flask import Flask, request, render_template
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    x = data['x']
    y = data['y']
    pyautogui.moveRel(x, y)
    return '', 204

@app.route('/click', methods=['POST'])
def click():
    pyautogui.leftClick()
    return '', 205

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
