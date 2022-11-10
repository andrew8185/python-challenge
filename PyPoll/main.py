import os
import csv

#create an empty dictionary for candidates
candidates = {}

#define initial variable values
total_votes = 0
most_votes_count = 0
most_votes_candidate = ""


csvpath = os.path.join("Resources", "election_data.csv")

#open csv
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #create a loop through the csv file
    for row in csvreader:
        
        #set candidate_name variable as the column of candidates from the csv
        candidate_name = row[2]
        
        #for each loop of the rows in the csv file add 1 to the total_votes variable
        total_votes = total_votes + 1
    
        #insert the candidate names into the dictionary. For each unique candiate name found add it
        #to the dictionary as a key with a starting value of 1. If it already exists increase the value by 1
        if candidate_name in candidates:
            candidates[candidate_name] = candidates[candidate_name] + 1
        else:
            candidates[candidate_name] = 1


#create a new txt value to hold outputs as well as print to terminal
save_to = os.path.join("Resources", "election_results.txt")
with open(save_to, 'w') as txt_file:
    output = "Election Results\n----------------------------------------\n"
    print(output)
    txt_file.write(output)
    #set the output variable to print the total votes
    output = "Total Votes: " + str(total_votes) +"\n----------------------------------------\n"
    print(output)
    txt_file.write(output)
    
    #set up a for loop to loop through the condidates dictionary created above
    for candidate_name, candidate_votes in candidates.items():
        #if function where each candidate's vote is compared to the most votes candidate variable (starts at 0) and if the candidate's vote is
        #larger that the most votes variable, set the candidate's votes as the most votes variable
        if candidate_votes > most_votes_count:
            most_votes_candidate = candidate_name
            most_votes_count = candidate_votes
        #set then print the candidate's vote as a percentage
        candidates_percent = round((candidate_votes/total_votes)*100,3)
        output = candidate_name + ":" + str(candidates_percent) + '% ' + '(' + str(candidate_votes) + ')'
        print(output)
        txt_file.write(output + '\n')
  
    #print the winner
    print(f'----------------------------------------\nWinner: {most_votes_candidate}\n----------------------------------------')
    txt_file.write(f'----------------------------------------\nWinner: {most_votes_candidate}\n----------------------------------------')
