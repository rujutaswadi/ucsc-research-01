import csv as c, computations as comp

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
    black_counts = comp.get_black_occurences()
    white_counts = comp.get_white_occurences()

    statistics = calculations(black_counts, white_counts)

    stats = []

    for key in statistics.keys():
        output_row = []
        output_row.append(key)
        output_row.append(statistics[key])
        output_row.append(1-statistics[key])
        stats.append(output_row)
        #print("name: ", key, statistics[key])

    
    #print(stats)
    return stats



def write_statistics():
    with open ('/Users/rujuta/Desktop/research_project/statistics.csv', 'w', newline='') as output:
        stats = read_stats()

        writer = c.writer(output)

        writer.writerow(['name', 'black_percentage', 'white_percentage'])

        writer.writerows(stats)