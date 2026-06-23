Feature: Fingerprinting protection validation

  Scenario Outline: Verify Firefox extension overrides and records modified fingerprint vectors
    When we view the Firefox page with some <feature> values interference
    Then we have a Firefox page which ran the <feature> response
    Then we will log the <feature> testing time in the saved file
    Then the visitor id for <feature> is saved

    Examples:

      | feature                                    |
      | audio and battery and canvas and clientRects and font      |
      | audio and battery and canvas and clientRects and navigator |
      | audio and battery and canvas and clientRects and screen    |
      | audio and battery and canvas and clientRects and webgl     |
      | audio and battery and canvas and clientRects and webRTC    |