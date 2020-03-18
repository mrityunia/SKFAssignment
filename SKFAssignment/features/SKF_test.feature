Feature: SKF test

  @chrome
  Scenario: Verify Bearing dropdown
    Given the user launch the application
      And ‘Accept & continue’ if displayed
     When the user clicks on ‘Single Bearing’ image
      And Clicks on Select bearing type dropdown
     Then verify the following options are present
      | bearing options                    |
      | Insert bearing (Y-bearing)         |
      | Angular contact ball bearings      |
      | Self-aligning ball bearings        |
      | Cylindrical roller bearings        |
      | Needle roller bearings             |
      | Tapered roller bearings            |
      | Spherical roller bearings          |
      | CARB toroidal roller bearings      |
      | Thrust ball bearings               |
      | Cylindrical roller thrust bearings |
      | Needle roller thrust bearings      |
      | Spherical roller thrust bearings   |
      | Track roller                       |
      | Deep groove ball bearings          |
      And Close dropdown without selecting any option.

  @chrome
  Scenario: Verify user is able to open Deep groove ball bearings
    Given the user launch the application
      And ‘Accept & continue’ if displayed
     When the user selects "Deep groove ball bearing" from Select bearing type dropdown
      And enter "6203" in Search designation input box
      And Select the row showing ‘6203’ under ‘Designation’ header.
     Then verify ‘Next’ button color has turned to ‘Dark grey’