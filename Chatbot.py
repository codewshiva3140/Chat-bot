import google.generativeai as genai

# Step 1: Connect to Gemini using your API key
genai.configure(api_key="KEY HERE")

# Step 2: Load the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Step 3: Start a chat session with memory
chat = model.start_chat(history=[])

print("Jarvis is ready! Type 'bye' to exit.")
print("-" * 40)

# Step 4: Keep talking in a loop
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "bye":
        print("Jarvis: Goodbye! Get back to coding soon 🫡")
        break
    
    response = chat.send_message(user_input)
    print(f"Jarvis: {response.text}")