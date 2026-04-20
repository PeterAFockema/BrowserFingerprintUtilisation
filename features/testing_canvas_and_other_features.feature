Feature: Checking canvas and other feature element fingerprinting responses
    Scenario: Preliminary Firefox test results for an extension to change the canvas and clientRects value
        When we view the Firefox page with some canvas and clientRects values interference
        Then we have a Firefox page which ran the canvas and clientRects response
        # Then the Firefox canvas value has been recorded
        # Then the Firefox clientRects value has been recorded
        Then we will log the canvas and clientRects testing time in the saved file
        Then the Firefox canvas value is saved
        Then the Firefox clientRects value is saved
        Then the visitor id for canvas and clientRects is saved

    Scenario: Preliminary Firefox test results for an extension to change the canvas and font value
        When we view the Firefox page with some canvas and font values interference
        Then we have a Firefox page which ran the canvas and font response
        # Then the Firefox canvas value has been recorded
        # Then the Firefox font value has been recorded
        Then we will log the canvas and font testing time in the saved file
        Then the Firefox canvas value is saved
        Then the Firefox font value is saved
        Then the visitor id for canvas and font is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the canvas and navigator value
        When we view the Firefox page with some canvas and navigator values interference
        Then we have a Firefox page which ran the canvas and navigator response
        # Then the Firefox canvas value has been recorded
        # Then the Firefox navigator value has been recorded
        Then we will log the canvas and navigator testing time in the saved file
        Then the Firefox canvas value is saved
        Then the Firefox navigator value is saved
        Then the visitor id for canvas and navigator is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the canvas and screen value
        When we view the Firefox page with some canvas and screen values interference
        Then we have a Firefox page which ran the canvas and screen response
        # Then the Firefox canvas value has been recorded
        # Then the Firefox screen value has been recorded
        Then we will log the canvas and screen testing time in the saved file
        Then the Firefox canvas value is saved
        Then the Firefox screen value is saved
        Then the visitor id for canvas and screen is saved

    Scenario: Preliminary Firefox test results for an extension to change the canvas and webgl value
        When we view the Firefox page with some canvas and webgl values interference
        Then we have a Firefox page which ran the canvas and webgl response
        # Then the Firefox canvas value has been recorded
        # Then the Firefox webgl value has been recorded
        Then we will log the canvas and webgl testing time in the saved file
        Then the Firefox canvas value is saved
        Then the Firefox webgl value is saved
        Then the visitor id for canvas and webgl is saved

    Scenario: Preliminary Firefox test results for an extension to change the canvas and webRTC value
        When we view the Firefox page with some canvas and webRTC values interference
        Then we have a Firefox page which ran the canvas and webRTC response
        # Then the Firefox canvas value has been recorded
        # Then the Firefox webRTC value has been recorded
        Then we will log the canvas and webRTC testing time in the saved file
        Then the Firefox canvas value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for canvas and webRTC is saved