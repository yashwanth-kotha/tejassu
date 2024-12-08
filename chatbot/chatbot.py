import openai
import os

def main():
    
    openai.api_key = os.getenv("openai.api_key")

    
    print("Welcome to the terminal chatbot! Type 'exit' to end the conversation.")

    while True:
        # Get user input
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Use OpenAI API to generate a response
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,
                temperature=0.7
            )

            # Extract response text and print it
            bot_response = response['choices'][0]['message']['content'].strip()
            print(f"Bot: {bot_response}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
