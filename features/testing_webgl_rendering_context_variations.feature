Feature: Checking WebGLRenderingContext variations for effects on fingerprinting responses
    Scenario: Preliminary Firefox test results for no extension to change WebGLRenderingContext values
        When we view the Firefox page with no parameter or buffer values interference
        Then we have a Firefox page which ran the screen response
        Then the Firefox screen value has been recorded
        Then we will log the screen testing time in the saved file
        Then the Firefox screen value is saved
        Then the visitor id for screen value is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the WebGLRenderingContext parameter value
        When we view the Firefox page with some parameter values interference
        Then we have a Firefox page which ran the parameter response
        Then the Firefox font value has been recorded
        Then we will log the parameter testing time in the saved file
        Then the Firefox font value is saved
        Then the visitor id for parameter value variation is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the WebGLRenderingContext buffer value
        When we view the Firefox page with some buffer values interference
        Then we have a Firefox page which ran the buffer response
        Then the Firefox font value has been recorded
        Then we will log the buffer testing time in the saved file
        Then the Firefox font value is saved
        Then the visitor id for buffer value variation is saved

    Scenario: Preliminary Firefox test results for an extension to change both WebGLRenderingContext parameter and buffer value
        When we view the Firefox page with parameter and buffer values interference
        Then we have a Firefox page which ran the parameter and buffer values response
        Then the Firefox font value has been recorded
        Then we will log the parameter and buffer values testing time in the saved file
        Then the Firefox font value is saved
        Then the visitor id for parameter and buffer values variation value is saved