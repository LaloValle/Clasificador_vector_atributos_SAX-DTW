"""
    Methoud described in the paper "Using dynamic time warping distances as features for improved time series classification"
    as an approach that assures the effectiveness and improved accuracy of their method against the baseline DTW-1NN approach
    because of the use of more robusts ML models.

    The method suggest the use of the DTW distances between an interest time series and the instances of training in order to
    arrange a feature vector with the distances and use it to feed a more robust ML model as SVM, for the classification
    improving the accuracy of the predictions exploiting advantages of models like SVM that are capable of down-weigh datasets
    with noisy training instances.    
    
    According to the text, and implementing a combination of DTW and SAX features composing, it's proven the upgrade of the
    method combining possibly other time series classification methods

    Cons
    ----
        - It can be computational and time expensive as the DTW-Feature vector needs to be composed of all the training instances
          by computing the DTW distance with the interest time series
        - More parameters of the classifier needs to be specified and calculated:
            * As SVC uses a polynomial kernel the degree must be computed and determined with cross validation
        
    Pros
    ----
        - The implementation of a sturdier model can improve the accuracy classification by down-weightening outliers and noisy
          instances that might influence the result

    Parameters
    ----------
    The value of the parameters used in the article:
        polinomial kernel: linear, cuadratic or cubic
"""
import pandas as ps
import numpy as np
import matplotlib.pyplot as plt
# Local Libraries
from LLibraries.DTW import DTW_1NN
from LLibraries.SAX import *
from LLibraries.DTWWindowOptimizer import *
from LLibraries.Tools import stratified_sampling,add_label_column
from Libraries.Tools import standardize

def tests():
    #============================
    # Recovering of the datasets
    #============================
    gestures_Z_dataset = []
    #----------------
    # Pebble Gesture
    #----------------
    # Z Axis
    gestures_Z_dataset = np.genfromtxt(
        './Data/GesturePebbleZ1/GesturePebbleZ1_TRAIN.tsv',
        dtype = np.float16,
        delimiter = '	',
        missing_values = {'NaN'},
        filling_values = {np.NaN}
    )
    # Class labels
    unique_labels = np.unique(gestures_Z_dataset[:,0])
    print('Number of classes >> ', unique_labels.size)
    print('Max lenght time series >> ', gestures_Z_dataset.shape[1])

    ##
    ##
    ##  Incompleto
    ##
    ##




def main():
    tests()

if __name__ == '__main__': main()