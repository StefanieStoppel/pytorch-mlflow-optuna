# PyTorch: Using MLflow and Optuna for experiment tracking and hyperparameter optimization

This repository belongs to the [guide I wrote on Medium](add_url)

## Setup
1. Open a terminal and cd into your project directory. Create a virtual environment using [Python's venv](https://docs.python.org/3/library/venv.html)
 to encapsulate the project's dependencies: `python3 -m venv ./venv`.
2. Activate the virtual environment: `source venv/bin/activate`. 
All subsequent commands will be executed in the context of the environment.
3. Install requirements directly: `pip install torch torchvision mlflow optuna jupyter` 
or using the requirements.txt file: `pip install -r requirements.txt`.
4. Start the MLflow UI: `mlflow ui` and visit [http://localhost:5000/](http://localhost:5000) in your browser to view it.
5. In a new terminal start the jupyter server: `jupyter notebook` and visit [http://localhost:8888/](http://localhost:8888) in your browser.
6. Open the notebook `mlflow-optuna-pytorch.ipynb`.