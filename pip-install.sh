#!/bin/bash
# Usage: ./pip-install.sh <package-name>

if [ -z "$1" ]; then
  echo "❌ Please provide a package name"
  exit 1
fi

# Install the package
pip install "$1"

# Freeze the environment into requirements.txt
pip freeze > requirements.txt

echo "✅ Installed $1 and updated requirements.txt"
