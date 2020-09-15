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
import math

def detect_anomaly( log_file :Path):
    with open('testing.txt') as fp:
        while True:
            try:
                s  = fp.readline()
                p = ast.literal_eval(s)
                # print(p)
                try:
                    temp = p.get('office').get('temperature')
                    temp_std = math.sqrt(18)
                    temp_mean = 21
                    # print(temp[0])
                    if(temp[0] >  temp_mean + 2*temp_std):
                        print("This is an outlier at office and this is the temp recorded " + str(temp[0]))
                        print("This is the time " + str(p.get('office').get('time')))
                    elif(temp[0] < temp_mean - 2*temp_std):
                        print("This is an outlier at office and this is the temp recorded " + str(temp[0]))
                        print("This is the time " + str(p.get('office').get('time')))

                except AttributeError:
                    try:
                        temp = p.get('lab1').get('temperature')
                        # occupancy = p.get('lab1').get('occupancy')
                        temp_std = math.sqrt(1908)
                        temp_mean = 26.98
                        # print(temp)
                        if(temp[0] >  temp_mean + 2*temp_std):
                            print("This is an outlier at lab1 and this is the temp recorded " + str(temp[0]))
                            print("This is the time "+ str(p.get('lab1').get('time')))
                        elif(temp[0] < temp_mean - 2*temp_std):
                            print("This is an outlier at lab1 and this is the temp recorded " + str(temp[0]))
                            print("This is the time " + str(p.get('lab1').get('time')))

                    except AttributeError:
                        temp = p.get('class1').get('temperature')
                        # occupancy = p.get('class1').get('occupancy')
                        temp_std = math.sqrt(406)
                        temp_mean = 23
                        # print(temp)
                        if(temp[0] >  temp_mean + 2*temp_std):
                            print("This is an outlier at class1 and this is the temp recorded " + str(temp[0]))
                            print("This is the time " + str(p.get('class1').get('time')))
                        elif(temp[0] < temp_mean - 2*temp_std):
                            print("This is an outlier at class1 and this is the temp recorded " + str(temp[0]))
                            print("This is the time " + str(p.get('class1').get('time')))
            except:
                print('sleep')
                time.sleep(1)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description='Anomaly detector')
    p.add_argument('log_file', help = 'Please enter where the data is')
    P = p.parse_args()
    detect_anomaly(P.log_file);
    