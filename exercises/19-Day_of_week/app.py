#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
  day_dict = {0:[day for day in range(4,365+1,7)],
              1:[day for day in range(5,365+1,7)],
              2:[day for day in range(6,365+1,7)],
              3:[day for day in range(7,365+1,7)],
              4:[day for day in range(1,365+1,7)],
              5:[day for day in range(2,365+1,7)],
              6:[day for day in range(3,365+1,7)],
              }
  for week_day,year_day in day_dict.items():
    if k in year_day:
      return week_day




#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(2))