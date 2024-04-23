import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

import streamlit as st

load_dotenv()

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class TripCrew:
    def __init__(self, origin, cities, starting_date, departure_date, interests):
        self.origin = origin
        self.cities = cities
        self.starting_date = starting_date
        self.departure_date = departure_date
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.starting_date,
            self.departure_date,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.starting_date,
            self.departure_date,
            self.interests
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.starting_date,
            self.departure_date,
            self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent,
                    city_selection_expert,
                    local_tour_guide
                    ],
            tasks=[plan_itinerary,
                    identify_city,
                    gather_city_info
                    ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    st.title("RAAFYA International Travelling Agency ✈️")
    first_name = st.text_input(dedent("What is your first name? "))
    last_name = st.text_input(dedent("What is your last name? "))
    origin = st.text_input(dedent("""Where will you be travelling from? e.g. Abu Dhabi, UAE: """))
    cities = st.text_input(dedent("""What country are you interested in visiting? """))
    starting_date = st.text_input(dedent("What day would you like to go? e.g. March 15: "))
    departure_date = st.text_input(dedent("What day would you like to come back? e.g. March 18: "))
    interests = st.text_input(dedent("What are some of your high level interests and hobbies? e.g. Ice skating, Hiking, Yoga: "))
    trip_crew = TripCrew(origin, cities, starting_date, departure_date, interests)

    if st.button("Start Generation"):
        with st.spinner("Generating your plan..."):
            result = trip_crew.run()
            # Write the result to a text file
            with open(f"{first_name}_{last_name}'s plan.txt", "w", encoding='utf-8') as text_file:
                text_file.write(result)
            # Display a success message
            st.success("Plan generated successfully!")
            # Add a download button for the text file
            st.download_button(label="Download", data=result, file_name=f"{first_name}_{last_name}'s plan.txt", mime="text/plain")


# Without streamlit uncomment this and comment above

    # print("## Welcome to Raafya International Travelling Agency")
    # print("-------------------------------")
    # origin = input(dedent("""Where will you be travelling from? e.g. Abu Dhabi, UAE: """))
    # cities = input(dedent("""What country are you interested in visiting? """))
    # starting_date = input(dedent("What day would you like to go? e.g. March 15: "))
    # departure_date = input(dedent("What day would you like to come back? e.g. March 18: "))
    # interests = input(dedent("What are some of your high level interests and hobbies? e.g. Ice skating, Hiking, Yoga: "))
    # trip_crew = TripCrew(origin, cities, starting_date, departure_date, interests)
    # result = trip_crew.run()
    # print("\n\n########################")
    # print("## Here is you Trip Plan")
    # print("########################\n")
    # print(result)