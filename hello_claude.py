from dotenv import load_dotenv
import anthropic

load_dotenv()                    # loads ANTHROPIC_API_KEY from .env
client = anthropic.Anthropic()   # picks up the key automatically

message = client.messages.create(
    model="claude-haiku-5-5",    # cheapest model; good for practice
    max_tokens=300,
    system="You are a concise data science tutor.",
    messages=[
        {"role": "user", "content": "In two sentences, what is a window function in SQL?"}
    ],
)

print(message.content[0].text)
print(message.usage)             # input/output tokens = what you pay for