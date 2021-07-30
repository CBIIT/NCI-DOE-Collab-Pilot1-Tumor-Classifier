# NCI-DOE-Collab-Pilot1-Tumor-Classifier

### Description:
The Tumor Classifier capability (TC1) shows how to train and use a neural network model to classify tumor types from molecular features (such as RNA-Seq expressions) provided in Genomics Data Commons (GDC).

### User Community:	
Researchers interested in cancer susceptibility/histology; classification of diseases for oncology; cancer biology.

### Usability:	
Data scientists can train the provided untrained model on their own data, or use the trained model to classify the provided test samples. The provided scripts use data that have been downloaded from GDC and normalized.

### Uniqueness:	
Researchers have commonly used machine learning to classify molecular data. This capability shows how you can use neural networks in classification of genomic profiles without downsampling the provided expressions.

### Components:	
* Untrained model: 
  * The untrained neural network model is defined in [tc1.model.json](https://modac.cancer.gov/searchTab?dme_data_id=NCI-DME-MS01-6996872), and is also available in YAML format.
* Data:
  * The processed training and test data are in [MoDaC](https://modac.cancer.gov/searchTab?dme_data_id=NCI-DME-MS01-6996872).
* Trained model:
  * The trained model is defined by combining the untrained model and model weights.
  * The trained model weights are used in inference [tc1.model.h5](https://modac.cancer.gov/searchTab?dme_data_id=NCI-DME-MS01-6996872)

### Technical Details:
Refer to this [README](./Pilot1/TC1/README.md)
