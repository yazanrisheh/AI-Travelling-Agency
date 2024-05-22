from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI

from tools.search_tool import search_tool
from tools.calculator_tool import CalculatorTool

# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

# Add more detials in backstory and specify the output I am expecting. backstory = resume/credentials and be as detailed as possible
    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent("""Expert in travel planning and logistics. I have decades of experience making travel
                             itineraries. I know the cheapest flights, best airlines, and any requirement needed to
                             travel to the desired location
                             """),
            goal=dedent("""Create a detailed itinerary plan with detailed per plans, include budget,
                        packing suggestions, and cultural etiquette.
                        """),
            tools=[search_tool,
                   CalculatorTool.calculate
                   ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent("""Expert at analyzing travel data to pick ideal destinations based on 
                             everything the travellers input including price and the date which you could identify for any
                             special events or occasions"""),
            goal=dedent("""Select the best cities based on weather,
                        season, prices, and travel interests"""),
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    #This is local tour guide which is generic cuz city input can be diff
    def local_tour_guide(self):
        return Agent(
            role = "Local Tour Guide",
            backstory = dedent("""Knowledgeable local guide with extensive information
                               about the city, it's attractions and customs. Always provide
                               google maps link so that the traveller can know where exactly to go. Provides tips and tricks
                               for the selected city including things to not do to prevent any trouble that could fine, jail, or deport
                               you. Specify things that makes the travellers life easier for example,
                               an application to download for cheap taxis, or a place that provides food 
                               with affordable price etc...
                               """),
            goal = dedent("""Provide the BEST insights about the selected city including attractions and customs,
                          unique things, and things to not do to prevent any trouble that could fine, jail, or deport.
                          Always provide google map link to any location in this format:
                          Link: (google map link)
                          """),
            tools = [search_tool],
            allow_delegation = False,
            verbose = True,
            llm = self.OpenAIGPT35
        )
