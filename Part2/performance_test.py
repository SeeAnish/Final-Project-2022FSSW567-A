import json
import unittest
import MRTD
import time
import csv
from MRTDtest import main as run_unit_test

def speed_test_verify_endoced_with_test( first , last , fileName , step_num):
    with open('records_encoded.json') as json_file:
        tic = time.perf_counter()
        data = json.load(json_file)
        records = data["records_encoded"]
        with open(fileName, 'w', newline='') as time_data_file:
            time_writer = csv.writer(time_data_file)
            time_writer.writerow(["Lines Executed", "time in seconds with test"])
            tic = time.perf_counter()
            for i in range(first, last , step_num):
                MRTD.vertify(records[i])
                run_unit_test()
                # print("Record Number #", i + 1)
                # print(records[i], "\n", "\n")
                t2 = time.perf_counter()
                if i == 99:
                    time_writer.writerow([i + 1, f"{t2 - tic:0.8f}"])
                elif (i+1) % 1000 == 0:
                    time_writer.writerow([i + 1, f"{t2 - tic:0.8f}"])
            print(f"csv file updated - {fileName}.")
        tac = time.perf_counter()

        print(f"Verified {last-first} files in - ", f"{tac - tic:0.4f}", "ms")


def speed_test_verify_endoced_without_test( first , last , fileName , step_num):
    with open('records_encoded.json') as json_file:
        tic = time.perf_counter()
        data = json.load(json_file)
        records = data["records_encoded"]
        with open(fileName, 'w', newline='') as time_data_file:
            time_writer = csv.writer(time_data_file)
            time_writer.writerow(["Lines Executed", "time in seconds without test"])
            tic = time.perf_counter()
            for i in range(first, last , step_num):
                MRTD.vertify(records[i])
                # print("Record Number #", i + 1)
                # print(records[i], "\n", "\n")
                t2 = time.perf_counter()
                if i == 99:
                    time_writer.writerow([i + 1, f"{t2 - tic:0.8f}"])
                elif (i+1) % 1000 == 0:
                    time_writer.writerow([i + 1, f"{t2 - tic:0.8f}"])
            print(f"csv file updated - {fileName}.")
        tac = time.perf_counter()

        print(f"Verified {last-first} files in - ", f"{tac - tic:0.4f}", "ms")



if __name__ == '__main__':

    speed_test_verify_endoced_with_test(0 , 10000 , "encode with test case.csv" , 1)
    speed_test_verify_endoced_without_test(0, 10000, "encode without test case.csv", 1)