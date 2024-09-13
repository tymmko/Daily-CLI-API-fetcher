'''
Module to represent time entries in a formatted way.
'''
import json
import pandas as pd
import isodate
from fetcher import *

dumped_json = main()
data = json.loads(dumped_json)

def convert_duration(duration: str) -> str:
    '''
    Function to convert ISO 8601 styled duration format to a human-readable format.
    '''
    if not duration:
        return None
    return isodate.parse_duration(duration)

def convert_date(date: str) -> str:
    '''
    Function to convert ISO 8601 styled data format to a human-readable format.
    '''
    if not date:
        return None
    datetime_obj = isodate.parse_datetime(date)
    return datetime_obj.strftime("%d.%m.%Y")
if __name__ == '__main__':
    data = [
        {'description': entry['name'], 'duration': convert_duration(entry['timeInterval']['duration']), 'date': convert_date(entry['timeInterval']['end'])}
        for entry in data if 'timeInterval' in entry
    ]
    tasks_data = pd.DataFrame(data)
    tasks_data['date'] = pd.to_datetime(tasks_data['date'], format='%d.%m.%Y')
    if not config['extended_report']:
        tasks_data = tasks_data.groupby('description').agg(
            total_duration=('duration', 'sum'),
            date=('date', 'max')
        ).reset_index()

    print(tasks_data.sort_values(by='date', ascending=config['dataframe_asc_order']))
