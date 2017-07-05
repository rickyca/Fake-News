import pickle
from raw_data_reader import read_raw_data
from webhose_api import get_raw_data_api

def get_raw_data():
    '''
    Gets Data from an API and returns it
    '''
    # Get data from API
    posts = get_raw_data_api()
    #posts = raw_input()
    return posts

def pull_data(pickle_file='raw_data.p'):
    '''
    Pulls raw data, appends it to old pickled raw data, and stores the updated raw data
    '''
    # Open pickle file and asign its value to raw_data
    raw_data = read_raw_data(pickle_file='raw_data.p', print_it=False)
    # Get new raw data and append it to old data
    raw_data.append(get_raw_data())
    # Save new raw data
    pickle.dump(raw_data, open(pickle_file, 'wb'))
    return

if __name__ == '__main__':
	pull_data()
