##this script will analysis election data
import csv
import operator
import collections


with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    file_header = next(csvreader)
     
    total_line_count = 0
    
    candidate = collections.Counter()
    
    sort = sorted (csvreader,key=operator.itemgetter(2))
    
    for c, row in enumerate(sort):
        
#counts total number of votes
        total_line_count = total_line_count + 1
        
#counts votes for each candidate        
        candidate[row[2]] += 1
        
print("Total Votes: " + str(total_line_count))
print("------------------------------------")
        
from collections import Counter

#the newlist is a list that contains name of candiate and total votes
newlist = Counter(candidate)
#creating new list 
numlist=[]
namelist=[]
output_list=[]


for name, total_votes in newlist.items():
       
#percentage of votes each candidate 

    percent_vote = (total_votes / total_line_count) * 100
    
#takes the total_votes value and appends to numlist

    numlist.append(total_votes)
    
#takes the name and appends to namelist

    namelist.append(name)
    
#concatenates the name,%of votes, and total_votes   

    output_data=(name + ": " + "%.2f%%" %  (percent_vote)+ " " + "(" + str(total_votes) + ")")

#the result of the cancatenation is placed into a output_list

    output_list.append(output_data)
    
#finds a winner by calculating the max number within the numlist 

winner = max(numlist)

#finds the winner's index number in the numlist to later refrence the candiate name from namelist
max_index = numlist.index(winner)

for name in output_list:
    print (name)
print("--------------------------------")
print("winner: " + namelist[max_index])

#writes a txt file with the scripts output

results = open("pypoll_output.txt","w")

results.write("\nTotal Votes: " + str(total_line_count))
results.write("\n------------------------------------")
results.write("\n" + output_list[0])
results.write("\n" + output_list[1])
results.write("\n" + output_list[2])
results.write("\n" + output_list[3])
results.write("\n--------------------------------")
results.write("\nwinner: " + namelist[max_index])

results.close()

    