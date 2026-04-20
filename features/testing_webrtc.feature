Feature: Checking webRTC element fingerprinting responses
    Scenario: Preliminary Firefox test results for no extension to change the webRTC value
        When we view the Firefox page with no webRTC values interference
        Then we have a Firefox page which ran the webRTC response
        # Then the Firefox webRTC value has been recorded
        Then we will log the webRTC testing time in the saved file
        Then the Firefox webRTC value is saved
        Then the visitor id for webRTC is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the webRTC value
        When we view the Firefox page with some webRTC values interference
        Then we have a Firefox page which ran the webRTC response
        # Then the Firefox webRTC value has been recorded
        Then we will log the webRTC testing time in the saved file
        Then the Firefox webRTC value is saved
        Then the visitor id for webRTC is saved        
        
        
        