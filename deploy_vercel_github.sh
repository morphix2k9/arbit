#!/bin/bash

echo "🚀 Starting Deployment Script for Vercel & GitHub Actions..."

# Navigate to the project directory (Change this if needed)
cd "$(dirname "$0")"

# Ensure .github/workflows directory exists
if [ ! -d ".github/workflows" ]; then
    echo "📁 Creating .github/workflows directory..."
    mkdir -p .github/workflows
fi

# Ensure vercel_deploy.yml exists and create it if missing
if [ ! -f ".github/workflows/vercel_deploy.yml" ]; then
    echo "⚠️ vercel_deploy.yml missing. Creating default deployment file..."
    cat <<EOT > .github/workflows/vercel_deploy.yml
name: Auto-Deploy to Vercel

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set Up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install Vercel CLI
        run: npm install -g vercel && export PATH="\$HOME/.npm-global/bin:\$PATH"

      - name: Pull Vercel Project Settings
        run: vercel pull --yes --environment=production --token \${{ secrets.VERCEL_TOKEN }}

      - name: Deploy to Vercel
        run: vercel deploy --prod --token \${{ secrets.VERCEL_TOKEN }}
EOT
    echo "✅ Created vercel_deploy.yml"
else
    echo "✅ vercel_deploy.yml exists."
fi

# Ensure sync.yml exists and create it if missing
if [ ! -f ".github/workflows/sync.yml" ]; then
    echo "⚠️ sync.yml missing. Creating default sync file..."
    cat <<EOT > .github/workflows/sync.yml
name: Auto-Sync Local Changes to GitHub

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set Up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Deploy to Vercel
        run: vercel deploy --prod
EOT
    echo "✅ Created sync.yml"
else
    echo "✅ sync.yml exists."
fi

# Commit and Push Changes to GitHub
echo "🔄 Syncing changes with GitHub..."
git add .github/workflows/vercel_deploy.yml .github/workflows/sync.yml
git commit -m "Ensured vercel_deploy.yml and sync.yml exist and updated."
git push origin main

# Verify Vercel CLI Installation
echo "🔍 Checking Vercel CLI installation..."
if ! command -v vercel &> /dev/null
then
    echo "⚠️ Vercel CLI not found. Installing now..."
    npm install -g vercel
else
    echo "✅ Vercel CLI is installed."
fi

# Deploy to Vercel
echo "🚀 Deploying to Vercel..."
vercel deploy --prod

echo "✅ Deployment Complete!"

