import matplotlib.pyplot as plt
import pandas as pd


def main():
    df = pd.read_csv("student_performance_ml.csv")

    avg_sleep = df.groupby("FinalResult")["SleepHours"].mean()

    plt.figure(figsize=(6, 4))
    plt.bar(["Fail (0)", "Pass (1)"], avg_sleep, color=["crimson", "royalblue"])
    plt.title("Average Sleep Hours by Result")
    plt.ylabel("Average Sleep Hours")
    plt.show()


if __name__ == "__main__":
    main()