from django.test import TestCase
import requests
from django.http import JsonResponse


# URL endpoint for retrieving trivia questions
# Example URL for 10 trivia questions
url = "https://opentdb.com/api.php?amount=40&type=multiple"  

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the JSON data from the response
    trivia_data = response.json()

    # Process the trivia data
    for result in trivia_data['results']:
        # Extract and print the question
        print("Question:", result['question'])
        # Extract and print the correct answer
        print("Correct Answer:", result['correct_answer'])
        # Extract and print the incorrect answers (if available)
        if 'incorrect_answers' in result:
            print("Incorrect Answers:", result['incorrect_answers'])
        print("\n")
else:
    print("Failed to retrieve trivia questions. Status code:", response.status_code)
