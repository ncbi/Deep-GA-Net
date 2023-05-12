# Deep-GA-Net 
This repository provides scripts, OCT scan samples, and heatmap samples for the paper titled "Deep-GA-Net for Accurate and Explainable Detection of Geographic Atrophy on Optical Coherence Tomography Scans".

## Instructions to set up
### Prerequisites
Have python 3.8, tensorflow 2.3, keras 2.4 installed locally.

### Clone the repository
```
git clone https://github.com/ncbi/Deep-GA-Net.git
cd Deep-GA-Net
```

### Create a virtual environment
```
python3.8 -m venv deep_ga_net
source deep_ga_net/bin/activate 
```

### The trained models
You can access the trained Deep-GA-Net model from the "Model" folder. We included the models with the best accuracy across the folds of the cross-validation. This model was trained on our development dataset.
We compressed the models to be able to upload them. You can extract the model files using any software. Note that the password is "deepganet".

You can extract the model from git shell widnow using the following command
```
unzip Model/final_model.zip -d Model
unzip Model/best_model.zip -d Model
```
Please, type the password "deepganet" (i.e., without quotes "") when prompted to do so.


### Sample scans
We included sample OCT scans (i.e., 3 scans) along with the en face projections and the heatmaps generated from our model. We compressed the OCT scans in one file for conveniecne. You can extract the compresed file using and software. Note that the password is "deepganet".

You can extract the data from git shell widnow using the following command
```
unzip Data/Data.zip -d Data
```
Please, type the password "deepganet" (i.e., without quotes "") when prompted to do so.

### Run the script
You can run the model on the sample data using

```
python3.8 .\classify_data.py
```
Please note that models and images are provided in the repository

You can run the model on new data using
```
python3.8 classify_data.py --model_folder="Model" --scan_folder="your_data_folder" --output_file="your_output.csv"
```
Please, stucture your data folder simialr to the provided samples. Make sure to have a folder for each scan including 128 B-scans. If your OCT scan has differnt number of B-scans, you many resample to have the exact number of B-scans.


## Heatmpas of sample scans
The samples can be accessed from "Heatmaps" folder and the corresponding en face projections can be accessed from the "En face" folder.

## NCBI's Disclaimer
This tool shows the results of research conducted in the [Computational Biology Branch](https://www.ncbi.nlm.nih.gov/research/), [NCBI](https://www.ncbi.nlm.nih.gov/home/about). 

The information produced on this website is not intended for direct diagnostic use or medical decision-making without review and oversight by a clinical professional. Individuals should not change their health behavior solely on the basis of information produced on this website. NIH does not independently verify the validity or utility of the information produced by this tool. If you have questions about the information produced on this website, please see a health care professional. 

More information about [NCBI's disclaimer policy](https://www.ncbi.nlm.nih.gov/home/about/policies.shtml) is available.

About [text mining group](https://www.ncbi.nlm.nih.gov/research/bionlp/).

## For Research Use Only
The performance characteristics of this product have not been evaluated by the Food and Drug Administration and is not intended for commercial use or purposes beyond research use only. 

## Acknowledgement
This research was supported in part by the Intramural Research Program of the National Eye Institute, National Institutes of Health, Department of Health and Human Services, Bethesda, Maryland, and the National Center for Biotechnology Information, National Library of Medicine, National Institutes of Health. The sponsor and funding organization participated in the design and conduct of the study; data collection, management, analysis, and interpretation; and the preparation, review and approval of the manuscript.
The views expressed herein are those of the authors and do not reflect the official policy or position of Walter Reed National Military Medical Center, Madigan Army Medical Center, Joint Base Andrews, the U.S. Army Medical Department, the U.S. Army Office of the Surgeon General, the Department of the Air Force, the Department of the Army/Navy/Air Force, Department of Defense, the Uniformed Services University of the Health Sciences or any other agency of the U.S. Government. Mention of trade names, commercial products, or organizations does not imply endorsement by the U.S. Government.


## Cite our work
Elsawy, Amr, Tiarnan DL Keenan, Qingyu Chen, Xioashuang Shi, Alisa T. Thavikulwat, Sanjeeb Bhandari, Emily Y. Chew, and Zhiyong Lu. "Deep-GA-Net for Accurate and Explainable Detection of Geographic Atrophy on Optical Coherence Tomography Scans." Ophthalmology Science.