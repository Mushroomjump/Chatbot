import asyncio
from rasa.core.agent import Agent

# Load your trained Rasa chatbot model
model_path = 'C:/Users/Anna Kima/Desktop/Chatbot/models/20240301-154513-massive-request.tar.gz'
domain_path = 'C:/Users/Anna Kima/Desktop/Chatbot/domain.yml'
agent = Agent.load(model_path)

# Define a function to generate responses
async def generate_response(user_input):
    # Await the response from the Rasa model
    response = await agent.handle_text(user_input)
    # Extract the response text from the Rasa response
    response_text = response[0]["text"] if response else "Sorry, I didn't understand that."
    return response_text

# Test the model with some sample inputs
async def main():
    sample_inputs = [
        "How do i get a loan from absa",
        "What is bitcoin?",
        "How can i get a crypto loan",
    ]

    for input_text in sample_inputs:
        response = await generate_response(input_text)
        print(f"User: {input_text}")
        print(f"Bot: {response}")
        print()

# Run the main function
asyncio.run(main())
