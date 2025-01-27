import datetime


def parse_time(time_str):
    if ':' in time_str:
        return datetime.datetime.strptime(time_str, '%H:%M')
    else:
        return datetime.datetime.strptime(time_str,'%H')


def calculate_interval(start, end):
    start = parse_time(start)
    end = parse_time(end)
    if end<start:
        end += datetime.timedelta(hours=12)
    
    diff = end - start
    return diff.total_seconds()/3600


def process_interval(input_str):
    data = input_str.strip()
    data = data.replace(' ', '')
    data = data.split(',')
    
    total_hours = 0.0
    for interval in data:
        start, end = interval.split('-')
        total_hours+=calculate_interval(start, end)
    
    return total_hours


intervals = '10-12, 10:30-12:45, 12-3, 11:15-2:45'

print(process_interval(intervals))