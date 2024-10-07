import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_assignment(topic):
    prompt = f"Generate 3 descriptive UPSC Mains-style questions on the topic '{topic}':"
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text

# Usage
if _name_ == "_main_":
    topic = "Indian Economy"
    assignment = generate_assignment(topic)
    print(assignment)