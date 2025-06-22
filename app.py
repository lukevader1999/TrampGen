from flask import Flask, jsonify
from KuerGenerator import KuerGenerator

app = Flask(__name__, static_folder='static')

myKuerGenerator = KuerGenerator()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/generate_kuer', methods=['GET'])
def generate_kuer():
    liste = myKuerGenerator.get_new_kuer()
    liste: list[str] = [s.name for s in liste]
    return jsonify({'liste': liste})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)