import os
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Helper functions to determine properties of a number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 0:
        return False  # Handle non-positive numbers
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_armstrong(n):
    if n < 0:
        return False
    digits = [int(digit) for digit in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def digit_sum(n):
    return sum(int(digit) for digit in str(abs(int(n))))  # Handle floating-point numbers

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Check if the input is a valid number (integer or floating-point)
    try:
        number = float(number)  # Accept both integers and floating-point numbers
    except (ValueError, TypeError):
        return jsonify({"number": "alphabet", "error": True}), 400

    # Calculate properties
    prime = is_prime(int(number)) if number.is_integer() else False  # Prime only for integers
    perfect = is_perfect(int(number)) if number.is_integer() else False  # Perfect only for integers
    armstrong = is_armstrong(int(number)) if number.is_integer() else False  # Armstrong only for integers
    odd = int(number) % 2 != 0 if number.is_integer() else False  # Odd/even only for integers

    properties = []
    if armstrong:
        properties.append("armstrong")
    if number.is_integer():
        properties.append("odd" if odd else "even")

    # Fetch the fun fact from Numbers API (math type)
    try:
        fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math?json")
        fun_fact_response.raise_for_status()  # Raise an error for bad status codes
        fun_fact = fun_fact_response.json().get('text', f"No fun fact available for {number}")
    except requests.RequestException as e:
        fun_fact = f"Failed to fetch fun fact: {str(e)}"

    # Prepare response
    response = {
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "class_sum": digit_sum(number),  # Sum of digits
        "fun_fact": fun_fact
    }

    return jsonify(response), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
