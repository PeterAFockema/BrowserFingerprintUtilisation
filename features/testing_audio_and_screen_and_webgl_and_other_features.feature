Feature: Checking audio and screen and webgl and other feature element fingerprinting responses      
    Scenario: Preliminary Firefox test results for an extension to change the audio and screen and webgl and webRTC value
        When we view the Firefox page with some audio and screen and webgl and webRTC values interference
        Then we have a Firefox page which ran the audio and screen and webgl and webRTC response
        Then the Firefox audio and screen and webgl value has been recorded
        Then the Firefox webRTC value has been recorded
        Then we will log the audio and screen and webgl and webRTC testing time in the saved file
        Then the Firefox audio and screen and webgl value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for audio and screen and webgl and webRTC is saved