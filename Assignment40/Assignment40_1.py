import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def main():
    ## Step 1 : Load the dataset
    df = pd.read_csv("student_performance_ml.csv")


    ## Step 2 : Separate X and y columns
    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]


    ## Step 3 : Split and train the data
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train,Y_train)


    ### Q1
    importance = pd.Series(model.feature_importances_,index = X.columns)
    print(importance)
    print("Feature affecting least : ",importance.idxmin())
    print("Feature affecting the most : ",importance.idxmax())
    
    

if __name__ == "__main__":
    main()