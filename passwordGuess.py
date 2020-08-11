guest_count = 0

correct_pass = "123456"

while True:
    pass_guess = input("Enter your password: ")
    guest_count += 1

    if pass_guess == correct_pass:
        print("You have successfully logged in!")
        break
    elif pass_guess != correct_pass:
        if guest_count >= 3:
            print("You have been denied access!")
            break
