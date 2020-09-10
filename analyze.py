#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np


def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)
    time = data["temperature"].index
    time_np = time[1:] - time[:-1]
    time_np_series = time_np.total_seconds()
    print(time_np.mean().total_seconds())
    print(pow(np.std(time_np).total_seconds(),2))


    time_np_series = time_np_series.to_frame(index = False)
    time_np_series.plot.density()
    plt.xlabel("Time intervals (seconds)")
    plt.ylabel("Probability")
    plt.title("PDF plot of the time intervals")
    plt.savefig("PDF_time_intervals.png")


    for k in data:
        # this is for part c of the question I have not yet been able to plot the density function of the timedelta intervals
        time = data[k].index

        # median of data[k] and var of data[k] which is letter a)b) of task 2
        print(data[k].median())
        print(data[k].var())
        #density function of each sensor type which is letter c) of task 2
       
        data[k].plot.density()
        plt.xlabel(k)
        plt.ylabel("Probability")
        plt.title("PDF plot of " + str(k))
        plt.savefig("PDF_" + k + ".png")

        data[k].hist()
        plt.xlabel(k)
        plt.ylabel("Quantity")
        plt.title("Histogram for " + str(k))
        plt.savefig("Histogram_" + str(k) + ".png")


    plt.show()
