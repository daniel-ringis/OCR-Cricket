# Python program to read CSV file line by line
# import necessary packages
import csv
f = open("summary.csv", "w")
# Open file
with open('scorecard.csv') as file_obj:
    reader_obj = csv.reader(file_obj, delimiter=',')
    previous_score = 0
    previous_wicket = 0
# Iterate over each row in the csv
# file using reader object
    for row in reader_obj:
        if(len(row) == 2):
            curr = row[1]
            if "-" in curr:
                scoreboard = curr.split('-')
                timestamp = row[0] 
                current_score = scoreboard[0]
                current_wicket = scoreboard[1]
            #print(timestamp, current_score, current_wicket)
                if(current_score.isnumeric() & current_wicket.isnumeric()):
                    if(current_score != previous_score):
                        #print((int(current_score) - int(previous_score)), "Runs Scored at", timestamp)
                        if((int(current_score) - int(previous_score)) == 4):
                            f = open("summary.csv", "a")
                            f.write("Four Runs Scored at "+timestamp+"\n")
                            f.close()
                        if((int(current_score) - int(previous_score)) == 6):
                            f = open("summary.csv", "a")
                            f.write("Six Runs Scored at "+timestamp+"\n")   
                            f.close()                         
                        previous_score = current_score
                    if(int(current_wicket) != int(previous_wicket)):
                        f = open("summary.csv", "a")
                        f.write(current_wicket+"Wicket Taken at "+timestamp+"\n")
                        f.close() 
                        previous_wicket = current_wicket
            
            
