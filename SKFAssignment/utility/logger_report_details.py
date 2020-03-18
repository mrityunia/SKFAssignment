# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --

# To Do ::- this will initiate logger and Test Reports for testing

from utility.constraints_locator_details import *
import logging

logger_path = SOLUTION_DICTIONARY() + "//testdata//testlogs.log"
print(logger_path)
if os.path.exists(logger_path):
	os.remove(logger_path)
	open(logger_path, 'w')
	logging.basicConfig(filename=logger_path, format='%(asctime)s: %(module)s: %(funcName)s: '
	                                                 '%(lineno)d=> %(message)s', datefmt='%d- %I:%M')
else:
	open(logger_path, 'w')
	logging.basicConfig(filename=logger_path, format='%(asctime)s:%(module)s: %(funcName)s: '
	                                                 '%(lineno)d=>   %(message)s', datefmt='%d- %I:%M')


def start_logger():
	logging.debug("Logger is initiated ")