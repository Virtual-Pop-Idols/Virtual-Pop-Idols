# main.py - Entry point for the Virtual Pop Idols AI system

from ai_agent import VirtualPopIdolAgent
from config import load_config

def main():
    # Load the configuration settings
    config = load_config()

    # Initialize the AI agent
    idol_agent = VirtualPopIdolAgent(
        name=config["idol_name"],
        initial_skillset=config["initial_skillset"]
    )

    # Start the virtual performance
    print(f"Starting performance for {idol_agent.name}...")
    idol_agent.perform()

    # Monitor audience feedback
    print("Monitoring audience reactions...")
    idol_agent.process_feedback()

    # End the performance
    print(f"Performance by {idol_agent.name} completed successfully.")

if __name__ == "__main__":
    main()
