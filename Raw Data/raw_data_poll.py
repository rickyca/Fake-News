import datetime
import time
import logging
from raw_data_pull import pull_data

def poll_data(t=1):
    '''
    Polls data at times t hours intervals
    '''
    # Logging config
    logging.basicConfig(filename='pull.log',level=logging.DEBUG)
    # Iniciates last time
    last_time = datetime.datetime.now() - datetime.timedelta(hours=t)

    try:
        while True:
            # Get current time
            current_time = datetime.datetime.now()
            # Difference in time
            diff_time = current_time - last_time
            # If requested time has passed pull data
            if diff_time.seconds/60. >= t*60:
                #print "Pulling data"
		logging.info('Pulling data: ' + str(current_time))
                pull_data()
                # Update last_time
                last_time = current_time

            time.sleep(2)
    except KeyboardInterrupt:
        print "User Interruption"
    return

if __name__ == '__main__':
	poll_data()
