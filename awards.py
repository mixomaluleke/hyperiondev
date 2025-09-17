''' pseudocode
    #program recievs times for event
    #program calculates total times
    #program gives you an award
'''
# input the times for each event
cycle_times = float(input("Enter cycling time in minutes: "))
swimmers_times = float(input("Enter swimmers time in minutes: "))
runners_times = float(input("Enter runners time in minutes: "))

# Calculate the total time for the triathlon completion
total_time = cycle_times + swimmers_times + runners_times

# Display the total time taken
print("Total time taken for the triathlon:", total_time, "minutes")

# Determine the award based on the total time taken
if total_time <= 100:
    award = "Provincial Colours"
elif total_time <= 105:
    award = "Provincial Half Colours"
elif total_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"

# Display the award
print("Award:", award)