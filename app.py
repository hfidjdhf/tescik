from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Wczytaj dane z pliku
data = {}
with open('turnik.txt', 'r') as file:
    for line in file:
        if ':' in line:
            nick, ip = line.strip().split(':')
            data[nick] = ip

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find', methods=['GET'])
def find_ip():
    nick = request.args.get('nick')
    ip = data.get(nick)
    if ip:
        return jsonify({"ip": ip}), 200
    else:
        return jsonify({"error": "Nie znaleziono adresu IP dla tego nicku."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
