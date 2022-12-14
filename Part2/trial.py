import pandas as pd
from matplotlib import pyplot as plt
def plotting_graph():
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    columns = ["SN", "Execution_time_without_test"]
    df = pd.read_csv("encode_verify_100_entries.csv", usecols=columns)
    print("Contents in csv file:", df)
    plt.plot(df.SN, df.Execution_time_without_test)
    plt.show()
