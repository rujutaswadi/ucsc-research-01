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

def get_black_occurences():
    all_black_first_names = []
    black_counts = {}

    names = read_black_file()

    for name in names:
        #print(name[1])
        all_black_first_names.append(name[1])
    
    for f in all_black_first_names:
        #print(f, all_black_first_names.count(f))
    
        black_counts[f] = all_black_first_names.count(f)
    
    #print(black_counts)

    return black_counts #each black name and how many time it occurs


def write_black_names():
    with open ('/Users/rujuta/Desktop/research_project/black_names_samples_output.csv', 'w', newline='') as output:
        names = read_black_file()
        
        writer = c.writer(output)

        writer.writerow(['last_name', 'first_name'])

        writer.writerows(names)
    
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

def get_white_occurences():
    all_white_first_names = []
    white_counts = {}

    names = read_white_file()

    for name in names:
        all_white_first_names.append(name[1])
    
    for f in all_white_first_names:
        #print(f, all_white_first_names.count(f))
    
        white_counts[f] = all_white_first_names.count(f)
    
    return white_counts #each white name and how many time it appears
    #print(white_counts)

def write_white_names():
    with open ('/Users/rujuta/Desktop/research_project/white_names_samples_output.csv', 'w', newline='') as output:
       names = read_white_file()
       
       writer = c.writer(output)
       
       writer.writerow(['last_name', 'first_name'])
       
       writer.writerows(names)
            
        #print(names)


def calculations(black_occurences, white_occurences):
    unique_names = []
    black_names = black_occurences.keys()
    white_names = white_occurences.keys()

    for name in black_names:
        unique_names.append(name)
    for name in white_names:
        if name in unique_names == False: #can i say if not key in unique_names?
            unique_names.append(name)
    
    statistics = {}

    for name in unique_names:
        if name in black_names:
            black_count = black_occurences[name]
        else:
            black_count = 0
        if name in white_names:
            white_count = white_occurences[name]
        else:
            white_count = 0 
        
        statistics[name] = (black_count) / (black_count + white_count)
    
    return statistics

def read_stats():
    black_counts = get_black_occurences()
    white_counts = get_white_occurences()

    statistics = calculations(black_counts, white_counts)

    stats = []


    for key in statistics.keys():
        output_row = []
        output_row.append(key)
        output_row.append(statistics[key])
        stats.append(output_row)
        #print("name: ", key, statistics[key])

    
    #print(stats)
    return stats



def write_statistics():
    with open ('/Users/rujuta/Desktop/research_project/statistics.csv', 'w', newline='') as output:
        stats = read_stats()

        writer = c.writer(output)

        writer.writerow(['name', 'black_percentage'])

        writer.writerows(stats)

write_statistics()
