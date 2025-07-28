import asyncio
from dotenv import load_dotenv
from agents import Runner, set_tracing_disabled
from travel_agents import travel_agent

load_dotenv()

set_tracing_disabled(disabled=True)

async def main():
    print("Welcome to the Travel Agent🖐")
    # print("Do you have a travel plan?")
    current_agent = travel_agent
    messages = []
    while True:
        try:
            user_input = input("\nYou:")
            if user_input.lower() == "goodbye" or "thankyou":
              print("AI Agent: Goodbye🖐 Happy Journey!")
              break
            else:
              result = await Runner.run(current_agent,input= user_input)
              print(f"AI Agent: {result.final_output}")
              messages.append({"role":"user", "content": user_input})
              messages.append({"role":"assistant","content":result.final_output})
        except Exception as e:
            print(f"An error occurred: {e}")
            print("AI Agent: I apologize, an error occurred. Please try again or rephrase your query.")

if __name__== "__main__":
    asyncio.run(main())








