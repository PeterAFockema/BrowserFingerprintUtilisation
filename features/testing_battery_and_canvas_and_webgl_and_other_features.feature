Feature: Checking battery and canvas and webgl and other feature element fingerprinting responses       
    Scenario: Preliminary Firefox test results for an extension to change the battery and canvas and webgl and webRTC value
        When we view the Firefox page with some battery and canvas and webgl and webRTC values interference
        Then we have a Firefox page which ran the battery and canvas and webgl and webRTC response
        Then the Firefox battery and canvas and webgl value has been recorded
        Then the Firefox webRTC value has been recorded
        Then we will log the battery and canvas and webgl and webRTC testing time in the saved file
        Then the Firefox battery and canvas and webgl value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for battery and canvas and webgl and webRTC is saved