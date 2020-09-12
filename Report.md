# Senior Design 2020 Sensor Miniproject
Collaborators: Andreas Francisco, Nnenna Eze

## Task 1: Data Flow
The greeting string issued by the server to the client upon first connecting is "ECE Senior Capstone IoT Simulator"

## Task 2: Analysis
* run python analyze_2.py data

1. 
Temperature | Median | Variance
------------|--------|---------
Office | 22.988 | 405.962

2. 
Occupancy | Median | Variance
----------|--------|---------
Office | 2 | 2.0

3. 
* run python task3.py data
**Probability Distribution Function Plot for Temperature Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/92656877-d129aa00-f2c1-11ea-82dd-744e2deb4ff2.png" width="500" height="500">

**Histogram Plot for Temperature Sensor:**

**Probability Distribution Function Plot for Occupany Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/92656932-e69ed400-f2c1-11ea-8318-c67c01921fb9.png" width="500" height="500">

**Histogram Plot for Occupancy Sensor:**

**Probability Distribution Function Plot for CO2 Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/92656956-f3bbc300-f2c1-11ea-98da-cdbacbef7ca1.png" width="500" height="500">

**Histogram Plot for CO2 Sensor:**
![alt text](https://github.com/[nnennaeze07]/[2020-sensor-miniproject]/blob/[main]/Histogram_co2.jpg?raw=true)

4. 
The mean of the timer interval for the sensors is: 0.998251

The variance of the timer interval for the sensors is: 1.056720264961

**Probability Distribution Function Plot for Time Intervals:**

<img src="https://user-images.githubusercontent.com/44929220/92656972-fc13fe00-f2c1-11ea-82e1-16766291f34f.png" width="500" height="500">

This mimics an erlang distribution which is used to simulate waiting times for independent and identically distributed random variables, for example poisson variables are used to simulate bus arrivals and the waiting time between buses are simulated by erlang so you could say it is a well-know distribution for large systems.



## Task 3: Design
1. 
This is the percentage of bad data in office 1.5552995391705071
This is the median after removed points 22.988651867570866 for temperature at office
This is the variance after removed points 0.8887471326179444 for temperature at office

2. It depends on what you classify as a persistent change, if by a persistent change you mean consistent large fluctuations of temperature then intuitively it would indicate failure since we don't observe large fluctuations of temperature normally in a room, unless you are directly pointing in and out a heat source to the sensor. On the other hand if by persitent change you mean a gradual decrease/increase in temperature due a heat source being turned on then it would not indicate a failure of the sensor.

3. Not considering the anomalies for temperature data and taking the mean and variance after removing the anomalies we can conclude that reasonable bounds for the temperature for the office would be between 20 and 25 degrees.



## Questions to think about for Task 4:
1. How is this simulation reflective of the real world?

2. How is this simulation deficient? What factors does it faill to account for?
It doesn't take it to account that the temperatures at night should be lower since heat sources are usually turned off and occupancy goes down.
3. Difficulty of Python websockets library vs compiled languages
Overall I don't think it was hard to work with the python websockets library.
4. Would it be better to have server poll sensors or sensors reach out to server when they have data?
In terms of CPU usage you would be better of polling sensors since you know when you want to fetch for data and when you are not doing so you can save energy but if the sensors reach out to the server you have to keep it on to wait for the request and that will consume energy. On the other hand in terms of getting data you would be better waiting for the sensors to reach out to the server since as it was observed in task 2 if you do in the first way you will be requesting data when there is no data at the server and that can also can be expensive. Overall, both sides have its downsides and in order to know which method to use the designer of the system should make an expect cost analysis between what costs him more: requesting for data when there's none or having the system on and waiting for data to be sent.

