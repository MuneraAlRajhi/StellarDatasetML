#!/opt/conda/bin/python


# This is our main file. It runs the accuracy functions from other files.



#imports
from Stellar_ML_Random_Forest import Accuracy



#%%
# random forest accuracy
print("Random Forest Accuracy: ", Accuracy)


#%%
def knn_auc():
    auc = 0.9440833333333334
    return auc

#%% 
knn_auc()
# %%
