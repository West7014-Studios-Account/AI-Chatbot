from flask import Flask, request, jsonify
import openai

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

# Set up Flask app
app = Flask(__name__)

# Define chat AI function
def chat_ai(prompt):
    # Call OpenAI GPT-3 API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=10,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Retrieve the generated response text
    return response.choices[0].text.strip()

# Define chat API endpoint
@app.route('/chat', methods=['POST'])
def chat():
    # Retrieve user's message from the request form
    message = request.form['message']
    # Generate response using the chat AI function
    response = chat_ai("User: " + message + "\nAI:")
    # Return the response as a JSON object
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()
