# # Netflix lookup

# Finding the info to some of netlfix's most popular videos

# ## Instructions

# import the modules 

import os 
import csv 

# Prompt the user for what video they are looking for.

user_input = input("What movie you are looking for? ")

# file path
csv_path = os.path.join('resources', 'netflix_ratings.csv')

# if the movie is not found 
found = False 

# open and read the file 
with open(csv_path, newline = '') as csvfile:
    
    # read the file 
    read_csv = csv.reader(csvfile, delimiter = ',')

    # run the for loop for each row 
    for row in read_csv:
        
        # set up the conditions
        # Search through the `netflix_ratings.csv` to find the user's video.
        if row[0] == user_input:
            
            # if the CSV contains the user's video then print out the title, what it is rated and the current user ratings.

            print(f"{row[0]} is rated {row[1]} with a rating of {row[6]}")

            found = True 
    if not found:

        # If the CSV does not contain the user's video then print out a message telling them that their video could not be found.
        print(f"the movie: {user_input} is not in this Netflix list. Look up for another movie.")





