from crewai import Task
from textwrap import dedent

class CustomTasks:
    def __init__(self):
        # This method initializes any necessary variables or configurations if needed
        pass

    def process_identification_task(self, agent, business_info):
        """Task for identifying business processes that can be automated, customized with business-specific info."""
        return Task(
            description=dedent("""\
                Analyze the provided business information to identify processes that can be automated. Focus particularly on tasks related to content creation, such as filming and editing, which are time-consuming and potentially automatable."""),
            agent=agent,
            expected_output=dedent("""\
                A detailed report identifying potential automation opportunities within the YouTube content creation workflow, including recommendations for using AI to streamline filming and editing processes.""")
        )

    def automation_design_task(self, agent, identified_processes):
        """Task for designing CrewAI configurations to automate the identified processes."""
        return Task(
            description=dedent("""\
                Design specific CrewAI setups that will automate the identified business processes. Ensure that these setups are intuitive for users with no prior AI knowledge, focusing on simplifying content production and editing."""),
            agent=agent,
            expected_output=dedent("""\
                Detailed CrewAI automation plans, including user-friendly tools and technologies for automating YouTube video production and post-production tasks.""")
        )
