
import csv

def CSVtoList(Filename):
    output = []

    with open(Filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            output += [row]
    return output



man_vs_coast_runners = CSVtoList("ManVsCoast.csv")
#print (man_vs_coast_runners)

the_wall_runners = CSVtoList("TheWall.csv")
#print (the_wall_runners)


match_list =[]
for man_vs_coast_runner in man_vs_coast_runners:
    man_vs_coast_runner_name = man_vs_coast_runner[1] + " " + man_vs_coast_runner[2]
    man_vs_coast_runner_name = man_vs_coast_runner_name.upper()

    for the_wall_runner in the_wall_runners:
        the_wall_runner_name = the_wall_runner[2] +" "+ the_wall_runner[1]
        the_wall_runner_name = the_wall_runner_name.upper()

        if the_wall_runner_name == man_vs_coast_runner_name :
            #print ("Match")
            #print (the_wall_runner_name,"," "Wall Time : ,", the_wall_runner[3] ,",", "Coast Time : ,", man_vs_coast_runner[3])
            print ("| ",the_wall_runner_name,"| ",the_wall_runner[3], "| ", man_vs_coast_runner[3], "|" )



