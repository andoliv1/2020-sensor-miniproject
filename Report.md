# Senior Design 2020 Sensor Miniproject
Collaborators: Andreas Francisco, Nnenna Eze

## Task 0/1: Setting up Python Websockets and Data Flow
The greeting string issued by the server to the client upon first connecting is "ECE Senior Capstone IoT Simulator"

## Task 2: Analysis
* run python analyze_2.py data

1. 
Temperature | Median | Variance
------------|--------|---------
Office | 22.988 | 405.962
Lab1 | 21.002 | 18.435
Class1 | 26.988 | 1907.989

2. 
Occupancy | Median | Variance
----------|--------|---------
Office | 2 | 2.0
Lab1 | 5 | 5
Class1 | 19 | 19.45 

3. 
* run python task3.py data
**Probability Distribution Function Plot for Temperature Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/92656877-d129aa00-f2c1-11ea-82dd-744e2deb4ff2.png" width="500" height="500">

**Histogram Plot for Temperature Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/93241645-a3c27d80-f753-11ea-8134-ca5f0948b4a1.png" width="500" height="500">

**Probability Distribution Function Plot for Occupany Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/92656932-e69ed400-f2c1-11ea-8318-c67c01921fb9.png" width="500" height="500">

**Histogram Plot for Occupancy Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/93241614-9a391580-f753-11ea-8b71-b0720ff16528.png" width="500" height="500">

**Probability Distribution Function Plot for CO2 Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/92656956-f3bbc300-f2c1-11ea-98da-cdbacbef7ca1.png" width="500" height="500">

**Histogram Plot for CO2 Sensor:**

<img src="https://user-images.githubusercontent.com/44929220/93241552-7bd31a00-f753-11ea-8f0c-e1d2ffe98b8d.png" width="500" height="500">

4. 
The mean of the timer interval for the sensors is: 0.998251

The variance of the timer interval for the sensors is: 1.056720264961

**Probability Distribution Function Plot for Time Intervals:**

<img src="https://user-images.githubusercontent.com/44929220/92656972-fc13fe00-f2c1-11ea-82e1-16766291f34f.png" width="500" height="500">

This mimics an erlang distribution which is used to simulate waiting times for independent and identically distributed random variables, for example poisson variables are used to simulate bus arrivals and the waiting time between buses are simulated by erlang so you could say it is a well-know distribution for large systems.



## Task 3: Design
1. This is the percentage of bad data in office: 1.5552995391705071. 
This is the median after removed points: 22.988651867570866 for temperature at office. 
This is the variance after removed points: 0.8887471326179444 for temperature at office.

2. It depends on what you classify as a persistent change, if by a persistent change you mean consistent large fluctuations of temperature then intuitively it would indicate failure since we don't observe large fluctuations of temperature normally in a room, unless you are directly pointing in and out a heat source to the sensor. On the other hand if by persitent change you mean a gradual decrease/increase in temperature due a heat source being turned on then it would not indicate a failure of the sensor.

3. Not considering the anomalies for temperature data and taking the mean and variance after removing the anomalies we can conclude that reasonable bounds for the temperature for the office would be between 20 and 25 degrees.



## Questions to think about for Task 4:
1. How is this simulation reflective of the real world?
Sensors such as the three focused on during this project are used in many different ways in the real world. For example, the temperature sensor is common in office spaces or households to control the heat and AC systems. The occupancy sensor is also common, especially in light systems that monitor when rooms are empty in order to turn off the lights. CO2 sensors are important for ventilation systems, that turn on and off on their own based on the CO2 levels in a building. Many of these sensors work together, and are included in building spaces. In particular sustainable buildings, which have automated light systems and AC units. Of course, there are some aspects of these simulated sensors that do not reflective real world practices, such as the server retrieving the data from all three sensors at relatively the same time. 

2. How is this simulation deficient? What factors does it fail to account for?
The simulation ignores many real world factors. For example, it doesn't take it to account that the temperatures at night should be lower since heat sources are usually turned off and occupancy goes down. The data may also lag in real time, or have technical difficulties. In addition, it is not likely that the data from all three sensors is recieved at the same time. 

3. Difficulty of Python websockets library vs compiled languages
Overall we don't think it was hard to work with the python websockets library. It was very simple to quickly learn and use in our code, and it did not give us much trouble to work with. Originally, the fact that this miniproject was in Python rather than C/C++ was seen as an obstacle, but it proved to be very straightforward and easy to work with. 

4. Would it be better to have server poll sensors or sensors reach out to server when they have data?
In terms of CPU usage you would be better of polling sensors since you know when you want to fetch for data and when you are not doing so you can save energy but if the sensors reach out to the server you have to keep it on to wait for the request and that will consume energy. On the other hand in terms of getting data you would be better waiting for the sensors to reach out to the server since as it was observed in task 2 if you do in the first way you will be requesting data when there is no data at the server and that can also can be expensive. Overall, both sides have its downsides and in order to know which method to use the designer of the system should make an expect cost analysis between what costs him more: requesting for data when there's none or having the system on and waiting for data to be sent.

