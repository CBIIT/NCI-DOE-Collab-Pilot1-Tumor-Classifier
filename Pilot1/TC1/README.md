### Model description:
TC1, is a 1D convolutional network for classifying RNA-seq gene expression profiles into 18 balanced tumor types (e.g., breast cancer, melanoma, etc). 
The network follows the classic architecture of convolutional models with multiple 1D convolutional layers interleaved with pooling layers followed by final dense layers. 
The network can optionally use 1D locally connected layers in place of convolution layers as well as dropout layers for regularization. 
The model is trained and cross-validated on a total of 5,400 RNA-seq profiles from the NCI genomic data commons. 
The full set of expression features contains 60,483 float columns transformed from RNA-seq FPKM-UQ values. This model achieves around 98% classification accuracy. 
It is useful for studying the relationships between latent representations of different tumor types as well as classifying synthetically generated gene expression profiles. 
The model has also been used to flag incorrectly typed gene expression profiles from the databases

### Setup:
To setup the python environment needed to train and run this model, first make sure you install [conda](https://docs.conda.io/en/latest/) package manager, clone this repository, then create the environment as shown below.

```bash
   conda env create -f environment.yml -n TC1
   conda activate TC1
   ```

To download the processed data needed to train and test the model, and the trained model files, you should create an account first on the Model and Data Clearinghouse [MoDac](modac.cancer.gov). The training and test scripts will prompt you to enter your MoDac credentials.

### Training:
To train the model from scratch, the script [tc1_baseline_keras2.py](tc1_baseline_keras2.py) does the following:
* Reads the model configuration parameters from [tc1_default_model.txt](tc1_default_model.txt)
* Downloads the training data and splits it to training/validation sets
* Creates and trains the keras model
* Saves the best trained model based on the validation accuracy
* Evaluates the best model on the test dataset


```bash
   python tc1_baseline_keras2.py
   ...
   ...
Loading data...
done
df_train shape: (4320, 60484)
df_test shape: (1080, 60484)
X_train shape: (4320, 60483)
X_test shape: (1080, 60483)
Y_train shape: (4320, 36)
Y_test shape: (1080, 36)
X_train shape: (4320, 60483, 1)
X_test shape: (1080, 60483, 1)
0.0 128 20 1
1.0 128 10 1

_________________________________________________________________
dense_1 (Dense)              (None, 200)               154752200
_________________________________________________________________
activation_3 (Activation)    (None, 200)               0
_________________________________________________________________
dropout_1 (Dropout)          (None, 200)               0
_________________________________________________________________
dense_2 (Dense)              (None, 20)                4020
_________________________________________________________________
activation_4 (Activation)    (None, 20)                0
_________________________________________________________________
dropout_2 (Dropout)          (None, 20)                0
_________________________________________________________________
dense_3 (Dense)              (None, 36)                756
_________________________________________________________________
activation_5 (Activation)    (None, 36)                0
=================================================================
Total params: 154,923,632
Trainable params: 154,923,632
Non-trainable params: 0
_________________________________________________________________
Train on 4320 samples, validate on 1080 samples
Epoch 21/400:
loss: 0.0613 - acc: 0.9819 - val_loss: 0.1349 - val_acc: 0.9722
```

### Inference: 
To test the trained model in inference, the script [tc1_infer.py](tc1_infer.py) does the following:
* Downloads the trained model
* Downloads the processed test dataset with the corresponding labels
* Performs inference on the test dataset
* Reports the accuracy of the model on the test dataset


```bash
   python tc1_infer.py
   
   ...
   json Test score: 0.14670737570462128
   json Test accuracy: 0.9712962962962963
   json acc: 97.13%

   ```
