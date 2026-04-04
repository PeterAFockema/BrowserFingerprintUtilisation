Feature: Checking webgl element fingerprinting responses
    Scenario: Preliminary Firefox test results for no extension to change the webgl value
        When we view the Firefox page with no webgl values interference
        Then we have a Firefox page which ran the webgl response
        Then the Firefox webgl value has been recorded
        Then we will log the webgl testing time in the saved file
        Then the Firefox webgl value is saved
        Then the visitor id for webgl is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the webgl value
        When we view the Firefox page with some webgl values interference
        Then we have a Firefox page which ran the webgl response
        Then the Firefox webgl value has been recorded
        Then we will log the webgl testing time in the saved file
        Then the Firefox webgl value is saved
        Then the visitor id for webgl is saved        
        
        
        