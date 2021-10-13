print(" Welcome to Fizzbuzz! Enter a number between 1 and 100 and\n "
      "I'll show you which are divisible by three (FIZZ), by five (BUZZ) "
      "and\n by both three and five (FIZZBUZZ!)")
go_again = None
while True:
    try:
        user_input = int(input("Your number: "))
        if user_input > 100:
            print("Please, enter a number from 1 to 100!")
        else:
            for x in range(1, user_input+1):
                fizz = x % 3
                buzz = x % 5
                if fizz == 0 and not buzz == 0:
                    print("FIZZ")
                elif buzz == 0 and not fizz == 0:
                    print("BUZZ")
                elif fizz == 0 and buzz == 0:
                    print("FIZZBUZZ")
                else:
                    print(x)
            go_again = input("Would you like to go again? ")
            if go_again.lower() == "yes" or go_again.lower() == "y":
                None
            elif go_again.lower() == "no" or go_again.lower() == "n":
                break
            else:
                print("Let's continue, then!")
    except ValueError:
        print("It has to be a whole number!")
