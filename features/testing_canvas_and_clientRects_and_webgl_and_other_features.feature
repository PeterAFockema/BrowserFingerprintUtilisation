Feature: Checking canvas and clientRects and webgl and other feature element fingerprinting responses
    Scenario: Preliminary Firefox test results for an extension to change the canvas and clientRects and webgl and webRTC value
        When we view the Firefox page with some canvas and clientRects and webgl and webRTC values interference
        Then we have a Firefox page which ran the canvas and clientRects and webgl and webRTC response
        Then the Firefox canvas and clientRects and webgl value has been recorded
        Then the Firefox webRTC value has been recorded
        Then we will log the canvas and clientRects and webgl and webRTC testing time in the saved file
        # Then the Firefox canvas and clientRects and webgl value is saved
        Then the Firefox canvas value is saved
        Then the Firefox clientRects value is saved
        Then the Firefox webgl value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for canvas and clientRects and webgl and webRTC is saved