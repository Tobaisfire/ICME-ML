from datetime import datetime, timedelta

import os




def get_all_dates_in_month(year, st_month=1, ed_month=12):
    st_day=1
    end_day=31
    dates = []
    start_date = datetime(year, st_month, st_day)
    end_date = datetime(year, ed_month, end_day)
    
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    
    return [date.strftime("%Y%m%d") for date in dates]


def get_null_dates(path,year, st_month, ed_month):

    all_dates = get_all_dates_in_month(year, st_month, ed_month)
    lis = [i.split("_")[3] for i in os.listdir(f'{path}')]
    diff_in_lis = set(all_dates) - set(lis)

    return diff_in_lis



