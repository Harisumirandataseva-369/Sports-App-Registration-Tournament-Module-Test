#!/usr/bin/env python3
"""
Streamlit Tunnel Helper - Creates ngrok tunnel and displays public URL
"""

import subprocess
import time
import os
from pathlib import Path

def main():
    print("=" * 60)
    print("🏆 Sports App Tunnel Setup")
    print("=" * 60)
    print()
    
    # Check if pyngrok is installed
    try:
        from pyngrok import ngrok
    except ImportError:
        print("❌ pyngrok not installed. Installing...")
        subprocess.check_call([
            "pip", "install", "pyngrok"
        ])
        from pyngrok import ngrok
    
    print("✅ pyngrok installed")
    print()
    
    # Create two terminals
    print("Starting Streamlit and ngrok tunnel...")
    print()
    
    # Start Streamlit
    print("1️⃣  Starting Streamlit on port 8501...")
    try:
        streamlit_process = subprocess.Popen(
            ["streamlit", "run", "app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ Streamlit started")
    except Exception as e:
        print(f"❌ Error starting Streamlit: {e}")
        return
    
    # Wait for Streamlit to start
    time.sleep(3)
    
    # Start ngrok tunnel
    print("\n2️⃣  Creating ngrok tunnel...")
    try:
        from pyngrok import ngrok
        
        # Connect ngrok tunnel
        public_url = ngrok.connect(8501, "http")
        
        print("✅ ngrok tunnel created!")
        print()
        print("=" * 60)
        print("🌐 Public Tunnel URL:")
        print("=" * 60)
        print()
        print(f"   🔗 {public_url}")
        print()
        print("=" * 60)
        print()
        print("📍 Local URL: http://localhost:8501")
        print()
        print("Press Ctrl+C to stop tunnel and Streamlit")
        print("=" * 60)
        
        # Keep tunnel alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n🛑 Stopping tunnel and Streamlit...")
            streamlit_process.terminate()
            ngrok.disconnect(public_url)
            print("✅ Stopped")
            
    except Exception as e:
        print(f"❌ Error creating tunnel: {e}")
        streamlit_process.terminate()

if __name__ == "__main__":
    main()
