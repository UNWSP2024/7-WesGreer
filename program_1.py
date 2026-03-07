# Monthly Rainfall(list) Program
# written by Wesley Greer on 3/6/2026

# import statistics for the mean function
import statistics
# create a list and have the user input the amount of rain each month into the list
monthly_rainfall = []
for month in range(1,13):
    print('What was the total rainfall (in inches) for month', month)
    rain = float(input('Enter Here: '))
    monthly_rainfall.append(rain)
    
# The program should calculate and display the total rainfall for the year, avg, lowest and highest values
total_rainfall = sum(monthly_rainfall)
avg_rainfall = statistics.mean(monthly_rainfall)
low_rainfall = min(monthly_rainfall)
high_rainfall = max(monthly_rainfall)

print(f'The total rainfall for the year was {total_rainfall:.2f} inches.')
print(f'The average rainfall for the year was {avg_rainfall:.2f} inches.')
print('The lowest amount of rainfall in one month was', low_rainfall, 'inches.')
print('The highest amount of rainfall in one month was', high_rainfall, 'inches.')
