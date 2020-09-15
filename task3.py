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
import math


def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}
    counter = 0
    counter2 = 0
    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])
            if(room == "office"):
                counter += 1
                temp_std = math.sqrt(18)
                temp_mean = 22.28
                if(r[room]["temperature"][0] > temp_mean - 2*temp_std and r[room]["temperature"][0] < 2*temp_std + temp_mean):
                    counter2 += 1
                    temperature[time] = {room: r[room]["temperature"][0]}
                    occupancy[time] = {room: r[room]["occupancy"][0]}
                    co2[time] = {room: r[room]["co2"][0]}

            else:
                temperature[time] = {room: r[room]["temperature"][0]}
                occupancy[time] = {room: r[room]["occupancy"][0]}
                co2[time] = {room: r[room]["co2"][0]}

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }
    print("This is the percentage of bad data in office " + str((( 1- (counter2/counter))*100)))
    return data


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)

    for k in data:
        # this is for part c of the question I have not yet been able to plot the density function of the timedelta intervals
        time = data[k].index
        if(k == "temperature"):
            # median of data[k] and var of data[k] which is letter a)b) of task 2
            print("This is the median after removed points " + str(data[k]["office"].median()) + " for " + str(k) + " at office")
            print("This is the variance after removed points " + str(data[k]["office"].var()) + " for " + str(k) + " at office")
            #density function of each sensor type which is letter c) of task 2



    plt.show()