# Senior Design 2020 Sensor Miniproject
Collaborators: Andreas Francisco, Nnenna Eze

## Task 1: Data Flow
The greeting string issued by the server to the client upon first connecting is "ECE Senior Capstone IoT Simulator"

## Task 2: Analysis
Temperature | Median | Variance
------------|--------|---------
Class 1 | 26.944 | 32.765
Office | 22.996 | 8898.989
Lab1 | 21.006 | 50.665

Occupancy | Median | Variance
----------|--------|---------
Class1 | 19 | 19.3
Office | 2 | 1.9
Lab1 | 5 | 5.0



**Probability Distribution Function Plot for Temperature Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/92656877-d129aa00-f2c1-11ea-82dd-744e2deb4ff2.png" width="500" height="500">

**Probability Distribution Function Plot for Occupany Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/92656932-e69ed400-f2c1-11ea-8318-c67c01921fb9.png" width="500" height="500">

**Probability Distribution Function Plot for CO2 Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/92656956-f3bbc300-f2c1-11ea-98da-cdbacbef7ca1.png" width="500" height="500">


The mean of the timer interval for the sensors is: 1.025027

The variance of the timer interval for the sensors is: 1.0242775883559998

**Probability Distribution Function Plot for Time Intervals:**

<img src="https://user-images.githubusercontent.com/44929220/92656972-fc13fe00-f2c1-11ea-82e1-16766291f34f.png" width="500" height="500">

## Task 3: Design

## Questions to think about for Task 4:
1. How is this simulation reflective of the real world?
2. How is this simulation deficient? What factors does it faill to account for?
3. Difficulty of Python websockets library vs compiled languages
4. Would it be better to have server poll sensors or sensors reach out to server when they have data?
