import csv
import time

def CSVtoList(Filename):
    output = []

    with open(Filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            output += [row]
    return output

def SumTime(timeList):
    totalSecs = 0
    for tm in timeList:
        timeParts = [int(s) for s in tm.split(':')]
        totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
    totalSecs, sec = divmod(totalSecs, 60)
    hr, min = divmod(totalSecs, 60)
    Time = "%d:%02d:%02d" % (hr, min, sec)
    return (Time)


#Get the RatRace Runners Results.
man_vs_coast_runners = CSVtoList("./RawFiles/ManVsCoast.csv")
man_vs_lakes_runners = CSVtoList("./RawFiles/ManVsLakes.csv")
man_vs_mountain_runners = CSVtoList("./RawFiles/ManVsMountain.csv")

match_list =[]

#Set the Start Time.
start_time = time.time()

#Start Iterating through the Coast Runners.
for man_vs_coast_runner in man_vs_coast_runners:
    #Get the Coast Runners Name - To Upper Case, and then store it temporarily.
    #This helps with Readability.
    man_vs_coast_runner_name = str(man_vs_coast_runner[1].upper()) +" " + str(man_vs_coast_runner[2].upper())

    #Start Iterating through the next Man Vs Lakes Results List.
    for man_vs_lakes_runner in man_vs_lakes_runners:
        man_vs_lakes_runner_name = str(man_vs_lakes_runner[1].upper()) + " " + str(man_vs_lakes_runner[2].upper())

        #If the Coast Runner is not the Lakes Runner, Do nothing more, and go to the next contestant.
        #However, If we have the same name for Coast, and Lakes, Run through all Mountain runners, and look for a match.
        if (man_vs_coast_runner_name == man_vs_lakes_runner_name):
            for man_vs_mountain_runner in man_vs_mountain_runners:
                man_vs_mountain_runner_name = str(man_vs_mountain_runner[1].upper()) + " " + str(man_vs_mountain_runner[2].upper())

                if (man_vs_coast_runner_name == man_vs_lakes_runner_name ==man_vs_mountain_runner_name ):
                    #If there is a match, Then add this to the Match List.
                    name = man_vs_coast_runner_name
                    man_vs_coast_time = "Coast : " + str( man_vs_coast_runner[5] ) +" "
                    man_vs_lakes_time = "Lakes : "+ str(man_vs_lakes_runner[5]) +" "
                    man_vs_mountain_time = "Mountain : " +str(man_vs_mountain_runner[5]) +" "
                    try:
                        man_vs_total_time = SumTime ([man_vs_coast_runner[5], man_vs_lakes_runner[5],man_vs_mountain_runner[5]])
                    except:
                        #print("Maybe this Person DNF'd")
                        #print([man_vs_coast_runner[5], man_vs_lakes_runner[5], man_vs_mountain_runner[5]])
                        man_vs_total_time = "Unknown"
                    report_string = str(name) + str(man_vs_lakes_time) + str(man_vs_coast_time) + str(man_vs_mountain_time) + "Man Vs Total Time :" + man_vs_total_time

                    match_list += [report_string]

#Wrapup: Print the Match List, and then the total number of entries.
for person in match_list:
    print(person)
print(len(match_list))

print("--- %s seconds ---" % (time.time() - start_time))
