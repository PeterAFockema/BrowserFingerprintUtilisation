Feature: Checking navigator and other feature element fingerprinting responses        
    Scenario: Preliminary Firefox test results for an extension to change the navigator and screen value
        When we view the Firefox page with some navigator and screen values interference
        Then we have a Firefox page which ran the navigator and screen response
        # Then the Firefox navigator value has been recorded
        # Then the Firefox screen value has been recorded
        Then we will log the navigator and screen testing time in the saved file
        Then the Firefox navigator value is saved
        Then the Firefox screen value is saved
        Then the visitor id for navigator and screen is saved

    Scenario: Preliminary Firefox test results for an extension to change the navigator and webgl value
        When we view the Firefox page with some navigator and webgl values interference
        Then we have a Firefox page which ran the navigator and webgl response
        # Then the Firefox navigator value has been recorded
        # Then the Firefox webgl value has been recorded
        Then we will log the navigator and webgl testing time in the saved file
        Then the Firefox navigator value is saved
        Then the Firefox webgl value is saved
        Then the visitor id for navigator and webgl is saved

    Scenario: Preliminary Firefox test results for an extension to change the navigator and webRTC value
        When we view the Firefox page with some navigator and webRTC values interference
        Then we have a Firefox page which ran the navigator and webRTC response
        # Then the Firefox navigator value has been recorded
        # Then the Firefox webRTC value has been recorded
        Then we will log the navigator and webRTC testing time in the saved file
        Then the Firefox navigator value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for navigator and webRTC is saved