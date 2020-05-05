time = int(input())
curr = 10
today = "Tuesday"

new = curr + time
if new in range(0, 24):
    print(today)
elif new > 23:
    print("Wednesday")
else:
    print("Monday")
