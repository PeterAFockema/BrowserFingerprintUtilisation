Feature: Checking battery and other feature element fingerprinting responses
    Scenario: Preliminary Firefox test results for an extension to change the battery and canvas value
        When we view the Firefox page with some battery and canvas values interference
        Then we have a Firefox page which ran the battery and canvas response
        # Then the Firefox battery value has been recorded
        # Then the Firefox canvas value has been recorded
        Then we will log the battery and canvas testing time in the saved file
        Then the Firefox battery value is saved
        Then the Firefox canvas value is saved
        Then the visitor id for battery and canvas is saved

    Scenario: Preliminary Firefox test results for an extension to change the battery and clientRects value
        When we view the Firefox page with some battery and clientRects values interference
        Then we have a Firefox page which ran the battery and clientRects response
        # Then the Firefox battery value has been recorded
        # Then the Firefox clientRects value has been recorded
        Then we will log the battery and clientRects testing time in the saved file
        Then the Firefox battery value is saved
        Then the Firefox clientRects value is saved
        Then the visitor id for battery and clientRects is saved

    Scenario: Preliminary Firefox test results for an extension to change the battery and font value
        When we view the Firefox page with some battery and font values interference
        Then we have a Firefox page which ran the battery and font response
        # Then the Firefox battery value has been recorded
        # Then the Firefox font value has been recorded
        Then we will log the battery and font testing time in the saved file
        Then the Firefox battery value is saved
        Then the Firefox font value is saved
        Then the visitor id for battery and font is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the battery and navigator value
        When we view the Firefox page with some battery and navigator values interference
        Then we have a Firefox page which ran the battery and navigator response
        # Then the Firefox battery value has been recorded
        # Then the Firefox navigator value has been recorded
        Then we will log the battery and navigator testing time in the saved file
        Then the Firefox battery value is saved
        Then the Firefox navigator value is saved
        Then the visitor id for battery and navigator is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the battery and screen value
        When we view the Firefox page with some battery and screen values interference
        Then we have a Firefox page which ran the battery and screen response
        # Then the Firefox battery value has been recorded
        # Then the Firefox screen value has been recorded
        Then we will log the battery and screen testing time in the saved file
        Then the Firefox battery value is saved
        Then the Firefox screen value is saved
        Then the visitor id for battery and screen is saved

    Scenario: Preliminary Firefox test results for an extension to change the battery and webgl value
        When we view the Firefox page with some battery and webgl values interference
        Then we have a Firefox page which ran the battery and webgl response
        # Then the Firefox battery value has been recorded
        # Then the Firefox webgl value has been recorded
        Then we will log the battery and webgl testing time in the saved file
        Then the Firefox battery value is saved
        Then the Firefox webgl value is saved
        Then the visitor id for battery and webgl is saved

    Scenario: Preliminary Firefox test results for an extension to change the battery and webRTC value
        When we view the Firefox page with some battery and webRTC values interference
        Then we have a Firefox page which ran the battery and webRTC response
        # Then the Firefox battery value has been recorded
        # Then the Firefox webRTC value has been recorded
        Then we will log the battery and webRTC testing time in the saved file
        Then the Firefox battery value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for battery and webRTC is saved