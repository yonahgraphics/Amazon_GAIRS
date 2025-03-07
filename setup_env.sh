#!/bin/bash

# Simple script to create a Python 3.11 virtual environment and install requirements

# Set virtual environment name
VENV_NAME="venv-py311"

# Create virtual environment with Python 3.11
echo "Creating Python 3.11 virtual environment: $VENV_NAME"
python3.11 -m venv $VENV_NAME

# Activate virtual environment
echo "Activating virtual environment"
source $VENV_NAME/bin/activate

# Check if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing packages from requirements.txt"
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "No requirements.txt found. Exiting."
    deactivate
    exit 1
fi

echo ""
echo "Virtual environment setup complete!"