"""

Loading trained model

Usage:

    python .\trained_model.py --model_path=<str>

Options:
    --model_folder=<str>       the path of the models
    --image_folder=<str>        the path of the images
    --output_file=<str>        the output file
"""

from docopt import docopt

import tensorflow as tf

from tensorflow.keras.models import *


import sys

import os


def load(model_path='Model'):               
    
    best_model = load_model(os.path.join(model_path, 'final_model'))
        
    best_model.load_weights(os.path.join(model_path, 'best_model', 'best_model')) 
        
    return best_model



if __name__ == "__main__":
        
    argv = docopt(__doc__, sys.argv[1:])
    
    # parameters are passed
    
    if len(argv) > 0: 
    
        model_path = argv['--model_path']

        load(model_path)
    
    # no parameters, using the defaults
        
    else: 
        
        load()