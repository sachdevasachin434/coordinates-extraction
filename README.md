# Longitude-Lattitude Extraction

This contains a post endpoint that returns longitude and latitude for the address passed. The project contains 6 test cases to validate
the application.

## Project Setup.
Below are the steps to set up the project for evaluation:
1. Clone the Git repository using ```git clone repository_url```.
2. After cloning the project, go to the project directory.
3. src contains the source code of the project.

## Virtual Environment Setup
1. Open command prompt(Windows) or terminal(Linux) and go to project directory.
2. Make sure you have virtualenv installed on your system.
3. If not already installed, run ```pip install virtualenv``` to install virtualenv on your system.
4. Create a virtual environment using ```virtualenv verloop_env```.
5. Run ```.\verloop_env\Scripts\activate``` command to enable virtualenv
environment.
6. Install project requirements from requirements.txt using ```pip install -r requirements.txt``` command.
7. Run ```pip freeze``` command to check packages installed.

## Steps to hit and run endpoints
#### Prerequisite - Insert GCP key with Maps Embed API enabled into config.json(location-```src/config.json```) file
This file contains the json in which the user can insert GCP key that would be passed into required URL.
1. After enabling the virtual environment, go cd to src folder and run ```flask run``` command to start the flask server.
2. Use postman to hit endpoint.

### Input
Accepts 2 parameters in JSON body with keys as address and output_format.
1. address allows string as instance.
2. output_format allows string as instance and accepts only 2 values as input which is json or XML.
Example json - {
         "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
         "output_format": "json"}

### Output
The API returns 4 types of output:
1. JSON with no error - Returns a json object with coordinates and address.
2. JSON with some error - Returns a json object with error_message.
3. XML with no error - Returns XML with coordinates and address.
4. JSON with some error - Returns XML with error_message.

### Run Test Cases
Go to project directory ```parent_directory/verloop_assignment``` and run ```pytest``` to run test cases.

### Run Pylint
Go to project directory and run pylint src/app to check linting of the code.

#### If anything is required from my side please feel free to contact me at +917015920459 or drop a mail at sachdevasachin434@gmail.com
