from flask import Flask, request, jsonify

app = Flask(__name__)

TAX_RATE = 0.10  # 10%

@app.route('/tax')
def tax():
    amount = request.args.get('amount')

    if amount is None:
        return jsonify({'error': 'amount is required'}), 400

    try:
        amount = float(amount)
    except ValueError:
        return jsonify({'error': 'amount must be a number'}), 400

    tax = amount * TAX_RATE

    return jsonify({
        'amount': amount,
        'tax': tax,
        'total': amount + tax
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
