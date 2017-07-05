import pickle

def create_raw_data_file(pickle_file='raw_data.p'):
    '''
    Creates a new pickle file with an empy list
    '''
    raw_data = []
    pickle.dump(raw_data, open(pickle_file, 'wb'))
    return

if __name__ == '__main__':
	create_raw_data_file()
