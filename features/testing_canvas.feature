Feature: Checking canvas element fingerprinting responses
    #Scenario: Preliminary Chrome test results for no extension to change the canvas value
    #    Given we declare a Chrome server defined for canvas values with no extension
    #    When we view the Chrome page with no canvas values interference
    #    Then we have a Chrome page which ran the canvas response
    #    Then the Chrome canvas value has been recorded
    
    # NOTE: This Scenario will not be developed for now (See README.md)
    #Scenario: Preliminary Chrome test results for an extension to change the canvas value
    #    Given we declare a Chrome server defined for canvas values with an extension
    #    When we view the Chrome page with some canvas values interference
    #    Then we have a Chrome page which ran the canvas response
    #    Then the Chrome canvas value has been recorded
    #

    Scenario: Preliminary Firefox test results for no extension to change the canvas value
        Given we declare a Firefox server defined for canvas values with no extension
        When we view the Firefox page with no canvas values interference
        Then we have a Firefox page which ran the canvas response
        Then the Firefox canvas value has been recorded
        Then the Firefox canvas value is saved
        Then the visitor id is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the canvas value
        Given we declare a Firefox server defined for canvas values with an extension
        When we view the Firefox page with some canvas values interference
        Then we have a Firefox page which ran the canvas response
        Then the Firefox canvas value has been recorded
        Then the Firefox canvas value is saved
        Then the visitor id is saved