import pandas as pd
import matplotlib.pyplot as plt

def main():
    Datapath = "student_performance_ml.csv"
    df = pd.read_csv(Datapath)

    pass_students = df[df['FinalResult']==1]
    fail_students = df[df['FinalResult']==0]
    

    plt.figure(figsize=(10,8))
    plt.scatter(
        marker = 'o',
        alpha = 0.9,
        s = 80,
        color = 'royalblue' 
    )



    plt.title("Result")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Scores")
    plt.grid(True)
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()