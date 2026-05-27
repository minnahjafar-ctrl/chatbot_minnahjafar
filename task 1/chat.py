import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {
        "role": "system",
        "content": " Be romantic."
    }
]

while True:

    user_input = input("You: ")

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=1.2,
        max_tokens=50
    )

    assistant_reply = response.choices[0].message.content

    print("AI:", assistant_reply)

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )