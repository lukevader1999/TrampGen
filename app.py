from flask import Flask, jsonify, send_from_directory
from KuerGenerator import KuerGenerator
import os

app = Flask(__name__, static_folder='frontend_react/build', static_url_path='')

myKuerGenerator = KuerGenerator()

@app.route('/generate_kuer', methods=['GET'])
def generate_kuer():
    liste = myKuerGenerator.get_new_kuer()
    liste: list[str] = [s.name for s in liste]
    return jsonify({'liste': liste})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)