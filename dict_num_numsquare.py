# Program to ask a number, n from user and generate a dictionary containing (i, i*i), where i = 1 to n
num = int(input("Enter a number: "))
init = 1
final = 0
num_square = {
}
while num != 0:
    if init <= num:
        final += init
        num_square[final] = final * final
        num -= 1
print(num_square)
