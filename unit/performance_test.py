import json
import unittest
import MRTD
import time
import csv


def speed_test_verify_endoced(num , fileName):
    with open('records_encoded.json') as json_file:
        tic = time.perf_counter()
        data = json.load(json_file)
        records = data["records_encoded"]
        with open(fileName, 'w', newline='') as time_data_file:
            time_writer = csv.writer(time_data_file)
            time_writer.writerow(["SN", "time_from_start"])
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

if __name__ == '__main__':
    speed_test_verify_endoced(100 , 'encode_verify_100_entries.csv')

    #new data