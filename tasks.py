from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.

class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, starting_date, departure_date, interests):
        return Task(
            description=dedent(
                f"""

            **Task**: Develop a Travel Itinerary plan based on the date range

            **Description**: Expand the city guide into a full travel itinerary plan based
            on the arrival date and departure date with detailed per-day plans,
            including weather forecasts, places to eat, packing suggestions, and 
            a budget breakdown. You MUST suggest actual places to visit, actual hotels
            to stay, and actual restaurants to go to. This itinerary should cover all aspects of the trip,
            from arrival to departure, integrating the city guide information with practical 
            travel logistics.

            **Parameters**:
            City:{city}
            Arrival Date: {starting_date}
            Departure Date: {departure_date}
            Traveler Interests: {interests}

            **Note**: {self.__tip_section()}
            
            {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output = dedent("Create a structured format plan ")
        )

    def identify_city(self, agent, origin, cities, interests, starting_date, departure_date):
        return Task(
            description=dedent(
                f"""
            **Task**: Identify the Best City for the Trip
            **Description**: Analyze and select the best city for the trip based on 
            specific criteria such as weather patterns, seasonal events, and travel costs.
            This task involves comparing multiple cities, considering factors like current weather
            conditions, upcoming cultural or seasonal events, and overall travel expenses.
            Your final answer must be a detailed report on the chosen city,
            including actual flight costs, weather forecast, and attractions.

            **Parameters**:
            Origin: {origin}
            Cities: {cities}
            Interests: {interests}
            Arrival Date: {starting_date}
            Departure Date: {departure_date}

                                    
            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output = dedent("""
                                     Detailed report on the chosen city, including actual flight costs, 
                                     weather forecast, and attractions
        """)
        )
    
    def gather_city_info(self, agent, city, starting_date, departure_date, interests):
        return Task(
            description = dedent(
                f"""
                **Tasks**: Gather In-depth City Guide Information
                **Description**: Compile an in-depth guide for the selected city, gathering information about
                key attractions, local customs, special events, and daily activity recommendations.
                This guide should provide a thorough overview of what the city has to offer, including
                hidden gems, cultural hotspots, must-visit landmarks, weather forecasts,
                and high-level costs.

                **Parameters**:
                Cities : {city}
                Interests: {interests}
                Arrival Date: {starting_date}
                Departure Date: {departure_date}

                **Note**: {self.__tip_section()}
                """
            ),
            agent = agent,
            expected_output = dedent("""
                                    Informative rundown of the city's offerings, including hidden gems, 
                                     cultural attractions, famous landmarks, weather forecasts, 
                                     and with the breakdown of each cost.
                                     """)
        )
