import pandas as pd
import matplotlib.pyplot as plt

def main():
    Datapath = "student_performance_ml.csv"
    df = pd.read_csv(Datapath)

    plt.figure(figsize=(8,5))
    plt.hist(
        df['StudyHours'],
        bins = 10,
        color = 'royalblue',
        rwidth = 1.0,
        edgecolor = 'black',
        label = 'Students'
            )

    plt.title("Average Study Hours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    plt.grid(True)

    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()