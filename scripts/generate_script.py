import os
import random
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TOPICS = [
    "Motivation to hustle",
    "Financial independence",
    "Wealth mindset",
    "Never give up attitude",
    "Entrepreneur success"
]

def generate_script():
    topic = random.choice(TOPICS)

    prompt = f"""
    Write a 25-35 second YouTube Short script.
    Theme: {topic}.
    Style: motivational, finance, emotional push, bold claims allowed.
    Audience: 18-40 future millionaires.
    End with a cliffhanger or action call.
    No hashtags.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    script_text = response.choices[0].message.content.strip()

    with open("output/script.txt", "w", encoding="utf-8") as f:
        f.write(script_text)

    print("Generated Script:\n", script_text)
    return script_text


if __name__ == "__main__":
    generate_script()
