Feature: Checking audio element fingerprinting responses
    Scenario: Preliminary Firefox test results for no extension to change the audio value
        When we view the Firefox page with no audio values interference
        Then we have a Firefox page which ran the audio response
        Then the Firefox audio value has been recorded
        Then we will log the audio testing time in the saved file
        Then the Firefox audio value is saved
        Then the visitor id for audio is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the audio value
        When we view the Firefox page with some audio values interference
        Then we have a Firefox page which ran the audio response
        Then the Firefox audio value has been recorded
        Then we will log the audio testing time in the saved file
        Then the Firefox audio value is saved
        Then the visitor id for audio is saved        
        
        
        