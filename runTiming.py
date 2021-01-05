def runTime():
    """Gets the number of times one runs 10kms and finds the average time taken"""
    total_time = 0
    count = 0
    entries = int(input("Enter the number of runs you have so far: "))
    for minute in range(0, entries):
        minute = int(input("Enter 10 km run time in mins: "))
        total_time += float(minute)
        count += 1
    average_t = total_time/entries
    print(f"Average of {average_t} minutes over {entries} runs")

runTime()