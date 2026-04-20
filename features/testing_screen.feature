Feature: Checking screen element fingerprinting responses
    Scenario: Preliminary Firefox test results for no extension to change the screen value
        When we view the Firefox page with no screen values interference
        Then we have a Firefox page which ran the screen response
        # Then the Firefox screen value has been recorded
        Then we will log the no screen testing time variance in the saved file
        Then the Firefox screen value is saved
        Then the visitor id for screen value is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the screen value
        When we view the Firefox page with some screen values interference
        Then we have a Firefox page which ran the screen response
        # Then the Firefox screen value has been recorded
        Then we will log the screen testing time in the saved file
        Then the Firefox screen value is saved
        Then the visitor id for screen value is saved