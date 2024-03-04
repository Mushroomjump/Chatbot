from flask import Flask, request, jsonify
from rasa.core.agent import Agent

app = Flask(__name__)

# Load your trained Rasa chatbot model
model_path = 'C:/Users/Anna Kima/Desktop/Chatbot/models/nlu-20240301-121217-electrical-key.tar.gz'
agent = Agent.load(model_path)

# Define your chatbot model or function for generating responses
def generate_response(user_input):
    # Retrieve response from the Rasa model
    response = agent.handle_text(user_input)
    # Extract the response text from the Rasa response
    response_text = response[0]["text"] if response else "Sorry, I didn't understand that."
    return response_text

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get user input from the request
            user_input = request.form['user_input']
            # Generate response using the chatbot model
            response = generate_response(user_input)
            # Return the response to the client
            return jsonify({"result": response})
        except Exception as e:
            # Log the error for debugging
            print("Error:", e)
            return jsonify({"result": "Error processing request."}), 500
    else:
        # Render the HTML page for the chatbot
        return app.send_static_file('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
