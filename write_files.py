import csv as c, read_files as rf

def write_black_names():
    with open ('/Users/rujuta/Desktop/research_project/black_names_samples_output.csv', 'w', newline='') as output:
        names = rf.read_black_file()
        
        writer = c.writer(output)

        writer.writerow(['last_name', 'first_name'])

        writer.writerows(names)

def write_white_names():
    with open ('/Users/rujuta/Desktop/research_project/white_names_samples_output.csv', 'w', newline='') as output:
       names = rf.read_white_file()
       
       writer = c.writer(output)
       
       writer.writerow(['last_name', 'first_name'])
       
       writer.writerows(names)
            
        #print(names)