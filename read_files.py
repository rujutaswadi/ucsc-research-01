import csv as c

def read_black_file():
    with open("/Users/rujuta/Desktop/research_project/black_names_sample.csv") as black_names:
        name_reader = c.reader(black_names)

        names = []

        to_be_corrected = []
        valid = []

        for row in name_reader:

            if len(row) < 2:
                to_be_corrected.append(row)
            else:
                valid.append(row)

        for valid_row in valid: #only go through the rows with proper formatting
            full_name = valid_row[0]

            full_name = full_name.replace("  ", " ") #changes all double spaces to a single space (but doesn't handle case for more than a double space)

            first_space_pos = full_name.index(' ')
            last_name = full_name[0:first_space_pos]

            second_space_pos = full_name.find(' ',first_space_pos+1)
            if second_space_pos == -1:
                first_name = full_name[first_space_pos:] #to catch the last letter of the name
            else:
                first_name = full_name[first_space_pos:second_space_pos]

            if len(valid_row) < 3: #it means it's missing either occupation or address
                house_pos = valid_row[1].find('h ')
                if house_pos == -1:
                    occupation = valid_row[1]
                    address = ''
                else:
                    occupation = ''
                    address = valid_row[1]
            else: #not missing any elements
                occupation = valid_row[1]
                address = valid_row[2]

            output_row = []


            #output_row.append(last_name)
            #output_row.append(first_name)
            
            
            if len(first_name) > 2:
                output_row.append(last_name)
                output_row.append(first_name)
                #print(first_name)
                names.append(output_row)


            
        
    return names #all first and last names for black people

def read_white_file():
    with open("/Users/rujuta/Desktop/research_project/white_names_sample.csv") as white_names:
        name_reader = c.reader(white_names)

        names = []

        to_be_corrected = []
        valid = []

        for row in name_reader:

            if len(row) < 2:
                to_be_corrected.append(row)
            else:
                valid.append(row)
        
        for valid_row in valid: #only go through names with proper formatting

            #print(valid_row)
            
            full_name = valid_row[0]

            full_name = full_name.replace("  ", " ") #changes all double spaces to a single space (but doesn't handle case for more than a double space)

            first_space_pos = full_name.index(' ')
            last_name = full_name[0:first_space_pos]
            
            second_space_pos = full_name.find(' ',first_space_pos+1)
            if second_space_pos == -1:
                first_name = full_name[first_space_pos:] #to catch the last letter of the name
            else:
                first_name = full_name[first_space_pos:second_space_pos]

            if len(valid_row) < 3: #it means it's missing either occupation or address
                house_pos = valid_row[1].find('h ')
                if house_pos == -1:
                    occupation = valid_row[1]
                    address = ''
                else:
                    occupation = ''
                    address = valid_row[1]
            else: #not missing any elements
                occupation = valid_row[1]
                address = valid_row[2]
            
            #print(last_name)
            #print(first_name)

            output_row = []

            #output_row.append(last_name)
            #output_row.append(first_name)

            if len(first_name) > 2:
                output_row.append(last_name)
                output_row.append(first_name)
                names.append(output_row)
        
    return names #all first and last names for white people