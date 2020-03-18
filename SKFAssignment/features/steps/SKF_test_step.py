# Created by ********  chomri01 at 3/12/2020

# Feature Name :: --

# To Do ::-
from behave import given, when, then
from pages.skf_page import *

@given(u'the user launch the application')
def step_impl(context):
    global sfk_home
    sfk_home=SKFHomePage(context)
    assert True is sfk_home.open_application(),"Not able to open SKF application"
    pass
@given(u'‘Accept & continue’ if displayed')
def step_impl(context):
    assert True is sfk_home.accept_privacy(),"Not able to Accept and Continue button "
    pass

@when(u'the user clicks on ‘Single Bearing’ image')
def step_impl(context):
    global skf_single_bearing
    skf_single_bearing=SKFBearing(context)
    assert True is skf_single_bearing.select_single_immage(),"Not able to select Single bearing option"
    pass

@when(u'Clicks on Select bearing type dropdown')
def step_impl(context):

    assert True is skf_single_bearing.click_single_bearing_dropdown(),"Not able to click dropdown"

@then(u'verify the following options are present')
def step_impl(context):
    options = skf_single_bearing.get_all_single_bearing_options()
    assert not None is options,"Single bearing options are none"
    is_present=True
    for row in context.table:
        bearing_opt=row["bearing options"]
        if bearing_opt not in options:
            is_present=False
            break
    assert False is is_present, "All the bearing option are not present"
@then(u'Close dropdown without selecting any option.')
def step_impl(context):
    skf_single_bearing.clicking_blank_space()
    pass

@when(u'the user selects "{bearing_name}" from Select bearing type dropdown')
def step_impl(context,bearing_name):
    global skf_single_bearing
    skf_single_bearing = SKFBearing(context)
    assert True is skf_single_bearing.select_single_immage(), "Not able to select Single bearing option"
    assert True is skf_single_bearing.click_single_bearing_dropdown(),"Not able to click on Single bearing dropdown"
    assert True is skf_single_bearing.selecting_single_bearing(bearing_name=bearing_name), "Not able to select " \
                                                                                           "Bearing options "
    pass

@when(u'enter "{designation}" in Search designation input box')
def step_impl(context,designation):
    assert True is skf_single_bearing.enter_designation(designation),"Not able to enter "+str(designation)+"Into search field"
    pass


@when(u'Select the row showing ‘{designation}’ under ‘Designation’ header.')
def step_impl(context,designation):
    assert True is skf_single_bearing.select_designation(designation=designation),"Not able to enter"+str(designation)+"from search field"
    pass
@then(u'verify ‘Next’ button color has turned to ‘Dark grey’')
def step_impl(context):
    assert True is skf_single_bearing.get_next_button_attribute(),"Next element is not dark grey"
    pass
