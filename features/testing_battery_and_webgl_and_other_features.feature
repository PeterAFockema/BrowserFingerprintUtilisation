Feature: Checking battery and screen and other feature element fingerprinting responses      
    Scenario: Preliminary Firefox test results for an extension to change the battery and screen and webgl value
        When we view the Firefox page with some battery and screen and webgl values interference
        Then we have a Firefox page which ran the battery and screen and webgl response
        Then the Firefox battery and screen value has been recorded
        Then the Firefox webgl value has been recorded
        Then we will log the battery and screen and webgl testing time in the saved file
        Then the Firefox battery and screen value is saved
        Then the Firefox webgl value is saved
        Then the visitor id for battery and screen and webgl is saved

    Scenario: Preliminary Firefox test results for an extension to change the battery and screen and webRTC value
        When we view the Firefox page with some battery and screen and webRTC values interference
        Then we have a Firefox page which ran the battery and screen and webRTC response
        Then the Firefox battery and screen value has been recorded
        Then the Firefox webRTC value has been recorded
        Then we will log the battery and screen and webRTC testing time in the saved file
        Then the Firefox battery and screen value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for battery and screen and webRTC is saved