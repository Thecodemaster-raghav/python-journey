from dotenv import load_dotenv
import anthropic

# loading the .env using load_dotenv()
load_files = load_dotenv()
# creating a client to call an llm; here i am using anthropic
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=600,
    messages=[
        {
            "role":"user",
            "content":"give me 2 most followed football(soccer players) in the world on instagram.",
        }
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)
        
print({"input_tokens":message.usage.input_tokens})
print({"output_tokens":message.usage.output_tokens})
if message.stop_reason == "max_tokens":
    print("Reply cut out; max token reached")