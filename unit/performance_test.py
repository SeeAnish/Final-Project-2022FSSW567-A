import json
import unittest
import MRTD
import pandas as pd
from matplotlib import pyplot as plt
import time
import csv
from MRTDtest import main as run_unit_test

def speed_test_verify_endoced(num , fileName):
    with open('records_encoded.json') as json_file:
        #tic = time.perf_counter()
        data = json.load(json_file)
        records = data["records_encoded"]
        with open(fileName, 'w', newline='') as time_data_file:
            time_writer = csv.writer(time_data_file)
            time_writer.writerow(["SN", "Execution_time_without_test"])
            tic = time.perf_counter()
            for i in range(0, num):
                MRTD.vertify(records[i])
                # print("Record Number #", i + 1)
                # print(records[i], "\n", "\n")
                t2 = time.perf_counter()
                time_writer.writerow([i + 1, f"{t2 - tic:0.8f}"])
            print(f"csv file updated - {fileName}.")
        tac = time.perf_counter()        
        print(f"Decoded {num} files in - ", f"{tac - tic:0.4f}", "ms")

def speed_test_verify_endoced_with_unittest(num , fileName):
    with open('records_encoded.json') as json_file:
        data = json.load(json_file)
        records = data["records_encoded"]
        with open(fileName, 'w', newline='') as time_data_file:
            time_writer = csv.writer(time_data_file)
            time_writer.writerow(["SN", "Execution_time_with_test"])
            tic = time.perf_counter()
            run_unit_test()
            for i in range(0, num):
                MRTD.vertify(records[i])
                # print("Record Number #", i + 1)
                # print(records[i], "\n", "\n")
                tok = time.perf_counter()
                time_writer.writerow([i + 1, f"{tok - tic:0.8f}"])
            print(f"csv file updated - {fileName}.")
        tac = time.perf_counter()        
        print(f"Decoded {num} files in - ", f"{tac - tic:0.4f}", "ms")
    
def plotting_graph1():
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    columns = ["SN", "Execution_time_without_test"]
    df = pd.read_csv("encode_verify_100_entries.csv", usecols=columns)
    print("Contents in csv file:", df)
    plt.plot(df.SN, df.Execution_time_without_test)
    plt.show()


def main():
    k = [100, 1000]
    speed_test_verify_endoced(100 , 'encode_verify_100_entries.csv')
    plotting_graph1()
    speed_test_verify_endoced(1000 , 'encode_verify_100_entries.csv')
    plotting_graph1()
    
    #speed_test_verify_endoced_with_unittest(i, 'unittest_encode_entries.csv')

if __name__ == '__main__':
    main()
    
    #new data