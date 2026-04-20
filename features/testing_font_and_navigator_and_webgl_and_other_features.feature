Feature: Checking font and navigator and webgl and other feature element fingerprinting responses   
    Scenario: Preliminary Firefox test results for an extension to change the font and navigator and webgl and webRTC value
        When we view the Firefox page with some font and navigator and webgl and webRTC values interference
        Then we have a Firefox page which ran the font and navigator and webgl and webRTC response
        # Then the Firefox font and navigator and webgl value has been recorded
        # Then the Firefox webRTC value has been recorded
        Then we will log the font and navigator and webgl and webRTC testing time in the saved file
        # Then the Firefox font and navigator and webgl value is saved
        Then the Firefox font value is saved
        Then the Firefox navigator value is saved
        Then the Firefox webgl value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for font and navigator and webgl and webRTC is saved