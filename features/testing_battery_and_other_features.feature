Feature: Checking battery element fingerprinting responses
    Scenario: Preliminary Firefox test results for no extension to change the battery value
        When we view the Firefox page with no battery values interference
        Then we have a Firefox page which ran the battery response
        Then the Firefox battery value has been recorded
        Then we will log the battery testing time in the saved file
        Then the Firefox battery value is saved
        Then the visitor id for battery is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the battery value
        When we view the Firefox page with some battery values interference
        Then we have a Firefox page which ran the battery response
        Then the Firefox battery value has been recorded
        Then we will log the battery testing time in the saved file
        Then the Firefox battery value is saved
        Then the visitor id for battery is saved        
        
        
        