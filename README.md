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
 
-File Structure

-Testing

-Deployment

-Performance

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
http://127.0.0.1:5000/api/classify-number?number=432
```

Expected Response:
For an input that's valid like `432`, the expected response from the API will be



   
   

