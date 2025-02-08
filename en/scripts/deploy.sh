#!/bin/bash

# deploy.sh - Deployment script for Virtual Pop Idols AI project

echo "Starting deployment of the Virtual Pop Idols AI project..."

# Navigate to the project directory
cd "$(dirname "$0")/../src"

# Install necessary dependencies
echo "Installing dependencies..."
pip install -r ../requirements.txt

# Run initial setup
echo "Running initial setup..."
python main.py

echo "Deployment completed successfully!"
