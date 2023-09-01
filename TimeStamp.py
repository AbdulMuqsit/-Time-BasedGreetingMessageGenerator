import time
# t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

if(0 <= hour < 12):
    print("Good Morning Sir!")
elif(12 <= hour < 17):
    print("Good Afternoon Sir!")
else:
    print("Good Night Sir!")

# basic code to gets familarised with the python syntax
