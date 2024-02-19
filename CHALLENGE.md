# Instructions

The MAPER system processes and stores measurements from 10,000 sensors that send a value to the cloud server every 15 minutes. The server has a Postgres database, and the API and algorithms are implemented in Python using Django. The database contains information from 5 years of these 10,000 sensors.

1. **Design a database table** to store values received from the 10,000 sensors every 15 minutes. Additionally, design an API to be implemented with Django, allowing the Frontend to request measurements from up to 16 sensors simultaneously for a maximum period of 1 year. Do not implement the design, but:
    a. Define the format of the Request and the Response, including details of the data format to be transmitted to the Frontend.
    b. Define columns and other design parameters for the database table.
    c. Outline general considerations on how the API would function when the Frontend issues a GET request.

2. Implement a "hour meter" (machine runtime meter). Each monitored machine has 4 sensors installed. These sensors measure the machine's vibration simultaneously. A CSV with vibration values reported by each sensor and timestamp is provided.

    - **Design and create a database table** to store the daily operating time of each machine. Use the database engine of your preference.

    - **Design and implement an algorithm** that measures the machine's operating hours (i.e., the time the machine was turned on, in hours). In production, this algorithm would run once a day, "looking" at the vibration data from the previous day, calculating the operating hours. Do not implement the periodic execution mechanism of this algorithm, but design and implement the algorithm in isolation. The input to the algorithm is the CSV data, but the output should be written to the database table.

    - **Design and implement a Django API** for the Frontend to request the operating hours of a specific machine on a specific day.
