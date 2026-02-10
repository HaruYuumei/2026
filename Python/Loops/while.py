#basic python course


# LOOPS
# While
# For


# While is a loop state that will continuously iterating as long as its condition is True
count = 0
isTrue = True
while count < 10:
    count += 1
    print(count)

# you can use a break statement to stop a loop 
count = 0
while count < 25:
    count +=1
    print(count)
    if count >12:
        break       # Exits the loop


# you can use Continue to stop the current iteration and continue to the next

count = 0
while count < 30:
    count+=1
    print(count)
    if count ==20:
        print("pausing and continuing")
        continue        # keep going


# you can use else to run a block of code after the condition of the While became False

count = 0
while count < 10:
    count+=1
    print(count)
else:
    print("count is over 10 now")