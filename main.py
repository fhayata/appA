from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mirror', methods=['POST'])
def mirror():
    data = request.json
    string_to_mirror = data.get('string', '')
    mirrored_string = string_to_mirror[::-1]
    return jsonify({'mirrored_string': mirrored_string})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
