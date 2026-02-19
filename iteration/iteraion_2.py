# The number of rows
rows = 10

# checking if row is even and greater that 0.
if (rows // 2) * 2 == rows and rows > 0:
    
    count = 0
    star_asteriks = "*"
    half = rows//2

    for index in range(1, rows):
        
        if index <= half:
            count += 1

        else:
            count -= 1

            #print

       print(star_asteriks * count)

else:
    # if an invalid number is entered.
    print("Invalid input.Please enter an even positive integer for 'rows.")