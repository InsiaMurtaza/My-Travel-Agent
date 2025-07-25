import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool, set_tracing_disabled
from openai import AsyncOpenAI

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.0-flash"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

set_tracing_disabled(disabled=True)

client = AsyncOpenAI(api_key=gemini_api_key, base_url= BASE_URL)

@function_tool
def get_flights()->str:
    return f"""There are many options in airlines like Emirates, PIA, Qatar Airways, flydubai 
        You may visit Emirates official website
        http://www.emirates.com
        For PIA  you may visit
        http://www.piac.com.pk
        For Qatar Airways you may visit
        http://www.qatarairways.com
        For Flydubai you may visit
        http://www.flydubai.com"""
    

@function_tool
def travel_info_generator(mood:str)->str:
    if "beach" or "relax" in mood:
        return f"""1. Maldives – Ultimate Luxury & Seclusion
Best For: Overwater bungalows, snorkeling, honeymoon vibes
Why: White-sand beaches, turquoise waters, and private island resorts.

🇮🇩 2. Bali, Indonesia – Culture & Surf
Best For: Yoga retreats, surfing, temples, nightlife
Why: Uluwatu and Seminyak beaches offer both relaxation and vibrant energy.

🇹🇭 3. Thailand – Tropical Variety
Best Beaches: Phuket, Krabi (Railay Beach), Koh Phi Phi, Koh Samui
Why: Affordable luxury, amazing food, island hopping, dramatic limestone cliffs.

🇬🇷 4. Greece – Scenic and Historic Coasts
Best Beaches: Mykonos (Paradise Beach), Santorini (Red Beach), Crete (Elafonissi)
Why: Beach and history in one trip, with Mediterranean charm and great food.

🇲🇽 5. Mexico – Caribbean & Pacific Gems
Best Beaches: Tulum, Cancun, Playa del Carmen, Cabo San Lucas
Why: Vibrant culture, Mayan ruins nearby, cenotes, and resort life.

🇮🇹 6. Amalfi Coast, Italy – Scenic Cliffs & Charm
Best For: Cliffside views, coastal villages (like Positano), historic ruins
Why: Unique mix of beach, culture, and luxury.

🇧🇷 7. Brazil – Long Coasts & Tropical Heat
Best Beaches: Copacabana, Ipanema (Rio), Fernando de Noronha
Why: Lively beach culture, tropical islands, samba energy.

🇺🇸 8. Hawaii, USA – Diverse Landscapes
Best Islands: Maui, Oahu (Waikiki), Kauai (Hanalei Bay), Big Island
Why: Volcanoes, waterfalls, black-sand beaches, surfing.

🇸🇨 9. Seychelles – Dreamlike Isolation
Best For: Honeymooners, nature lovers
Why: Unique boulder-lined beaches (like Anse Source d'Argent), marine life, and privacy.

🇹🇿 10. Zanzibar, Tanzania – Exotic Culture & Warm Waters
Best For: African spice island experience
Why: Historic Stone Town meets turquoise beaches and coral reefs."""#"You may visit Maldives as there are many resorts alongside beach and cool environment where you can relax. It's easy to get visa of Maldives and you will have an option of many airlines which fly to Maldives from Pakistan."
    elif "hiking" or "adventurous" or "adventure" in mood:
        return f"""1. Nepal – Himalayas & Everest Base Camp
Top Hikes: Everest Base Camp Trek, Annapurna Circuit, Langtang Valley
Why: World-class mountain views, authentic mountain villages, Buddhist culture.
Difficulty: Moderate to Hard

🇺🇸 2. USA – National Parks Galore
Top Hikes:
Yosemite (California) – Half Dome, Mist Trail
Grand Canyon (Arizona) – Rim-to-Rim Trail
Zion (Utah) – Angels Landing
Why: Vast landscapes, well-marked trails, diversity from desert to alpine.
Difficulty: Easy to Extreme

🇨🇭 3. Switzerland – Alpine Majesty
Top Hikes: The Eiger Trail, Zermatt to the Matterhorn, Lauterbrunnen Valley
Why: Stunning peaks, lakes, charming alpine villages, efficient transport.
Difficulty: Moderate

🇳🇿 4. New Zealand – Lord of the Rings Country
Top Hikes: Tongariro Alpine Crossing, Routeburn Track, Milford Track
Why: Epic volcanic landscapes, fjords, lush valleys, and crystal-clear lakes.
Difficulty: Moderate to Hard

🇨🇱 5. Patagonia (Chile & Argentina) – Wild Beauty
Top Hikes: Torres del Paine W Trek, Fitz Roy Trek
Why: Jagged peaks, glaciers, remote and raw wilderness.
Difficulty: Moderate to Hard

🇨🇦 6. Canada – Rockies & Wilderness
Top Hikes: Banff (Plain of Six Glaciers), Jasper (Sulphur Skyline), Lake Louise
Why: Glacier lakes, pine forests, wildlife, and crisp air.
Difficulty: Easy to Moderate

🇲🇦 7. Morocco – Atlas Mountains & Desert
Top Hike: Mount Toubkal (highest in North Africa)
Why: Berber villages, desert views, and high-altitude climbs.
Difficulty: Moderate to Hard

🇳🇴 8. Norway – Fjords & Clifftop Hikes
Top Hikes: Trolltunga, Preikestolen (Pulpit Rock), Romsdalseggen Ridge
Why: Iconic fjord views, waterfalls, and northern light possibilities.
Difficulty: Moderate

🇯🇵 9. Japan – Forests, Volcanoes & Pilgrimage Trails
Top Hikes: Mount Fuji, Kumano Kodo Trail, Japanese Alps
Why: Mix of spiritual and scenic, onsen (hot spring) culture, great food.
Difficulty: Moderate

🇵🇰 10. Pakistan – Untouched Mountain Majesty
Top Hikes: Fairy Meadows, Hunza Valley, Rakaposhi Base Camp, Passu Glacier
Why: Home to some of the tallest peaks in the world (K2), unique cultural blend, raw beauty.
Difficulty: Moderate to Hard"""
    elif "explore ancient history." in mood:
        return f""" 1. Egypt – Ancient Egyptian Civilization
Must-See: Pyramids of Giza, Valley of the Kings, Luxor Temple, Karnak Temple
Why: Home to pharaohs, pyramids, mummies, and hieroglyphs, Egypt offers one of the richest ancient histories on Earth.

🏛️ 2. Greece – Ancient Greek Civilization
Must-See: Acropolis of Athens, Delphi, Olympia, Knossos (Crete)
Why: Birthplace of democracy, philosophy, and the Olympics; ruins and museums reveal a vivid past.

🏺 3. Italy – Roman Empire
Must-See: Colosseum, Roman Forum, Pompeii, Herculaneum, Ostia Antica
Why: Walk the streets of ancient Rome and see preserved cities buried in volcanic ash.

🏯 4. China – Ancient Chinese Dynasties
Must-See: The Great Wall, Terracotta Army in Xi’an, Forbidden City
Why: Explore over 4,000 years of dynastic rule, inventions, and ancient philosophy.

🕌 5. Iraq (Mesopotamia) – Cradle of Civilization
Must-See: Ancient Babylon, Ur, Nineveh (some ruins in modern Iraq)
Why: Home of Sumerians, Assyrians, and Babylonians — birthplace of writing, cities, and early law.

🛕 6. India – Indus Valley Civilization and Early Empires
Must-See: Mohenjo-Daro, Harappa, Hampi, Ellora & Ajanta Caves
Why: One of the oldest continuous civilizations, rich with ancient architecture, science, and religion.

🏯 7. Peru – Inca Civilization
Must-See: Machu Picchu, Cusco, Sacsayhuamán
Why: Mysterious mountaintop cities and precision stonework in the Andes.

🏜️ 8. Jordan – Nabataean and Biblical History
Must-See: Petra, Jerash, Dead Sea Scrolls sites
Why: Famous for rock-cut architecture and ancient trade routes.

🛕 9. Cambodia – Khmer Empire
Must-See: Angkor Wat, Angkor Thom, Bayon Temple
Why: Stunning temple complexes showcasing ancient Hindu and Buddhist influence.

🧱 10. Turkey – Byzantium, Hittites, and More
Must-See: Ephesus, Troy, Göbekli Tepe, Cappadocia
Why: A crossroads of empires, from Neolithic to Byzantine."""

