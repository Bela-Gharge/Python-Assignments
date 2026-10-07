import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.figure(figsize=(7,4))
    plt.boxplot(df["Attendance"], patch_artist=True)

    plt.title("BoxPlot of Attendance")
    plt.ylabel("Attendance")

    plt.grid(axis="y", linestyle = "--" , alpha = 0.7)
    plt.show()

    ## There are no outliers in the plot

    

if __name__ == "__main__":
    main()