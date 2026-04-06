Feature: Checking canvas and screen element fingerprinting responses
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

    #Scenario: Preliminary Firefox test results for no extension to change the canvas and screen value
    #    When we view the Firefox page with no canvas values interference
    #    Then we have a Firefox page which ran the canvas response
    #    Then the Firefox canvas value has been recorded
    #    Then we will log the canvas testing time in the saved file
    #    Then the Firefox canvas value is saved
    #    Then the visitor id for canvas is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the canvas and screen value
        When we view the Firefox page with some canvas and screen values interference
        Then we have a Firefox page which ran the canvas and screen response
        Then the Firefox canvas value has been recorded
        Then the Firefox screen value has been recorded
        Then we will log the canvas and screen testing time in the saved file
        Then the Firefox canvas value is saved
        Then the Firefox screen value is saved
        Then the visitor id for canvas and screen is saved