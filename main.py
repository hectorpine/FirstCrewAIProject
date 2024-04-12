import os
from decouple import config
from crewai import Crew, Process
from textwrap import dedent

from agents import CustomAgents
from tasks import CustomTasks

# Set up environment variables
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"

class AutomationCrew:
    def __init__(self, business_info):
        self.business_info = business_info
        self.agents = CustomAgents()
        self.tasks = CustomTasks()

    def run(self):
        # Initialize agents
        business_analyst = self.agents.business_analyst_agent()
        solutions_architect = self.agents.solutions_architect_agent()

        # Initialize tasks with respective agents and the user-provided business information
        process_identification_task = self.tasks.process_identification_task(business_analyst, self.business_info)
        automation_design_task = self.tasks.automation_design_task(solutions_architect, "identified processes from task 1")

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[business_analyst, solutions_architect],
            tasks=[process_identification_task, automation_design_task],
            verbose=True,
        )

        # Execute the crew to carry out the business automation project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Business Automation Crew Setup")
    print("------------------------------------------------")
    business_info = input("Hello, please tell me about your business and the problems you would like to solve, or if you have questions about CrewAI ask away as well: ").strip()
    
    automation_crew = AutomationCrew(business_info)
    result = automation_crew.run()
    
    with open('automation_crew_output.txt', 'w') as file:
        file.write("## Business Automation Results:\n")
        file.write("########################\n\n")
        file.write(result)
        file.write("\n########################\n")
    
    print("\n\n########################")
    print("## Here are the results of your business automation project:")
    print("########################\n")
    print(result)
