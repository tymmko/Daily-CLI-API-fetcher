'''
Module to represent tasks in great stdout way.
'''
from fetcher import * 
import json
import pandas as pd
import isodate

dumpted_json = main()
data = json.loads(dumpted_json)

def convert_duration(duration: str) -> str:
    '''
    Function converts ISO 8601 styled duration format to simple date format.
    '''
    if not duration:
        return None
    return isodate.parse_duration(duration)
    
if __name__ == '__main__':
    data = [
        {'name': task['name'], 'duration': convert_duration(task['duration'])}
        for task in data
    ]
    df = pd.DataFrame(data).sort_values(by='duration', ascending= config['dataframe_asc_order'])
    print(df)
