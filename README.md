# Daily CLI API Fetcher 
This app is designed to use Clockify API for getting tasks information. 

## Installation
*Install requirements:*

Run:  
`pip install -r requirements.txt` (or `pip3 install -r requirements.txt` if you're a linux or mac user) 


*Run the code:*

`git clone https://github.com/tymmko/Daily-CLI-API-fetcher`

`cd Daily-CLI-API-fetcher`

Add your X_API_KEY in config.yml: API_KEY, HEADER

Run:
`python3 main.py`

## Instruction

This script is designed to create and print a pandas DataFrame that contains a list of tasks and their corresponding durations. It gets task data, processes the duration information, and formats it for easy viewing. The tasks are sorted in descending order based on their durations (You can change this in `configuration/config.yml`). The DataFrame can be further customized or exported for reporting and analysis purposes.
