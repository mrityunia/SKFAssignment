# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --

# To Do ::-

from utility.driver_details import *
from utility.logger_report_details import *
def before_feature(context, scenario):
	start_logger()
	logging.info("Starting Feature name is {}".format(str(scenario.name)))
	pass
def before_scenario(context, scenario):
	logging.info("Starting scenario ---------")
	global browser
	for tag in scenario.tags:
		if str(tag).lower() in browsers_name:
			browser = tag
			break
	if str(browser).lower() == "chrome":
		context.Browser = get_chrome_driver()
	elif str(browser).lower() == "firefox":
		context.Browser = get_firefox_driver()
	else:
		logging.info("Initiating default Chrome Driver ")
		context.Browser = get_chrome_driver()
	pass
def after_scenario(context, scenario):
	logging.info("End of Scenario ------")
	if "debug" not in scenario.tags:
		context.Browser.quit()
		pass

def before_step(context, step):
	logging.info("Starting steps is {} ".format(str(step.name)))
