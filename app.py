from flask import Flask, request, jsonify
from saque import calcular_cedulas

app = Flask(__name__)

@app.route('/api/saque', methods=['POST'])
def saque():
    data = request.get_json()
    
    if not data or 'valor' not in data or not isinstance(data['valor'], int) or data['valor'] <= 0:
        return jsonify({"error": "Valor inválido"}), 400

    valor = data['valor']
    resultado = calcular_cedulas(valor)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)