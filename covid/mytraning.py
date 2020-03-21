import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle 

def data_split(data,ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    trim_indices = shuffled[test_set_size:] 
    return data.iloc[trim_indices], data.iloc[test_indices]


if __name__ == "__main__":
    #vread csv data
    a = pd.read_csv('covid.csv')

    trim,test = data_split(a,0.2)
    x_train = trim[['avg_fever','bodypain','age','runny_nose','difficulty_breathing']]
    x_test = test[['avg_fever','bodypain','age','runny_nose','difficulty_breathing']]
   
    y_train = trim[['infection_prob']]
    y_test = test[['infection_prob']]
   
    clf = LogisticRegression()
    clf.fit(x_train,y_train)
    
    file = open('model.pkl', 'wb') 
    # source, destination 
    pickle.dump(clf, file)   
    file.close()                   
  

 


