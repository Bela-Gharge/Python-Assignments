import pandas as pd 
import matplotlib.pyplot  as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay

def main():
    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    X = df.drop(columns=['FinalResult'])
    Y = df['FinalResult']


    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    depth_variation = [1,3,None]

    for depth in depth_variation :  
        model = DecisionTreeClassifier(max_depth=depth,random_state=42)
        model.fit(X_train,Y_train)

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test,y_pred)
        print(f"Accuracy for max depth {depth} is : {accuracy*100}")

    

if __name__ == "__main__":
    main()