@function_tool
def get_visa(destination:str)->str:
    if "Maldives" in destination:
        return f"""🇲🇻 Maldives
Visa: Free visa on arrival (30 days)
Requirements: Return ticket, hotel booking, funds
✅ Easiest or Visa-Free / e-Visa / Visa on Arrival"""
    elif "Thailand" in destination:
        return f"""🇹🇭 Thailand
Visa: e-Visa available (pre-arranged online)
Processing time: 7–10 days typically
✅ Easiest or Visa-Free / e-Visa / Visa on Arrival"""
    elif "Turkey" in destination:
        return f"""🇹🇷 Turkey
Visa: e-Visa available if you have a valid US/UK/Schengen visa
Otherwise, you must apply via embassy
Processing time: 2–4 weeks
✅ Easiest or Visa-Free / e-Visa / Visa on Arrival"""
    elif "Morocco" in destination:
        return f"""🇲🇦 Morocco
Visa: Apply at embassy
Processing: Moderate effort, but usually granted if documentation is strong
✅ Easiest or Visa-Free / e-Visa / Visa on Arrival"""
    elif "Indonesia" in destination:
        return f"""🇮🇩 Indonesia
Visa: Apply through Indonesian embassy
Approval: Moderate success rate with full documents
🟡 Moderately Difficult (Embassy Visa Required, but Common for Tourists)"""
    elif "Tanzania" in destination:
        return f"""🇹🇿 Tanzania
Visa: e-Visa available
Ease: Quite tourist-friendly
🟡 Moderately Difficult (Embassy Visa Required, but Common for Tourists)"""
    elif "China" in destination:
        return f"""🇨🇳 China
Visa: Requires strong documents + interview
Processing: Can take 2–3 weeks, but possible with good reasons (tourism, business)
🟡 Moderately Difficult (Embassy Visa Required, but Common for Tourists)"""
    elif "Greece" in destination:
        return f"""🇬🇷 Greece (Schengen Visa)
Visa: Schengen Visa required
Difficulty: Moderate to hard depending on financial docs, travel history
Embassy: Usually through Gerrys/FedEx Visa Centres
🔴 Harder to Get Visa (Strict Scrutiny or Low Approval Rates)"""
    elif "Italy" in destination:
        return f"""🇮🇹 Italy (Schengen Visa)
Same as above – needs strong financials, previous travel history 
🔴 Harder to Get Visa (Strict Scrutiny or Low Approval Rates)"""
    elif "Japan" in destination:
        return f"""🇯🇵 Japan
Visa: Embassy visa required, thorough process
Requirements: Bank statements, itinerary, sponsor (if any)
🔴 Harder to Get Visa (Strict Scrutiny or Low Approval Rates)"""
    elif "Norway" in destination:
        return f"""🇳🇴 Norway (Schengen Visa)
Same as Greece/Italy
🔴 Harder to Get Visa (Strict Scrutiny or Low Approval Rates)"""
    elif "Switzerland" in destination:
        return f"""🇨🇭 Switzerland (Schengen Visa)
Difficulty: Requires solid documentation, accommodation, insurance
🔴 Harder to Get Visa (Strict Scrutiny or Low Approval Rates)"""
    elif "Argentina" in destination:
        return f"""🇦🇷 Argentina
Visa: Embassy visa required
Difficulty: Medium difficulty, less tourist inflow from Pakistan so higher scrutiny
🔴 Harder to Get Visa (Strict Scrutiny or Low Approval Rates)"""    
    elif "USA" or "United States" or "US" in destination:
        return f"""🇺🇸 United States
Visa: B1/B2 Visitor Visa via Embassy
Difficulty: High – interviews, long processing, high rejection rate for new travelers without strong financials/travel history
🚫 Most Difficult to Get Visa"""
    elif "Brazil" in destination:
        return f"""🇧🇷 Brazil
Visa: Embassy visa required
Difficulty: Often high rejection rate unless solid reason (e.g. business)
🚫 Most Difficult to Get Visa"""
    elif "New Zealand" in destination:
        return f"""🇳🇿 New Zealand
Visa: Embassy visa required or via online
Difficulty: Moderate to hard (especially if no travel history or strong job ties)
🚫 Most Difficult to Get Visa"""
    elif "Canada" in destination:
        return f"""🇨🇦 Canada
Visa: Visit Visa via online + biometrics
Difficulty: High — you need strong reasons, ties to Pakistan, income proof    
🚫 Most Difficult to Get Visa"""
    
