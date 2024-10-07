import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate_answer(user_answer, toppers_answer):
    prompt = f"Evaluate the following user answer in comparison with the topper's answer. Provide feedback:\n\nTopper's Answer:\n{toppers_answer}\n\nUser's Answer:\n{user_answer}"
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text

# Usage
if _name_ == "_main_":
    user_answer = "This is a brief answer with some negative tone."
    toppers_answer = "The government must ensure fiscal discipline to maintain economic growth..."
    feedback = evaluate_answer(user_answer, toppers_answer)
    print(feedback)