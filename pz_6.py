from datetime import datetime

def is_leep_year(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
        return True
    else:
        return False
    
def difference_of_days(year1, month1, day1, year2, month2, day2):
    date1 = datetime(year1, month1, day1)
    date2 = datetime(year2, month2, day2)
    
    ref = datetime(1970, 1, 1)
    days1 = (date1 - ref).days + 1 
    days2 = (date2 - ref).days + 1
    
    total_leep_days = 0
    for i in range(year1, year2 + 1):
        if is_leep_year(i):
            total_leep_days += 1
            
    # Функция abs в Python возвращает абсолютное значение числа.
    days_diff = abs(days1 - days2)
    if month1 <= month2:
        days_diff -= total_leep_days if month1 == 2 else (total_leep_days // 2)
    else:
        days_diff += total_leep_days if month1 == 2 else (total_leep_days // 2)
        
    return days_diff

date_diff = difference_of_days(2022, 12, 25, 2023, 1, 1)
print(date_diff)