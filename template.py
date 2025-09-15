import os

ml_project_name = "ML_project"
# List of project folders
folders = [
    "notebooks",                 # For EDA & experimentation
    "data/raw",                  # Raw tweets
    "data/processed",            # Cleaned tweets
    "artifacts",                 # Saved models, encoders, transformers
    "src/ML_project/components",            # Data ingestion, preprocessing, training
    "src/ML_project/pipeline",              # Training & prediction pipelines
    "src/ML_project/utils",                 # Helper functions
    "src/ML_project/configuration",         # Configurations (YAML, Python dicts)
    "src/ML_project/constant",              # Static constants
    "templates",                 # HTML (for dashboard via Flask/Streamlit)
    "static",                    # CSS/JS files
    "prediction_test_file",      # Upload folder for test predictions
]

# List of starter files
files = [
    "app.py",                    # Flask/Streamlit entrypoint
    "requirements.txt",          # Dependencies
    "setup.py",                  # Package setup
    "src/ML_project/logger.py",             # Custom logger
    "src/ML_project/exception.py",          # Custom exception handling
    "README.md",                 # Documentation
    ".gitignore",                # Ignore unnecessary files
]

def create_project_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        # Add a __init__.py to Python packages
        if "src" in folder:
            init_file = os.path.join(folder, "__init__.py")
            if not os.path.exists(init_file):
                with open(init_file, "w") as f:
                    pass
    
    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                # Add default README content
                if file == "README.md":
                    f.write("# Tech Tweet Sentiment Dashboard\n")
                elif file == "requirements.txt":
                    f.write("pandas\nnumpy\nscikit-learn\nmatplotlib\nsnscrape\nstreamlit\n")
                else:
                    f.write("")

    print("✅ Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
