Feature: Checking navigator element fingerprinting responses
    Scenario: Preliminary Firefox test results for no extension to change the navigator value
        When we view the Firefox page with no navigator values interference
        Then we have a Firefox page which ran the navigator response
        Then the Firefox navigator value has been recorded
        Then we will log the navigator testing time in the saved file
        Then the Firefox navigator value is saved
        Then the visitor id for navigator is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the navigator value
        When we view the Firefox page with some navigator values interference
        Then we have a Firefox page which ran the navigator response
        Then the Firefox navigator value has been recorded
        Then we will log the navigator testing time in the saved file
        Then the Firefox navigator value is saved
        Then the visitor id for navigator is saved        
        
        
        