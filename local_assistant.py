from gpt4all import GPT4All

# Set the path to your downloaded model file
model_directory = "C:\\Users\\sammy\\gpt4all\\gpt4all-lora-quantized.bin"  # Adjust this path if needed
model = GPT4All(model_path)
model.open()  # Load the model into memory

print("Local GPT4All Assistant is ready. Type 'exit' to quit.")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break
    response = model.prompt(prompt)
    print("LYNX:", response)
