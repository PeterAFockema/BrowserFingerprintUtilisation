Feature: Checking HTMLCanvasElement variations for effects on fingerprinting responses
    Scenario: Preliminary Firefox test results for no extension to change HTMLCanvasElement values
        When we view the Firefox page with no toBlob and toDataURL values interference
        Then we have a Firefox page which ran the no toBlob and toDataURL response
        # Then the Firefox canvas value has been recorded
        Then we will log the no toBlob and toDataURL testing time in the saved file
        Then the Firefox canvas value is saved
        Then the visitor id for no toBlob and toDataURL value variation is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the Prototype toBlob value
        When we view the Firefox page with some toBlob values interference
        Then we have a Firefox page which ran the toBlob response
        # Then the Firefox canvas value has been recorded
        Then we will log the toBlob testing time in the saved file
        Then the Firefox canvas value is saved
        Then the visitor id for toBlob value variation is saved
    
    Scenario: Preliminary Firefox test results for an extension to change the Prototype toDataURL value
        When we view the Firefox page with some toDataURL values interference
        Then we have a Firefox page which ran the toDataURL response
        # Then the Firefox canvas value has been recorded
        Then we will log the toDataURL testing time in the saved file
        Then the Firefox canvas value is saved
        Then the visitor id for toDataURL value variation is saved

    Scenario: Preliminary Firefox test results for an extension to change both Prototype toBlob and toDataURL value
        When we view the Firefox page with toBlob and toDataURL values interference
        Then we have a Firefox page which ran the toBlob and toDataURL values response
        # Then the Firefox canvas value has been recorded
        Then we will log the toBlob and toDataURL values testing time in the saved file
        Then the Firefox canvas value is saved
        Then the visitor id for toBlob and toDataURL values variation is saved