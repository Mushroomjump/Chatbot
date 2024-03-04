import os
import random

import yaml
from rasa.core.agent import Agent


def load_domain(domain_path):
    with open(domain_path, 'r') as file:
        domain_data = yaml.safe_load(file)
    return domain_data.get('responses', {})


async def load_nlu_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model '{model_path}' not found.")

    # Load NLU agent
    agent = Agent.load(model_path=model_path)
    return agent

async def generate_response(agent, domain_responses):
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Predict intent using NLU model
        result = await agent.parse_message(user_input)

        # Extract intent from the parsed result
        predicted_intent = result["intent"]["name"]

        # Get response from domain file using correct key
        responses = domain_responses.get(f'utter_{predicted_intent}', "I'm sorry, I don't have a response for that.")

        # Print text
        if isinstance(responses, str):
            print(responses)
        else:
            for response in responses:
                print(response.get('text', ''))
    print(f'utter_{predicted_intent}')

if __name__ == "__main__":
    model_path = 'C:/Users/Anna Kima/Desktop/Chatbot/models/20240301-154513-massive-request.tar.gz'
    domain_path = 'C:/Users/Anna Kima/Desktop/Chatbot/domain.yml'


    # Run asynchronous operations using asyncio.run()
    async def main():
        agent = await load_nlu_model(model_path)
        domain_responses = load_domain(domain_path)
        await generate_response(agent, domain_responses)


    import asyncio

    asyncio.run(main())
