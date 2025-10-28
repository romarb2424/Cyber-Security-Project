""" 
Cyber Security Project - Main Entry Point
------------------------------------------
This script serves as the main entry point for the Cyber Security project.
It demonstrates a modular project structure and imports reusable functions 
from the `scripts` directory.
"""

import os
import sys
import pandas as pd
from datetime import datetime

# Import utility functions if available (placeholder for real ones)
# from scripts.data_preprocessing import clean_data
# from scripts.model_training import train_model

def load_data(filepath):
    """Load dataset from CSV or Excel file."""
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")

def main():
    print("🔐 Cyber Security Project - Starting Execution...\n")
    
    # Example data loading (adjust as per your dataset)
    data_path = os.path.join('data', 'raw', 'sample_data.csv')
    if os.path.exists(data_path):
        df = load_data(data_path)
        print(f"✅ Loaded data with shape: {df.shape}")
    else:
        print("⚠️ No data file found in 'data/raw/'. Please add your dataset.")
    
    # Placeholder for further steps
    print("\nNext steps:")
    print("1️⃣ Clean and preprocess data (see scripts/data_preprocessing.py)")
    print("2️⃣ Train model (see scripts/model_training.py)")
    print("3️⃣ Evaluate and generate reports (see reports/)")
    
    print("\n📅 Execution completed at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()
