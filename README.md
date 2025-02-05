# HNG-NumberClassification-API

This is a GitHub Repo for a number classification API that I built as a task during my HNG internship. For this task, I created a Flask-based API that can take a number and return interesting mathematical properties about it along with fun facts about that particular number. This API gets a number via a GET request and returns a JSON containing the classification, fun fact and properties. The properties to be returned include Armstrong, prime, perfect, odd and even.

## Table of Contents

-Installing the Flask API

-Using the API

-API Endpoint
- GET /api/classify-number
 
-Response Format
- Successful Response
- Error Response
 
-File and Code Structure

-Testing

-Deployment

## Installing the Flask API

### Prerequisites

1. Python

2. Python Packges Installer(PIP)

3. Terminal

### To create and run the API follow the steps below

1. Create your repository on GitHub

2. Clone that Repository to your local machine

```
Git Clone https://github.com/Dhee-Cloud/HNG-NumberClassification-API.git
cd HNG-NumberClassification-API.git
```

3. Install the required Dependencies

```
pip install -r requirement.txt
```

4. Run the Flask API App

```
python app.py
```

## Using the API
After setting up the API, you can perform a GET request to the `/api/classify-number` endpoint with a query parameter `number`

Example: 
```
http://127.0.0.1:5000/api/classify-number?number=371
```

Expected Response:
For an input that's valid like `371`, the expected response from the API will be

```
 {
     "number": 371,
     "is_prime": false,
     "is_perfect": false,
     "properties": ["armstrong", "odd"],
     "class_sum": 11,  // sum of its digits
     "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
 }

```

## API Endpoint

The endpoint is `/api/classify-number` and accepts a `number` query parameter and returns interesting mathematical properties about that particular number in JSON format, along with fun facts.

### parameter:
- `number`: This is the figure that needs to be classified

### Response:
- `"number"`: This is the figure that was entered.
- `"is_prime"`: This indicates if the figure is a prime number.
- `"is_perfect"`: This indicates if the figure is a perfect number.
- `"properties"`: This indicates the properties of the number.
- `"class_sum"`: It sums up all the digits in the figure given.
- `"fun_fact"`: This indicates a fun fact about the figure.

## Response Format
### Successful Response(200 OK)
For a successful response, the response should be format below:
```
{
     "number": 371,
     "is_prime": false,
     "is_perfect": false,
     "properties": ["armstrong", "odd"],
     "class_sum": 11,  // sum of its digits
     "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
 }
```

### Error Response(400 Bad Request)
To get a negative response like in a situation where you use alphabets instead of numbers , the response should be in the format below:
```
 {
     "number": "alphabet",
     "error": true
 }
```

## File and Code Structure

### Files

- README.md: This contains a detailed description of the task as well as the steps followed to complete the task.
- app.py: This is the main file containing the Flask App.
- requirement.txt: This is a file containing all the dependencies.
  
### Helper Functions
- `is_prime(n)`: Checks if a number is prime.
- `is_perfect(n)`: Checks if a number is perfect.
- `is_armstrong(n)`: Checks if a number is an Armstrong number.
- `sum_of_digits(n)`: Calculates the sum of digits of the number.
- `get_fun_fact(n)`: Returns a fun fact about the number.

## Testing
### To test the API:
- Run the Flask App `python app.py`
- Open another terminal
- Open Curl to send a `GET` request to the endpoint `/api/classify-number?number=<your_number>`
- Confirm your response is the expected response

### Example:
Positive Response
-  Input
  ```
  curl "http://127.0.0.1:5000/api/classify-number?number=371"
  ```
-  Response
```
   {
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

Negative Response
- Input
  ```
  curl "http://127.0.0.1:5000/api/classify-number?number=abc"
  ```
- Response
  ```
  {
    "number": "alphabet",
    "error": true
   }
  ```

## Deployment
For the deployment, we will be using an AWS Ec2 Instance following the steps below:

-Create your Ec2 Instance

-Connect into your instance using SSH
-Cloe your github repo
-Install the depencies
-Run the flask app








   
   

