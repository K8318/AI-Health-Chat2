#!/bin/bash
# ══════════════════════════════════════════════
#  MediBot — Django Health Chatbot Setup Script
# ══════════════════════════════════════════════

set -e  # exit on error

echo ""
echo "╔═══════════════════════════════════════════════╗"
echo "║  🏥  MediBot — Django AI Health Chatbot       ║"
echo "║      Setup & Run Script                        ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""

# Check Python
python3 --version || { echo "❌ Python 3 not found. Install it first."; exit 1; }

# Install dependencies
echo "📦 Installing dependencies..."
pip install django anthropic pillow

echo ""
echo "🗄️  Setting up database..."
python manage.py makemigrations core
python manage.py migrate

echo ""
echo "🌱 Seeding sample data..."
python manage.py seed_data

echo ""
echo "✅ Setup complete!"
echo ""
echo "════════════════════════════════════"
echo "  Login Credentials:"
echo "  Admin   → admin / admin123"
echo "  Patient → patient1 / patient123"
echo "════════════════════════════════════"
echo ""
echo "⚠️  Set your Anthropic API key:"
echo "   export ANTHROPIC_API_KEY=sk-ant-..."
echo ""
echo "🚀 Starting server at http://127.0.0.1:8000"
echo ""
python manage.py runserver
