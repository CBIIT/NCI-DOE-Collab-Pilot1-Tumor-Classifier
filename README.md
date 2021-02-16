# NCI-DOE-Collab-Pilot1-Tumor_Classifier

### Description:
The Tumor Classifier capability (TC1) shows how to train and use a neural network model to classify tumor types from molecular features 
(e.g., RNASeq expressions) provided in Genomics Data Commons (GDC).

### User Community:	
Researchers interested in cancer susceptibility/histology; classification of diseases for oncology; cancer biology 

### Usability:	
The provided untrained model can be used by a data scientist to be trained on their own data, or use the trained model to classify the provided test samples. The provided scripts use data that has been downloaded and normalized from GDC.

### Uniqueness:	
Using machine learning to classify molecular data has been comonly used. This capability shows how neural networks can be used in
classification of genomic profiles without downsampling the provided expressions.

### Impact:
Augments existing data quality control methods.

### Components:	

Untrained model: 
* Untrained neural network model is defined in [tc1_baseline_keras2.py] (./Pilot1/TC1/tc1_baseline_keras2.py)

Data:
* Processed training and test data in [MoDaC] (https://github.com/CBIIT/NCI-DOE-Collab-Pilot1-Tumor_Classifier/blob/master/Pilot1/TC1/modac.cancer.gov)

Trained Model:
* Trained model is defined by combining untrained model + data + weights and topology. 
* Trained model weights and topology are used in inference ([tb1_default_model.txt] (https://github.com/CBIIT/NCI-DOE-Collab-Pilot1-Tumor_Classifier/blob/master/Pilot1/TC1/tc1_default_model.txt)).

### Technical Details:
Please refer to this [README](./Pilot1/TC1/README.md)
