## MaxScale Docker Setup and Query Script
This repository provides a setup guide and a Python script to interact with a MaxScale database proxy instance. It includes instructions to install the necessary dependencies, set up the MaxScale container, and run the Python script to perform various queries on the database.

## Prerequisites
Docker: Install Docker on your system using the official Docker documentation for your specific operating system.

## Installation

Create a new directory:
```
mkdir maxscale-docker-test
```

Navigate to the directory:
```
cd maxscale-docker-test
```

Clone the project repository:
```
git clone https://github.com/cdumplins/maxscale-docker
```

Navigate to the MaxScale directory:
```
cd maxscale-docker/maxscale
```

Run the Docker Compose YAML file:
```
docker-compose up
```
Verify that everything is working correctly:

```
sudo docker-compose exec maxscale maxctrl list servers
```

Expected output:
```
┌─────────┬──────────┬──────┬─────────────┬─────────────────┬──────┬─────────────────┐
│ Server  │ Address  │ Port │ Connections │ State           │ GTID │ Monitor         │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────┼─────────────────┤
│ calvin1 │ primary1 │ 3306 │ 0           │ Master, Running │      │ MariaDB-Monitor │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────┼─────────────────┤
│ calvin2 │ primary2 │ 3306 │ 0           │ Running         │      │ MariaDB-Monitor │
└─────────┴──────────┴──────┴─────────────┴─────────────────┴──────┴─────────────────┘
```

## Running the Python Script

Install the MySQL Connector module:
```
sudo apt install python3-pip
pip3 install mysql-connector
```

Identify the IP address of the MaxScale container:
```
docker inspect maxscale-maxscale-1
```
Look for the "IPAddress": "<IP_ADDRESS>" key-value pair and **copy the IP address value**.

Navigate to the maxscale directory:
```
cd maxscale-docker/maxscale
```

Edit the python main file:
```
nano main.py
```
Locate the line **host = "<IP_ADDRESS>"** and replace <IP_ADDRESS> with the IP address you copied in the previous step.

Save the file by pressing **Ctrl + O**, then exit the editor with **Ctrl + X**.

Run the Python script:
```
python3 main.py
```

Expected outputs:
Largest Zipcode in zipcodes_one
Zipcodes in Kentucky
Zipcodes between 40000 and 41000
Total Wages in Pennsylvania
Note: If you start a new Docker container, it will have a new IP address assigned. In that case, repeat steps 2-5 to update the IP address in the Python script.

Shutting Down and Removing Containers
To stop and remove the Docker containers, use the following command:

## MaxScale Docker Setup and Query Script
This repository provides a setup guide and a Python script to interact with a MaxScale database proxy instance. It includes instructions to install the necessary dependencies, set up the MaxScale container, and run the Python script to perform various queries on the database.

## Prerequisites
Docker: Install Docker on your system using the official Docker documentation for your specific operating system.

## Installation

Create a new directory:
```
mkdir maxscale-docker-test
```

Navigate to the directory:
```
cd maxscale-docker-test
```

Clone the project repository:
```
git clone https://github.com/cdumplins/maxscale-docker
```

Navigate to the MaxScale directory:


cd maxscale-docker/maxscale
Run the Docker Compose YAML file:
```
docker-compose up
```
Verify that everything is working correctly:

```
sudo docker-compose exec maxscale maxctrl list servers
```

Expected output:
```
┌─────────┬──────────┬──────┬─────────────┬─────────────────┬──────┬─────────────────┐
│ Server  │ Address  │ Port │ Connections │ State           │ GTID │ Monitor         │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────┼─────────────────┤
│ calvin1 │ primary1 │ 3306 │ 0           │ Master, Running │      │ MariaDB-Monitor │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────┼─────────────────┤
│ calvin2 │ primary2 │ 3306 │ 0           │ Running         │      │ MariaDB-Monitor │
└─────────┴──────────┴──────┴─────────────┴─────────────────┴──────┴─────────────────┘
```

## Running the Python Script

Install the MySQL Connector module:
```
sudo apt install python3-pip
pip3 install mysql-connector
```

Identify the IP address of the MaxScale container:
```
docker inspect maxscale-maxscale-1
```
Look for the "IPAddress": "<IP_ADDRESS>" key-value pair and **copy the IP address value**.

Navigate to the Python script file:
```
cd ../..
```
nano main.py
```
Locate the line host = "<IP_ADDRESS>" and replace <IP_ADDRESS> with the IP address you copied in the previous step.

Save the file by pressing Ctrl + O, then exit the editor with Ctrl + X.

Run the Python script:
```
python3 main.py
```
Expected outputs:

Largest Zipcode in zipcodes_one
Zipcodes in Kentucky
Zipcodes between 40000 and 41000
Total Wages in Pennsylvania
Note: If you start a new Docker container, it will have a new IP address assigned. In that case, repeat steps 2-5 to update the IP address in the Python script.

Shutting Down and Removing Containers
To stop and remove the Docker containers, use the following command:
```
docker-compose down -v
```
This will remove the containers and associated volumes.
Zipcodes between 40000 and 41000
Total Wages in Pennsylvania

Note: If you start a new Docker container, it will have a new IP address assigned. In that case, repeat steps 2-5 to update the IP address in the Python script.

Shutting Down and Removing Containers
To stop and remove the Docker containers, use the following command:
```
docker-compose down -v
```
This will remove the containers and associated volumes.
```
docker-compose down -v
```

This will remove the containers and associated volumes.
Zipcodes between 40000 and 41000
Total Wages in Pennsylvania

***Note: If you start a new Docker container, it will have a new IP address assigned. In that case, repeat steps 2-5 to update the IP address in the Python script.***

Shutting Down and Removing Containers
To stop and remove the Docker containers, use the following command:

```
docker-compose down -v
```
This will remove the containers and associated volumes.