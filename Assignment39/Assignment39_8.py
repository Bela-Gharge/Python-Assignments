import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

def main():
    Border = "-"*50

    print(Border)
    print("Step 1 : Loading Dataset")
    Datapath = "student_performance_ml.csv"
    df = pd.read_csv(Datapath)
    print(Border)


    print(Border)
    print("Step 2 : Data Analysis")
    print("Shape of Dataset : ",df.shape)
    print("Column Names : ",list(df.columns))
    print("Missing values per column : ")
    print(df.isnull().sum())
    print("Statistical Report : ")
    print(df.describe())
    print(Border)


    print(Border)
    print("Step 3 : Visualization")
    plt.figure(figsize=(10,8))
    #############################
    print(Border)


    print(Border)
    print("Step 4 : Train-Test split")
    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    print("Data Splited successfully")
    print(Border)


    print(Border)
    print("Step 5 : Model Training")
    model = DecisionTreeClassifier(max_depth=3,random_state=42)
    model.fit(X_train,Y_train)
    print("Model trained successfully")
    print(Border)


    print(Border)
    print("Step 6 : Prediction")
    y_pred = model.predict(X_test)
    print("Actual Values : ")
    print(Y_test[:5])
    print("Predicted Values : ")
    print(y_pred[:5])
    print(Border)


    print(Border)
    print("Step 7 : Accuracy Calculation")
    accuracy = accuracy_score(Y_test,y_pred)
    print("Accuracy of model : ",accuracy*100)
    print(Border)


    print(Border)
    print("Step 8 : Confusion Matrix Generation")
    cm = confusion_matrix(Y_test,y_pred)
    print(cm)
    print(Border)


    print(Border)
    print("Step 9 : Final Conclusion")
    
    print("Model is a Balanced/Good fit")
    print(Border)



if __name__ == "__main__":
    main()