#pseudocode
#program recives data
#program runs an elif statement
#program print out results


#ask for negotiation price
price = int(input("enter your starting price : "))

'''
userble notations
>
>=
<
<=
==
'''
#if price is above 150 the program prints you are too expensive
if price >= 150:
    print("you are too expensive")

#if price is above 150 the program prints negotiate a bit more
elif price >= 75 and price < 150 :
 print("negotiate a bit more")


#if price is above 150 the program prints much better
elif price >= 50 and price < 75:
   print("much better")

   #if price is above 150 the program prints price cannot be true
elif price >= 00 and price < 50:
   print("price cannot be true")

   #if price is above 150 the program prints enter something real

else:
   print("enter something real")