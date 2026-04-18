Feature: Checking audio and canvas and webgl and other feature element fingerprinting responses   
    Scenario: Preliminary Firefox test results for an extension to change the audio and canvas and webgl and webRTC value
        When we view the Firefox page with some audio and canvas and webgl and webRTC values interference
        Then we have a Firefox page which ran the audio and canvas and webgl and webRTC response
        Then the Firefox audio and canvas and webgl value has been recorded
        Then the Firefox webRTC value has been recorded
        Then we will log the audio and canvas and webgl and webRTC testing time in the saved file
        # Then the Firefox audio and canvas and webgl value is saved
        Then the Firefox audio value is saved
        Then the Firefox canvas value is saved
        Then the Firefox webgl value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for audio and canvas and webgl and webRTC is saved