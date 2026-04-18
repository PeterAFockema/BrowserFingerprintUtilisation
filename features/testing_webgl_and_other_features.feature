Feature: Checking webgl and other feature element fingerprinting responses        
    Scenario: Preliminary Firefox test results for an extension to change the webgl and webRTC value
        When we view the Firefox page with some webgl and webRTC values interference
        Then we have a Firefox page which ran the webgl and webRTC response
        Then the Firefox webgl value has been recorded
        Then the Firefox webRTC value has been recorded
        Then we will log the webgl and webRTC testing time in the saved file
        Then the Firefox webgl value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for webgl and webRTC is saved