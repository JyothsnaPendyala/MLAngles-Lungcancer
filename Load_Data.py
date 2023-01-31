import pandas as pd
#changes mades in 
def create_datafarme():
    dataframe = pd.read_csv("Lung_cancer.csv")
    print(dataframe.head())
    return dataframe
create_datafarme()
