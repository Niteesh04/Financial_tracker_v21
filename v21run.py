# run.py — simple launcher for v21_encrpt.py
import os
import v21_encrpt as tracker

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("Launching secure finance tracker (v21)...")
    tracker.run_app(host="127.0.0.1", port=5000, debug=False)
