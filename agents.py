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

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. I have decades of experience making travel
                             itineraries.
                             """),
            goal=dedent(f"""Create a 7-day itinerary plan with detailed per plans, include budget,
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
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best cities based on weather,
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
            backstory = dedent(f"""Knowledgeable local guide with extensive information
                               about the city, it's attractions and customs.
                               """),
            goal = dedent(f"""Provide the BEST insights about the selected city
                          """),
            tools = [search_tool],
            allow_delegation = False,
            verbose = True,
            llm = self.OpenAIGPT35
        )
