import os
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# Helper functions
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 0:
        return False  
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_armstrong(n):
    if n < 0:
        return False
    digits = [int(digit) for digit in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_param = request.args.get('number')
    
    try:
        number = int(number_param)
    except (ValueError, TypeError):
        return jsonify({"error": True}), 400  # Fix incorrect error response format
    
    # Determine properties
    prime = is_prime(number)
    perfect = is_perfect(number)
    armstrong = is_armstrong(number)
    odd = number % 2 != 0
    properties = []

    if armstrong:
        properties.append("armstrong")
    properties.append("odd" if odd else "even")

    # Fetch fun fact with error handling
    fun_fact = f"No fun fact available for {number}"  # Default message
    try:
        response = requests.get(f"http://numbersapi.com/{number}?json", timeout=3)
        if response.status_code == 200:
            fun_fact = response.json().get('text', fun_fact)
    except requests.RequestException:
        pass  # Keep the default message if API fails

    # Prepare response
    response_data = {
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "class_sum": digit_sum(number),  # Fixed key name
        "fun_fact": fun_fact
    }
    
    return jsonify(response_data), 200

if _name_ == '_main_':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
