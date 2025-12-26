import os

# Project configuration
PROJECT_NAME = "hsz_neural_initialized_sim_refinement"

# Define the folder structure
FOLDERS = [
    f"{PROJECT_NAME}/data/raw",
    f"{PROJECT_NAME}/data/synthetic",
    f"{PROJECT_NAME}/data/processed",
    f"{PROJECT_NAME}/notebooks",
    f"{PROJECT_NAME}/src",
    f"{PROJECT_NAME}/submissions",
]

# Define initial files and their content
FILES = {
    f"{PROJECT_NAME}/README.md": f"""# {PROJECT_NAME}

## Challenge: Heat Signature Zero
**Objective:** Inverse heat diffusion using active inference.

### Structure
- `data/`: Raw inputs and synthetic generated data.
- `notebooks/`: Exploratory analysis and prototyping.
- `src/`: Core logic (Simulator wrapper, Models, Optimizer).
- `submissions/`: Output files for the leaderboard.
""",

    f"{PROJECT_NAME}/.gitignore": """# Python
__pycache__/
*.py[cod]
.ipynb_checkpoints/

# Data (Never commit large datasets)
data/
*.npz
*.npy
*.csv
*.h5

# Models
*.pth
*.pt
*.ckpt

# IDEs
.vscode/
.idea/
""",

    f"{PROJECT_NAME}/requirements.txt": """numpy
pandas
matplotlib
scipy
torch
torchmetrics
jupyterlab
tqdm
""",

    f"{PROJECT_NAME}/src/__init__.py": "",

    f"{PROJECT_NAME}/src/simulator.py": """# simulator.py
# Wrapper for the ThinkOnward thermal simulation engine.

class ThermalSimulator:
    def __init__(self):
        pass

    def forward(self, params):
        # TODO: Implement the call to the official simulator here
        pass
""",

    f"{PROJECT_NAME}/src/models.py": """# models.py
# Neural Network Architectures (The 'Guesser')
import torch.nn as nn

class InverseModel(nn.Module):
    def __init__(self):
        super().__init__()
        # TODO: Define architecture
        pass
""",

    f"{PROJECT_NAME}/src/optimizer.py": """# optimizer.py
# Logic for Simulation-Refinement (The 'Refiner')

def run_active_inference(model, simulator, input_data):
    # TODO: Implement the predict -> simulate -> refine loop
    pass
""",

    f"{PROJECT_NAME}/src/utils.py": """# utils.py
# Metrics, plotting, and data loading helpers

def calculate_metrics(pred, target):
    pass
"""
}

def create_structure():
    print(f" Initializing project: {PROJECT_NAME}...")

    # Create Folders
    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)
        print(f"   [DIR]  {folder}")

    # Create Files
    for file_path, content in FILES.items():
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"   [FILE] {file_path}")
        else:
            print(f"   [SKIP] {file_path} (already exists)")

    print(f"\n Done! Navigate into the folder:\n   cd {PROJECT_NAME}")

if __name__ == "__main__":
    create_structure()