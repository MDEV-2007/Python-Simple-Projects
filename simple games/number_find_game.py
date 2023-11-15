secret_number = 10
chane_count = 0
chane_limet = 3

while chane_count < chane_limet:
    Input  = int(input("Plese enter number: "))
    chane_count += 1
    if Input == secret_number:
        print("You Won!")
        break
else:
    print("You Lost!")