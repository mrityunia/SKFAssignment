# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --

# To Do ::- will store all the constraints deatls and locator
import os

app_url = "https://www.skfbearingselect.com"
browsers_name = ("chrome", "chromeheadless", "firefox")



def SOLUTION_DICTIONARY():
	print("SOLUTION_DICTIONARY is {}".format(os.getcwd()))
	return os.getcwd()

chrome_path=SOLUTION_DICTIONARY()+"//testdata//chromedriver.exe"
firefox_path=SOLUTION_DICTIONARY()+"//testdata//geckodriver.exe"

accept_continue="button.button-default"
single_image="img.single-bearing"
select_bearing_type="//span[text()='Select bearing type']"
single_bearing_dropdown='div.bearing-type-select>mat-select>div>div.mat-select-arrow-wrapper>div'
single_bearing_options_first='mat-option-12'
single_bearing_optiosn="//mat-option[@role='option']/span/span"
search_designation="div.searchbox>input"
designation_deatils="(//mat-row[@role='row']/mat-cell[7])[1]"
next_button_skf="//button[text()='next']"
