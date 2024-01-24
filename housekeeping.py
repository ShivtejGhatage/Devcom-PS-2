import os

def make_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_data_files(dev_id):
    
    recorded = dev_id + '.txt'
    
    if not os.path.isfile(recorded):
        write_file(recorded, '')

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data )
    



