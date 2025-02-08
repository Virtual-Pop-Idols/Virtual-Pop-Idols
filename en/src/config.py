# config.py - Configuration settings for the Virtual Pop Idols AI project

import json

def load_config():
    """Loads configuration settings from a JSON file."""
    config_file = "../shared/config/default_settings.json"
    
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
            print("Configuration loaded successfully.")
            return config
    except FileNotFoundError:
        print("Error: Configuration file not found.")
        return {
            "idol_name": "Default Idol",
            "initial_skillset": {"performance": 5, "stage_presence": 5}
        }

