#String_Handling
first_string = input("Enter a sentence: ")


changed_string = ""


for num in range(len(first_string)):
    
    if num % 2 == 0:
        changed_string += first_string[num].upper()
  
    else:
        changed_string += first_string[num].lower()

print(changed_string)


print("Practical Task 1: Part 2:changing words to upper and lowercase")

first_string = input("Enter a sentence: ")

words_list = first_string.split()

new_words_list = []


for index, word in enumerate(words_list):
    if index % 2 == 0:
        
        word = word.lower()

        new_words_list.append(word)
    else:
        
        word = word.upper()
        
        new_words_list.append(word)


changed_string2 = " ".join(new_words_list)


print(changed_string2)