Feature: Checking audio and font and other feature element fingerprinting responses
    Scenario: Preliminary Firefox test results for an extension to change the audio and font and navigator value
        When we view the Firefox page with some audio and font and navigator values interference
        Then we have a Firefox page which ran the audio and font and navigator response
        Then the Firefox audio and font value has been recorded
        Then the Firefox navigator value has been recorded
        Then we will log the audio and font and navigator testing time in the saved file
        Then the Firefox audio and font value is saved
        Then the Firefox navigator value is saved
        Then the visitor id for audio and font and navigator is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the audio and font and screen value
        When we view the Firefox page with some audio and font and screen values interference
        Then we have a Firefox page which ran the audio and font and screen response
        Then the Firefox audio and font value has been recorded
        Then the Firefox screen value has been recorded
        Then we will log the audio and font and screen testing time in the saved file
        Then the Firefox audio and font value is saved
        Then the Firefox screen value is saved
        Then the visitor id for audio and font and screen is saved

    Scenario: Preliminary Firefox test results for an extension to change the audio and font and webgl value
        When we view the Firefox page with some audio and font and webgl values interference
        Then we have a Firefox page which ran the audio and font and webgl response
        Then the Firefox audio and font value has been recorded
        Then the Firefox webgl value has been recorded
        Then we will log the audio and font and webgl testing time in the saved file
        Then the Firefox audio and font value is saved
        Then the Firefox webgl value is saved
        Then the visitor id for audio and font and webgl is saved

    Scenario: Preliminary Firefox test results for an extension to change the audio and font and webRTC value
        When we view the Firefox page with some audio and font and webRTC values interference
        Then we have a Firefox page which ran the audio and font and webRTC response
        Then the Firefox audio and font value has been recorded
        Then the Firefox webRTC value has been recorded
        Then we will log the audio and font and webRTC testing time in the saved file
        Then the Firefox audio and font value is saved
        Then the Firefox webRTC value is saved
        Then the visitor id for audio and font and webRTC is saved