# ai_agent.py - Core logic for Virtual Pop Idols AI agent

class VirtualPopIdolAgent:
    def __init__(self, name, initial_skillset):
        self.name = name
        self.skillset = initial_skillset
        self.feedback_log = []

    def perform(self):
        """Simulates the AI idol’s performance."""
        print(f"{self.name} is performing a high-energy dance and song set!")
        # Simulated performance logic
        print(f"{self.name} switches between songs dynamically based on audience reactions.")

    def process_feedback(self):
        """Processes audience feedback to improve future performances."""
        # Simulating feedback collection
        feedback_data = ["positive", "neutral", "negative"]
        self.feedback_log.extend(feedback_data)
        print(f"Feedback collected: {feedback_data}")

        # Evaluate and update skillset
        self._update_skillset()

    def _update_skillset(self):
        """Updates the idol’s skillset based on feedback."""
        print("Analyzing feedback to improve future performances...")
        # For simplicity, assume positive feedback increases skill
        positive_feedback_count = self.feedback_log.count("positive")

        if positive_feedback_count > 0:
            print(f"Positive feedback received: {positive_feedback_count}. Enhancing skillset.")
            self.skillset["performance"] += positive_feedback_count
        else:
            print("No positive feedback detected. Maintaining current skillset.")

        print(f"Updated skillset for {self.name}: {self.skillset}")

