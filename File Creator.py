suffix = 'user_defined'                                     			# declare the suffix to add

with open(raw_input("Enter Filename: "), 'r') as inF:           		# open user selected input file as context
    with open('map.csv', 'w') as f:                             		# open output file to write to as context
        for row in inF.readlines():                             		# iterate through each row that Python has read through
            token = row.strip()                                 		# save the original row value as the token for config
            for skill in token.split(";") :                     		# split each token by delimiter
            #    print(token + "," + skill + ","  + suffix)    			# DIAGNOSTIC print display before write to file
                f.write(token + "," + skill + ","  + suffix + '\n')  	# save to file
                                                                		# alternative option: append to a variable, then write to file
                                                                		# probably would be good to screen for lines that have commas in the future