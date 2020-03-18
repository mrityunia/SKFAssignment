# Created by ********  chomri01 at 3/12/2020

# Feature Name :: --

# To Do ::-
import threading

from utility.constraints_locator_details import *
from selenium.webdriver.common.by import By
from utility.web_element_helpper import *


class SKFHomePage(BasePage):
	def __init__(self, context):
		BasePage.__init__(
			self,
			context.Browser
		)
		self.element_helper = WebHelpper(context=context)
		pass

	location_directory = {
		"accept_continue": (By.CSS_SELECTOR, accept_continue)
	}

	def open_application(self):
		try:
			self.Browser.get(app_url)
			logging.info("{} application is opened ".format(str(app_url)))
			self.Browser.maximize_window()
			return True
		except:
			logging.error("Some error occurred at open application {} ".format(sys.exc_info()))
			return False

	def accept_privacy(self):
		is_accepted = False
		try:
			logging.info("Inserting into Accept Privacy ")
			if self.element_helper.we_display_element(*self.location_directory['accept_continue'], timeout=30):
				logging.info("Accept and Continue button is not displaying")
				self.element_helper.we_click(*self.location_directory['accept_continue'])
				logging.info("Clicked on Accept and Continue")
				is_accepted = True
			elif str(self.Browser.current_url).__contains__("one-or-two"):
				logging.info("already accepted")
				isaccepted = True
		except:
			logging.error("some error in accept_privacy() " + str(sys.exc_info()))
			pass
		return is_accepted


class SKFBearing(BasePage):
	def __init__(self, context):
		BasePage.__init__(
			self,
			context.Browser
		)
		self.element_helper = WebHelpper(context=context)
		pass

	location_directory = {
		"single_image": (By.CSS_SELECTOR, single_image),
		"select_single_bearing": (By.XPATH, select_bearing_type),
		"single_bearing_dropdown": (By.CSS_SELECTOR, single_bearing_dropdown),
		"single_bearing_options_first": (By.ID, single_bearing_options_first),
		"single_bearing_optiosn": (By.XPATH, single_bearing_optiosn),
		"blank__space": (By.XPATH, "//body"),
		"search_designation": (By.CSS_SELECTOR, search_designation),
		"designation_details": (By.XPATH, designation_deatils),
		"next_button": (By.XPATH, next_button_skf)
	}

	def select_single_immage(self):
		try:
			logging.info("Inserting into select_select_image")
			if self.element_helper.we_display_element(*self.location_directory['single_image'], timeout=30):
				logging.info("Single bearing is displaying")
				self.element_helper.we_click(*self.location_directory['single_image'])
				logging.info("clicked on single bearing element")
				if self.element_helper.we_display_element(*self.location_directory['select_single_bearing'],
				                                          timeout=30):
					logging.info("Single bearing options is showing")
					return True
		except:
			logging.error("some error occurred at " + str(sys.exc_info()))
			pass
		pass

	def click_single_bearing_dropdown(self):
		try:
			logging.info("clicking on single drop down")
			self.element_helper.we_click(*self.location_directory["single_bearing_dropdown"])
			self.element_helper.wait_to_load(*self.location_directory["single_bearing_options_first"])
			logging.info("Single Options are loaded")
			if self.element_helper.we_display_element(*self.location_directory["single_bearing_options_first"],
			                                          timeout=30):
				logging.info("Single bearing option are present ")
				return True
		except:
			logging.error("some error occured at click_single_bearing_dropdown => " + str(sys.exc_info()))

	def get_all_single_bearing_options(self):
		try:
			logging.info("Inserting into Get all the single bearing options")
			options = self.element_helper.we_find_elements(*self.location_directory["single_bearing_optiosn"])
			option_text = []
			if options is not None:
				logging.info("Total number of option is " + str(len(options)))
				for opt in options:
					option_text.append(opt.text)
				logging.info("bearing options are " + str(option_text))
			else:
				logging.info("Bearing options is None")
			return option_text
		except:
			logging.error("Some error occurred " + str(sys.exc_info()))
			return None

	def clicking_blank_space(self):
		try:
			bln = self.element_helper.we_click(*self.location_directory["blank__space"])
			logging.info("Clicked on blank element in the page")
		except:
			logging.error("Some error occurred " + str(sys.exc_info()))

	def selecting_single_bearing(self, bearing_name):
		is_selected = False
		try:
			logging.info("bearing option will be selecting is " + str(bearing_name))
			all_bearing = self.element_helper.we_find_elements(*self.location_directory["single_bearing_optiosn"])
			logging.info("done")
			if all_bearing is not None:
				logging.info("total number of bearing options is " + str(len(all_bearing)))
				for opt in all_bearing:
					if opt.text == bearing_name:
						opt.click()
						logging.info("clicked on {0} bearing option ".format(str(bearing_name)))
						is_selected = True
						break
					else:
						logging.info("Bearing name is {} ".format(str(opt.text)))

			else:
				logging.error("bearing options are not showing ")
		except:
			logging.error("Some error occurred at selecting_single_bearing " + str(sys.exc_info()))
		return is_selected

	def enter_designation(self, designation):
		is_entered = False
		try:
			self.element_helper.we_scroll_to_element(*self.location_directory["search_designation"])
			self.element_helper.we_send_keys(*self.location_directory["search_designation"], data=designation)
			import time
			time.sleep(3)
			for i in range(0, 10):
				des = self.element_helper.we_find_element(*self.location_directory["designation_details"]).text
				if des == designation:
					logging.info("Able to find the {} designation ")
					is_entered = True
					break
				else:
					logging.info("waiting to load {} ".format(str(designation)))
					import time
					time.sleep(60)
			logging.info("{0} to be entered in search designation ".format(str(designation)))
		except:
			logging.error("Some error occurred at selecting_single_bearing " + str(sys.exc_info()))
		return is_entered

	def select_designation(self, designation):
		try:
			self.element_helper.we_click(*self.location_directory["designation_details"])
			logging.info("{} designation is selected ")
			return True
		except:
			logging.error("Some error occurred at selecting_single_bearing " + str(sys.exc_info()))
			return False

	def get_next_button_attribute(self):
		try:
			logging.info("Inserting into next button attribute verification")
			self.element_helper.we_display_element(*self.location_directory["next_button"])
			att = self.element_helper.we_find_element(*self.location_directory["next_button"]).get_attribute("class")
			if att == "button-default":
				return True
			else:
				logging.error("Attribute is not button-default ")
				return False
		except:
			logging.error("Some error occurred at selecting_single_bearing " + str(sys.exc_info()))
			return False
