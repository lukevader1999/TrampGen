from flask import Flask, jsonify
from generate_kuer import generate_kuer as generate_kuer_list
from Sprung import Sprung
from SprungFilter import SprungFilter

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/generate_kuer', methods=['GET'])
def generate_kuer():
    sprung_filter = SprungFilter(max_rotationen=2, max_schrauben=1,filter_json_path="filter.json")
    liste: list[Sprung] = generate_kuer_list(sprung_filter=sprung_filter)
    liste: list[str] = [s.name for s in liste]
    return jsonify({'liste': liste})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)