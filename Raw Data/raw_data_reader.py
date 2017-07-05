import pickle

def read_raw_data(pickle_file='raw_data.p', print_it=False):
    '''
    Reads a raw pickle file and returns the data. Can also print it
    '''
    # Load pickle file
    raw_data = pickle.load(open(pickle_file,'rb'))

    if print_it:
        print raw_data

    return raw_data

if __name__ == '__main__':
	read_raw_data(print_it=True)
