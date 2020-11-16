# PyTorch: Using MLflow and Optuna for experiment tracking and hyperparameter optimization

This repository belongs to the [guide I wrote on Medium](add_url)

## Setup
1. Clone the project: `git clone https://github.com/StefanieStoppel/pytorch-mlflow-optuna.git`.
1. Open a terminal and cd into your project directory. 

### Creating a virtual environment 
You can either use [Python's venv](https://docs.python.org/3/library/venv.html) or [Conda](https://docs.conda.io/en/latest/):

#### Venv 
1. Create the virtual environment using Python >= 3.7: `python3 -m venv ./venv`.
2. Activate the virtual environment: `source venv/bin/activate`. 
3. Install all requirements: `pip install -r requirements.txt`

#### Conda 
1. Create the conda environment and install all dependencies: `conda env create --file environment.yml`.
2. Activate the conda environment: `conda activate pytorch-mlflow-optuna`. 

## Run
All subsequent commands assume you're in the context of a virtual environment / conda environment.

1. Start the MLflow UI in one terminal window by typing `mlflow ui` and visit [http://localhost:5000/](http://localhost:5000) in your browser to view it.
2. In a new terminal start the jupyter server: `jupyter notebook` and visit [http://localhost:8888/](http://localhost:8888) in your browser.
3. Open the notebook called `mlflow-optuna-pytorch.ipynb`.
4. Execute all cells and watch the network being trained.
5. The best set of hyperparameters & the corresponding trial number will be printed once the 5 trials are completed.
6. You can check out the different experiment runs, their hyperparameters and loss metric plots in the MLflow UI.