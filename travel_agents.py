import os
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
from function_tools import travel_info_generator, get_visa, get_flights, suggest_hotels

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.0-flash"
base_url = os.getenv("GEMINI_BASE_URL")

client = AsyncOpenAI(api_key=gemini_api_key, base_url= base_url)

exploreagent = Agent(name="ExploreAgent", 
                     instructions= "You are an efficient expore agent who knows the user's destination and you must use your tool *suggest_hotels* to recommend best hotels,resorts and food at best prices.",
                     tools= [suggest_hotels],
                     model=OpenAIChatCompletionsModel(model=MODEL,openai_client=client))


bookingagent = Agent(name="BookingAgent", 
                     instructions="You are an efficient booking agent who knows the user's destination and you must guide him/her accordingly with the help of your tools *get_visa* and *get_flights*. Then you should handoff to the ExploreAgent",
                     tools=[get_flights,get_visa],
                     handoffs=[exploreagent],
                     model=OpenAIChatCompletionsModel(model=MODEL,openai_client=client))

destinationagent = Agent(name="DestinationAgent", 
                        instructions= "You are an efficient destination agent. You must suggest suitable destinations using your tool *travel_info_generator* according to the user's requirement. Then you should handoff the destination to the BookingAgent.",
                        tools= [travel_info_generator],
                        handoffs=[bookingagent,exploreagent],
                        model=OpenAIChatCompletionsModel(model=MODEL,openai_client=client))

travel_agent = Agent(name="TravelAgent", instructions= "You are an efficeint travel agent who handoffs to the DestinationAgent if the user asks to suggest any place/destination to go to." 
"If the user asks for visa, tickets or flight details, you should handoff to the BookingAgent for visa and flight details."
"If the user asks to suggest hotels in a particular destination/place you should handoff to the ExploreAgent.",
model= OpenAIChatCompletionsModel(model=MODEL, openai_client= client),
handoffs=[destinationagent,bookingagent,exploreagent]
                     )

