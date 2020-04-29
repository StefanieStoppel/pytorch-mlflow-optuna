import neptune
import numpy as np

# The init() function called this way assumes that 
# NEPTUNE_API_TOKEN environment variable is defined.

neptune.init('angelie/sandbox')

# Define parameters

PARAMS = {'decay_factor' : 0.5,
          'n_iterations' : 117}

# Create experiment with defined parameters

neptune.create_experiment (name='example_with_parameters', upload_source_files=['neptune_main.py'], params=PARAMS)

# Upload source code


# log some metrics

for i in range(100):
    neptune.log_metric('loss', 0.95**i)

neptune.log_metric('AUC', 0.96)

# Log image data

array = np.random.rand(10, 10, 3)*255
array = np.repeat(array, 30, 0)
array = np.repeat(array, 30, 1)
neptune.log_image('mosaics', array)
