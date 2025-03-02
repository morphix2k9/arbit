#!/bin/bash

# Ensure script runs in project root
cd "$(dirname "$0")"

echo "🔍 Checking if Vercel CLI is installed..."
if ! command -v vercel &> /dev/null
then
    echo "❌ Vercel CLI not found. Installing..."
    npm install -g vercel@latest
else
    echo "✅ Vercel CLI is already installed."
fi

echo "🔍 Verifying Vercel version..."
npx vercel --version

echo "🚀 Pulling Vercel Project Settings..."
npx vercel pull --yes --environment=production --token $VERCEL_TOKEN

echo "🚀 Deploying to Vercel..."
npx vercel deploy --prod --token $VERCEL_TOKEN

echo "✅ Deployment Complete."
