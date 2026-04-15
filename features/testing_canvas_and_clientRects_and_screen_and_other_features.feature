Feature: Checking canvas and clientRects and screen and other feature element fingerprinting responses      
    Scenario: Preliminary Firefox test results for an extension to change the canvas and clientRects and screen and webgl value
        When we view the Firefox page with some canvas and clientRects and screen and webgl values interference
        Then we have a Firefox page which ran the canvas and clientRects and screen and webgl response
        Then the Firefox canvas and clientRects and screen value has been recorded
        Then the Firefox webgl value has been recorded
        Then we will log the canvas and clientRects and screen and webgl testing time in the saved file
        Then the Firefox canvas and clientRects and screen value is saved
        Then the Firefox webgl value is saved
        Then the visitor id for canvas and clientRects and screen and webgl is saved

    Scenario: Preliminary Firefox test results for an extension to change the canvas and clientRects and screen and webRTC value
        When we view the Firefox page with some canvas and clientRects and screen and webRTC values interference
        Then we have a Firefox page which ran the canvas and clientRects and screen and webRTC response
        Then the Firefox canvas and clientRects and screen value has been recorded
        Then the Firefox webRTC value has been recorded
        Then we will log the canvas and clientRects and screen and webRTC testing time in the saved file
        Then the Firefox canvas and clientRects and screen value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for canvas and clientRects and screen and webRTC is saved