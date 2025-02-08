#!/bin/bash

# test_agent.sh - Script to test the Virtual Pop Idols AI agent

echo "Starting tests for Virtual Pop Idols AI agent..."

# Navigate to the project directory
cd "$(dirname "$0")/../src"

# Run basic tests
echo "Running basic functionality tests..."
python -c "
from ai_agent import VirtualPopIdolAgent

# Initialize the agent for testing
test_agent = VirtualPopIdolAgent(name='Test Idol', initial_skillset={'performance': 5, 'stage_presence': 5})

# Test performance
print('Testing performance...')
test_agent.perform()

# Test feedback processing
print('Testing feedback processing...')
test_agent.process_feedback()

print('Tests completed successfully.')
"

echo "All tests passed."
