#!/bin/bash

echo "=========================================="
echo "🔄 RESTARTING DJANGO SERVER"
echo "=========================================="
echo ""
echo "This will:"
echo "1. Stop any running Django servers"
echo "2. Load new email configuration"
echo "3. Start fresh server"
echo ""

# Kill any running Django servers
echo "🛑 Stopping existing Django servers..."
pkill -f "python3 manage.py runserver" 2>/dev/null || true
pkill -f "python manage.py runserver" 2>/dev/null || true
sleep 2

echo "✅ Stopped"
echo ""

# Clear Python cache
echo "🧹 Clearing Python cache..."
find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
echo "✅ Cache cleared"
echo ""

# Load environment and start server
echo "🚀 Starting Django server with new email configuration..."
echo ""
echo "=========================================="

# Start the server
python3 manage.py runserver

echo ""
echo "=========================================="
echo "Server stopped"
echo "=========================================="
