import csv

def CSVtoList(Filename):
    output = []

    with open(Filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            output += [row]
    return output

man_vs_coast_runners = CSVtoList("./RawFiles/ManVsCoast.csv")
man_vs_lakes_runners = CSVtoList("./RawFiles/ManVsLakes.csv")
man_vs_mountain_runners = CSVtoList("./RawFiles/ManVsMountain.csv")


match_list =[]

a = 0

import time
start_time = time.time()

for man_vs_coast_runner in man_vs_coast_runners:
    man_vs_coast_runner_name = str(man_vs_coast_runner[1].upper()) +" " + str(man_vs_coast_runner[2].upper())
    for man_vs_lakes_runner in man_vs_lakes_runners:
        man_vs_lakes_runner_name = str(man_vs_lakes_runner[1].upper()) + " " + str(man_vs_lakes_runner[2].upper())
        if (man_vs_coast_runner_name == man_vs_lakes_runner_name):
            for man_vs_mountain_runner in man_vs_mountain_runners:
                man_vs_mountain_runner_name = str(man_vs_mountain_runner[1].upper()) + " " + str(man_vs_mountain_runner[2].upper())
                if (man_vs_coast_runner_name == man_vs_lakes_runner_name ==man_vs_mountain_runner_name ):
                    match_list += [man_vs_coast_runner_name]
print(match_list)

print("--- %s seconds ---" % (time.time() - start_time))
