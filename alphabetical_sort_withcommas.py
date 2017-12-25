# Program to enter comma separated sequence of words and print them alphabetically and comma separated
sequence = input("Enter series of words with commas: ")
print("Entered string = ", sequence)
str1 = sequence.split(",")
str1.sort()
updated_str = ",".join(str1)
print("Updated string = ",updated_str)