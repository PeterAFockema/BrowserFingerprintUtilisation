Feature: Checking font element fingerprinting responses
    #Scenario: Preliminary Firefox test results for no extension to change the font value
    #    Given we declare a Firefox server defined for font values with no extension
    #    When we view the Firefox page with no font values interference
    #    Then we have a Firefox page which ran the font response
    #    Then the Firefox font value has been recorded
    #    Then we will log the font testing time in the saved file
    #    Then the Firefox font value is saved
    #    Then the visitor id for font is saved
    
    
    Scenario: Preliminary Firefox test results for an extension to change the font value
        Given we declare a Firefox server defined for font values with an extension
        When we view the Firefox page with some font values interference
        Then we have a Firefox page which ran the font response
        Then the Firefox font value has been recorded
        Then we will log the font testing time in the saved file
        Then the Firefox font value is saved
        Then the visitor id for font is saved