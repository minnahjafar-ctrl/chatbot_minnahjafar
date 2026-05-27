from groq import Groq

client = Groq(api_key="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")

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