import pandas as pd

def main():
    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    # 1
    print(df.head(5))

    # 2
    print(df.tail(5))

    # 3
    print(df.shape)

    # 4
    print(list(df.columns))

    # 5
    print(df.dtypes)

if __name__ == "__main__":
    main()