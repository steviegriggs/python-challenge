import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    poll_data = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first 
    csv_header = next(poll_data)


   
    candidate_list = []
    candidate_votes = []
    tot_votes=0
    for x in poll_data:
        if str(x[2]) not in candidate_list:
            candidate_list.append(str(x[2]))
            candidate_votes.append(1)
            tot_votes += 1
        else:
            for y in candidate_list:
                if str(x[2]) == y:
                    candidate_votes[candidate_list.index(y)] = candidate_votes[candidate_list.index(y)] + 1
                    tot_votes += 1
            
        
    prcnt = []
    for x in candidate_votes:
        prcnt.append(((x/tot_votes)*100))

    win = 0
    windex = 0
    for x in candidate_votes:
        if x > win:
            win = x
            windex = candidate_votes.index(x)
    
    p_print = []

    p_print.append("Election results")
    p_print.append("-------------------------")
    p_print.append(f"Total Votes: {tot_votes}")
    p_print.append("-------------------------")
    
    i = 0
    while i < len(candidate_list):   
        p_print.append("{}: {}% ({:,})".format(
            candidate_list[i], round(prcnt[i],4), candidate_votes[i]))
        i += 1
    
    p_print.append("-------------------------")
    p_print.append(f"Winner: {candidate_list[windex]}")
    
    poll_txt= open("election_results.txt","w+")
    for x in p_print:
        print(x)
        print(x, file = poll_txt)
    poll_txt.close
    
    
    
    