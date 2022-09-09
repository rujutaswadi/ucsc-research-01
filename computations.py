import read_files as rf

def get_black_occurences():
    all_black_first_names = []
    black_counts = {}

    names = rf.read_black_file()

    for name in names:
        #print(name[1])
        all_black_first_names.append(name[1])
    
    for f in all_black_first_names:
        #print(f, all_black_first_names.count(f))
    
        black_counts[f] = all_black_first_names.count(f)
    

    #print(black_counts)

    return black_counts #each black name and how many time it occurs

def get_white_occurences():
    all_white_first_names = []
    white_counts = {}

    names = rf.read_white_file()

    for name in names:
        all_white_first_names.append(name[1])
    
    for f in all_white_first_names:
        #print(f, all_white_first_names.count(f))
    
        white_counts[f] = all_white_first_names.count(f)
    
    return white_counts #each white name and how many time it appears
    #print(white_counts)