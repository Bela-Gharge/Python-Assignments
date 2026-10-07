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


    ## Q1
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    model = DecisionTreeClassifier()
    model.fit(X_train,Y_train)


    ## Q2
    y_pred = model.predict(X_test)
    print(f"Predicted Values : {y_pred}")
    print(f"Actual Values : {Y_test}")
 
    ##Q3
    accuracy = accuracy_score(Y_test,y_pred)
    print(f"Accuracy of the model is : {accuracy*100}")


    ## Q4
    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test,y_pred))
    disp = ConfusionMatrixDisplay(confusion_matrix(Y_test,y_pred) , display_labels= ["Fail (0)" , "Pass (1)"])
    disp.plot(cmap= 'Blues')
    plt.show()


    ## Q5
    ## Training Accuracy
    Y_train_pred = model.predict(X_train)
    train_accuracy = accuracy_score(Y_train , Y_train_pred)*100
    print(f"Training Accuracy is : {train_accuracy}")

    ## Testing Accuracy 
    Y_test_pred = model.predict(X_test)
    test_accuracy = accuracy_score(Y_test , Y_test_pred)*100
    print(f"Testing Accuracy is : {test_accuracy}")

    print("Since both the training accuracy and testing accuracy are 100% we have a good/balanced fit")
    
    

if __name__ == "__main__":
    main()