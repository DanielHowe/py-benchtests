# Benchmark test to determine the efficiency of a system
import time

# Start your engines...
print("Calculating time..")
# Get the current time
startTime = time.monotonic_ns()

# Do some calculations
x = 1
for i in range(10):
    x += x**i
    print(x)
endTime = time.monotonic_ns()

#Calculate dif in end time
completionTimeNS = endTime - startTime

print("Completion time in nS - Start to Finish")
print(completionTimeNS)
print("Completion time in Seconds - Start to Finish")
print(completionTimeNS/1000000000)