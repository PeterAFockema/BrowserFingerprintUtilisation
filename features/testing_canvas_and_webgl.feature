Feature: Checking canvas and webgl element fingerprinting responses
    #Scenario: Preliminary Firefox test results for no extension to change the canvas and webgl value
    #    When we view the Firefox page with no canvas values interference
    #    Then we have a Firefox page which ran the canvas response
    #    Then the Firefox canvas value has been recorded
    #    Then we will log the canvas testing time in the saved file
    #    Then the Firefox canvas value is saved
    #    Then the visitor id for canvas is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the canvas and webgl value
        When we view the Firefox page with some canvas and webgl values interference
        Then we have a Firefox page which ran the canvas and webgl response
        # Then the Firefox canvas value has been recorded
        # Then the Firefox webgl value has been recorded
        Then we will log the canvas and webgl testing time in the saved file
        Then the Firefox canvas value is saved
        Then the Firefox webgl value is saved
        Then the visitor id for canvas and webgl is saved