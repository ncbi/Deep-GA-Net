import numpy as np

import cv2

import matplotlib.pyplot as plt

import os

def normalize_scan(scan):
    
    return (scan / 127.5) - 1.0

    

def preprocess_scan(scan_path):
                
    # scan_path = str(scan_path)
            
    img_names = [img for img in os.listdir(scan_path) if img.endswith('.png')]
                        
    scan = []
            
    for img_name in img_names:

        img_path = os.path.join(scan_path, img_name)

        img = cv2.imread(img_path)

        if len(img.shape) > 2:

            img = img[:,:,0]

        if (img.shape[0] != 128) or (img.shape[1] != 128): 
            
            img = cv2.resize(img, (128, 128))   


        scan.append(img)

    scan = np.stack(scan, axis=-1) 
    
    scan = normalize_scan(scan)

    
    return scan


def match_dims(scan):
        
    scan = np.expand_dims(scan, axis=0)

    scan = np.expand_dims(scan, axis=-1)

    return scan
