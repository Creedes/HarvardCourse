print("-----Function-----")

print("1. Input() Function")
print('What is your name?')
myName = input()
print("It is good to meet you,", myName)
print(f"Hello again, {myName}")

print("2. len() Function")
# Evaluates to the integer value of the number of characters in a string:
print("Dein Name hat", len(myName), "Buchstaben")

print("3. str(), int(), float() Function")
# Integer to String or Float:
print('I am {} years old.'.format(str(29)))
print("and i am roundabout {}cm tall" .format(int(176.87)))
print("------------------\n")