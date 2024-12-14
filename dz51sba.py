from datetime import datetime
from datetime import timedelta

def date_range(start_date, end_date):
    date_list = []
    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')

    
        while start_date_dt <= end_date_dt:
            date_list.append(start_date_dt.strftime('%Y-%m-%d'))
            start_date_dt += timedelta(days=1)
    
    finally: 
        return(date_list)
    
start_date = '2022-01-01'  
end_date = '2022-01-03'
print(date_range(start_date,end_date))