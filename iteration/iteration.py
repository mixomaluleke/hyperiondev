# variable initialised
total = 0
count = 0

# asking the user to enter a number until break
while True:
    # Get user input
    num = input("Enter a number (enter -1 to stop): ")

    # if input is -1 the loop breaks
    if num == '-1':
        break

    # Check if the input is a number
    if not num.lstrip('-').isdigit():
        print("Invalid input.")
        continue

    # Convert the input to a float
    num = float(num)

    # Increment the count and add the number to the total
    count += 1
    total += num

# Check if any numbers were entered (excluding -1)
if count > 0:
    # Calculate the average
    average = total / count
    print(f"The average of the numbers entered is: {average}")
else:
    print("No number entered.")