import os 

cs_files = os.listdir('CollegeScorecard')

## Check if all of the files have the same header
header = False # Variable assignment - boolean type

for filename in cs_files: 
    loc = 'CollegeScorecard/' + filename 
    
    with open(loc,'r') as file: # an idiom for openning files in read mode
        headline = file.readline() # read the first line

    if header: # if statement
        if header != headline: # does the header of this file differ?
            print('header differs for ' + filename)
    
        else: # if it does not differ
            print(filename + ' passes')
            
    else: # if we are at the first file
        header = headline