@function_tool
def suggest_hotels(destination:str)->str:
    if "Maldives" in destination:
        return f"""🌴 1. Maldives
Top Resorts: Soneva Fushi, Baros Maldives, OZEN Life Maadhoo
Food: Fresh seafood, Maldivian curry, coconut-based dishes
Must-Try: Garudhiya (fragrant fish soup), Hedhikaa (snacks)"""
    elif "Indonesia" in destination:
        return f"""🌾 2. Indonesia (Bali)
Top Resorts: The Mulia (Nusa Dua), Hanging Gardens of Bali (Ubud), AYANA Resort
Food: Nasi Goreng, Satay, Babi Guling (roast pork)
Must-Try: Local warung meals, Balinese sambal sauces"""
    elif "Thailand" in destination:
        return f"""🇹🇭 3. Thailand
Top Hotels: Anantara (Chiang Mai, Phuket), The Slate (Phuket), Banyan Tree
Food: Pad Thai, Green Curry, Tom Yum soup
Must-Try: Mango sticky rice, Street food in Bangkok"""
    elif "Greece" in destination:
        return f"""🇬🇷 4. Greece
Top Resorts: Katikies (Santorini), Canaves Oia, Blue Palace (Crete)
Food: Souvlaki, Moussaka, Greek salad, Feta cheese
Must-Try: Fresh seafood by the Aegean, Baklava"""
    elif "USA" or "United States" or "US" in destination:
        return f"""🇺🇸 5. USA
Top Hotels: Waldorf Astoria (New York), Four Seasons (Hawaii), Amangiri (Utah)
Food: Regional variety – Southern BBQ, New York pizza, California fusion
Must-Try: Food trucks, diners, Michelin-starred restaurants (if budget allows)"""
    elif "Italy" in destination:
        return f"""🇮🇹 6. Italy
Top Hotels: Belmond Hotel Caruso (Amalfi), Hotel de Russie (Rome), Gritti Palace (Venice)
Food: Pasta, Pizza, Gelato, Risotto
Must-Try: Neapolitan pizza in Naples, tiramisu"""
    elif "Brazil" in destination:
        return f"""🇧🇷 7. Brazil
Top Hotels: Belmond Copacabana Palace, Fasano (Rio), UXUA (Bahia)
Food: Feijoada, Pão de queijo, Grilled meats (Churrasco)
Must-Try: Açai bowls, Caipirinha (drink)"""
    elif "Tanzania" in destination:
        return f"""🌍 8. Tanzania
Top Resorts: Zuri Zanzibar, The Residence Zanzibar, Singita (safari lodges)
Food: Coconut rice, Zanzibari biryani, fresh seafood
Must-Try: Urojo soup, Chapati, Pulau"""
    elif "Switzerland" in destination:
        return f"""🇨🇭 9. Switzerland
Top Hotels: Badrutt’s Palace (St. Moritz), The Dolder Grand (Zurich), Hotel Villa Honegg
Food: Cheese fondue, Rösti, Swiss chocolate
Must-Try: Alpine restaurants, lakeside dining in Lucerne"""
    elif "New Zealand" in destination:
        return f"""🇳🇿 10. New Zealand
Top Lodges: Huka Lodge, Matakauri Lodge, Eichardt’s Private Hotel
Food: Lamb, seafood, Pavlova, Maori hangi meals
Must-Try: Green-lipped mussels"""
    elif "Argentina" in destination:
        return f"""🇦🇷 11. Argentina
Top Hotels: Alvear Palace (Buenos Aires), EOLO Patagonia, Palacio Duhau
Food: Asado (BBQ), Empanadas, Dulce de leche
Must-Try: Mate tea, Patagonian lamb"""
    elif "Canada" in destination:
        return f"""🇨🇦 12. Canada
Top Hotels: Fairmont Banff Springs, Rosewood (Vancouver), Ritz-Carlton (Toronto)
Food: Poutine, Maple syrup, Salmon, French-Canadian cuisine
Must-Try: Nanaimo bars, Butter tarts, fresh lobster (East coast)"""
    elif "Morocco" in destination:
        return f"""🇲🇦 13. Morocco
Top Riads/Hotels: La Mamounia (Marrakech), Riad Fes, Kasbah Tamadot
Food: Tagine, Couscous, Pastilla
Must-Try: Mint tea, Harira soup, street food in Jemaa el-Fnaa"""
    elif "Norway" in destination:
        return f"""🇳🇴 14. Norway
Top Hotels: The Thief (Oslo), Hotel Union Øye, Juvet Landscape Hotel
Food: Salmon, Reindeer meat, Brown cheese
Must-Try: Arctic cod, Cloudberries, seafood buffets"""
    elif "Japan" in destination:
        return f"""🇯🇵 15. Japan
Top Ryokans/Hotels: Hoshinoya Kyoto, Aman Tokyo, Park Hyatt Tokyo
Food: Sushi, Ramen, Tempura, Kaiseki meals
Must-Try: Wagyu beef, Matcha desserts, Izakaya dining"""
    elif "China" in destination:
        return f"""🇨🇳 16. China
Top Hotels: Peninsula (Beijing), Banyan Tree (Lijiang), The PuLi (Shanghai)
Food: Dim Sum, Peking Duck, Hot Pot, Regional cuisines
Must-Try: Sichuan street food, Beijing noodles, Bubble tea"""
    elif "Turkey" in destination:
        return f"""🇹🇷 17. Turkey
Top Hotels: Ciragan Palace Kempinski, Museum Hotel (Cappadocia), Six Senses Kaplankaya
Food: Kebabs, Baklava, Meze platters, Turkish breakfast
Must-Try: Simit, Iskender kebab, Turkish tea & coffee"""
    

