from model import *
import logging
import datetime
import time

time.sleep(20)

# Logging config
logging.basicConfig(filename='info.log',level=logging.DEBUG)
logging.info('Started at ' + str(datetime.datetime.now()))

# model_it(pre, method, dim_reduct=-1, ensemble=-1)

# Preprocessing - Method combinations
for pre in range(2):
    for method in range(5):
        try:
            model_it(pre, method)
            logging.info('Success_1: ' + str(pre) + '-' + str(method) + '\t' + str(datetime.datetime.now()))
        except Exception, e:
            logging.info('Failed_1: ' + str(pre) + '-' + str(method) + '\t' + str(e) + ' ' + str(datetime.datetime.now()))

# Preprocessing - Dimension reduction - Method combinations
for pre  in range(2):
    for method in range(5):
        try:
            model_it(pre, method, 0)
            logging.info('Success_2: ' + str(pre) + '-' + str(method) + '\t' + str(datetime.datetime.now()))
        except Exception, e:
            logging.info('Failed_2: ' + str(pre) + '-' + str(method) + '\t' + str(e) + ' ' + str(datetime.datetime.now()))

# Preprocessing - Ensemble Method combinations
for pre in range(2):
    for ensemble in range(2):
        try:
            model_it(pre, 0, -1, ensemble)
            logging.info('Success_3: ' + str(pre) + '-' + str(ensemble) + '\t' + str(datetime.datetime.now()))
        except Exception, e:
            logging.info('Failed_3: ' + str(pre) + '-' + str(ensemble) + '\t' + str(e) + ' ' + str(datetime.datetime.now()))

# Preprocessing - Dimension reduction - Ensemble Method combinations
for pre in range(2):
    for ensemble in range(2):
        try:
            model_it(pre, 0, 0, ensemble)
            logging.info('Success_4: ' + str(pre) + '-' + str(ensemble) + '\t' + str(datetime.datetime.now()))
        except Exception, e:
            logging.info('Failed_4: ' + str(pre) + '-' + str(ensemble) + '\t' + str(e) + ' ' + str(datetime.datetime.now()))
