#by Rujuta Swadi (2022)

import csv as c, computations as comp

def calculations(black_occurences, white_occurences):
    unique_names = []
    black_names = black_occurences.keys()
    white_names = white_occurences.keys()

    for b_name in black_names:
        unique_names.append(b_name)
    for w_name in white_names:
        if w_name not in unique_names:
            #print(w_name)
            unique_names.append(w_name)
    
    black_percentage = {}
    x_axis = {}
    total_people = 0

    for name in unique_names:
        if name in black_names:
            black_count = black_occurences[name]
        else:
            black_count = 0
        if name in white_names:
            white_count = white_occurences[name]
        else:
            white_count = 0 
        
        black_percentage[name] = (black_count) / (black_count + white_count)
        
        
        x_axis[name] = black_count / (black_count + white_count) #AA name/people with that name
    
        total_people = total_people + black_count + white_count

    y_axis = {}
    #print(total_people)

    for name in unique_names:
        if name in black_names:
            black_count = black_occurences[name]
        else:
            black_count = 0
        if name in white_names:
            white_count = white_occurences[name]
        else:
            white_count = 0

        y_axis[name] = (black_count + white_count) / total_people #frequency
    
    #return black_percentage #add x axis, add y axis
    return unique_names, black_percentage, x_axis, y_axis

def read_stats():
    black_counts = comp.get_black_occurences()
    white_counts = comp.get_white_occurences()

    unique_names, black_percentage, x_axis, y_axis = calculations(black_counts, white_counts)
    

    stats = []

    for name in unique_names:
        #print(name)
        output_row = []

        output_row.append(name)
        output_row.append(black_percentage[name])
        output_row.append(x_axis[name])
        output_row.append(y_axis[name])

        stats.append(output_row)

    
    #print(stats)
    return stats



def write_statistics():
    read_stats()


    with open ('statistics.csv', 'w', newline='') as output:
        stats = read_stats()

        writer = c.writer(output)

        writer.writerow(['name', 'black_percentage', 'x_axis', 'y_axis'])

        writer.writerows(stats)
        