exploreagent = Agent(name="ExploreAgent", 
                     instructions= "You are an efficient expore agent who understands the user's destination and recommends best hotels,resorts and food at best prices. You may use your tools to do so.",
                     tools= [suggest_hotels],
                     model=OpenAIChatCompletionsModel(model=MODEL,openai_client=client))


bookingagent = Agent(name="BookingAgent", 
                     instructions="You are an efficient booking agent who knows the user's destination and guide him/her accordingly with the help of your tools. Once the user chooses its airline and flight, you should handoff to the Explore Agent",
                     tools=[get_flights,get_visa],
                     handoffs=[exploreagent],
                     model=OpenAIChatCompletionsModel(model=MODEL,openai_client=client))

destinationagent = Agent(name="DestinationAgent", 
                        instructions= "You are an efficient destination agent who understands the user's mood to suggest suitable destinations using your tools 'travel_info_generator'. Once user confirms the destination you should handoff the destination to the BookingAgent.",
                        tools= [travel_info_generator],
                        handoffs=[bookingagent],
                        model=OpenAIChatCompletionsModel(model=MODEL,openai_client=client))



async def main():
    print("Welcome to the Travel Agent🖐")
    print("What is your mood? Do you want to travel to beach, for hiking or exploring some historical place?How do you feel?(e.g. adventurous, relaxed)")
    current_agent = destinationagent
    messages = []
    while True:
        try:
            user_input = input("\nYou:")
            if user_input.lower() in ["Thankyou for your guidance","No more questions","Goodbye"]:
                print("AI Agent: Goodbye🖐 Happy Journey!")
                break
            result = await Runner.run(current_agent,user_input)
            print(f"AI Agent: {result.final_output}")
            messages.append({"role":"user", "content": user_input})
            messages.append({"role":"assistant","content":result.final_output})
        except Exception as e:
            print(f"An error occurred: {e}")
            print("AI Agent: I apologize, an error occurred. Please try again or rephrase your query.")

if __name__== "__main__":
    asyncio.run(main())








