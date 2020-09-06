#!/usr/bin/env python3
"""
Program that scans the data in the provided file and detects anomalies and displays if the sensor is faulty
"""
import argparse
import ast
import pandas as pd
import numpy as np
from pathlib import Path
import time
def detect_anomaly( log_file :Path):
    s = 'data.txt'
    arr = numpy.zeros((3,2))
    with open(s) as fp:
        while True:
            try:
                s  = fp.readline()
                p = ast.literal_eval(s)
                try:
                    temp = p.get('office').get('temperature')
                    occupancy = p.get('office').get('occupancy')
                except AttributeError:
                    try:
                        temp = p.get('lab1').get('temperature')
                        occupancy = p.get('lab1').get('occupancy')
                    except AttributeError:
                        temp = p.get('class1').get('temperature')
                        occupancy = p.get('class1').get('occupancy')
            except:
                print('sleep')
                time.sleep(20)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description='Anomaly detector')
    p.add_argument('log_file', help = 'Please enter where the data is')
    P = p.parse_args()
    detect_anomaly(P.log_file);
    