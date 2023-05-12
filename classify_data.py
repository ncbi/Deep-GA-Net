"""

Detects GA in dataset.

Usage:

    python .\classify_data.py --model_folder=<str> --scan_folder=<str> --output_file=<str>

Options:
    --model_folder=<str>       the path of the models
    --scan_folder=<str>        the path of the scans
    --output_file=<str>        the output file
"""


import sys 

import os

from docopt import docopt

import numpy as np

import pandas as pd

import preprocessing

import trained_model

import tensorflow as tf


def classify_main(model_folder='Model', scan_folder='Data', output='predictions.csv'):
            
    print('Loading Deep-GA-Net')

    model = trained_model.load(model_folder)
    
    # model.summary()
        
    scan_list = [scan for scan in os.listdir(scan_folder) if os.path.isdir(os.path.join(scan_folder, scan))]
    
    print('#scans in folder is', len(scan_list))
    
    predictions = []
    
    for scan_name in scan_list:
        
        print('predicting scan', scan_name)
        
        scan_path = os.path.join(scan_folder, scan_name)
        
        scan = preprocessing.preprocess_scan(scan_path)       
        
        scan = preprocessing.match_dims(scan)
        
        print(scan.shape)
        
        # scan = tf.cast(scan, tf.float32)
        
        pred = model.predict(scan) # , verbose=0
        
        print(pred[0][0])
            
        predictions.append(pred[0][0])
    
    
    predictions = np.array(predictions)
    
    df = pd.DataFrame(predictions)
    
    df.to_csv(output, index=False)
    
            

if __name__ == "__main__":
        
    argv = docopt(__doc__, sys.argv[1:])
    
    if len(argv) == 3: # parameters are passed
    
        model_folder = argv['--model_folder']

        scan_folder = argv['--scan_folder']

        output = argv['--output_file']

        classify_main(model_folder, image_folder, output)
    
    else: # no parameters, using the defaults
        
        classify_main()
    





















