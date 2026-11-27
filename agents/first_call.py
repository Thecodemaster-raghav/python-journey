from dotenv import load_dotenv
import anthropic

# loading the .env using load_dotenv()
load_files = load_dotenv()
# creating a client to call an llm; here i am using anthropic
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=600,
    # adding the system prompt for consitency and first security layer
    system= "You are a research assistant,. Always help with exactly 2 items, " \
    "Format: Title | Authors | Year | one-sentence summary. With links.",
    messages=[
        {
            "role":"user",
            "content":"give 2 best ai research papers to read",
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