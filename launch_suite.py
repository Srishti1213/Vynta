import subprocess
import os

def run_gui():
    subprocess.run(["python", "main_gui.py"], cwd="gui-version")

def run_web():
    subprocess.run(["streamlit", "run", "streamlit_app.py"], cwd="web-version")

def run_cli():
    subprocess.run(["python", "main.py"], cwd="cli-version")

if __name__ == "__main__":
    print("\n🔍 Android Forensic Analysis Suite")
    print("===================================")
    print("1. Streamlit Web Interface")
    print("2. Desktop GUI")
    print("3. Command Line (Full Suite)")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice == "1":
        run_web()
    elif choice == "2":
        run_gui()
    elif choice == "3":
        run_cli()
    else:
        print("❌ Invalid option. Please run again.")
