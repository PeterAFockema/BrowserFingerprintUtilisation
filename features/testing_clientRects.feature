Feature: Checking clientRects element fingerprinting responses
    Scenario: Preliminary Firefox test results for no extension to change the clientRects value
        When we view the Firefox page with no clientRects values interference
        Then we have a Firefox page which ran the clientRects response
        # Then the Firefox clientRects value has been recorded
        Then we will log the clientRects testing time in the saved file
        Then the Firefox clientRects value is saved
        Then the visitor id for clientRects is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the clientRects value
        When we view the Firefox page with some clientRects values interference
        Then we have a Firefox page which ran the clientRects response
        # Then the Firefox clientRects value has been recorded
        Then we will log the clientRects testing time in the saved file
        Then the Firefox clientRects value is saved
        Then the visitor id for clientRects is saved        
        
        
        