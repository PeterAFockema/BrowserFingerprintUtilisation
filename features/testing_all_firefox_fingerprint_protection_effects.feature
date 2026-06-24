Feature: Fingerprinting protection validation

  Scenario Outline: Verify Firefox extension overrides and records modified fingerprint vectors
    When we view the Firefox page with some <feature> values interference
    Then we have a Firefox page which ran the <feature> response
    Then we will log the <feature> testing time in the saved file
    Then the visitor id for <feature> is saved

    Examples:

      | feature                                    |
      | audio                                                         |
      | battery                                                       |
      | canvas                                                        |
      | clientRects                                                   |
      | font                                                          |
      | navigator                                                     |
      | screen                                                        |
      | webgl                                                         |
      | webRTC                                                        |
      | audio and battery                                             |
      | audio and canvas                                              |
      | audio and clientRects                                         |
      | audio and font                                                |
      | audio and navigator                                           |
      | audio and screen                                              |
      | audio and webgl                                               |
      | audio and webRTC                                              |
      | battery and canvas                                            |
      | battery and clientRects                                       |
      | battery and font                                              |
      | battery and navigator                                         |
      | battery and screen                                            |
      | battery and webgl                                             |
      | battery and webRTC                                            |
      | canvas and clientRects                                        |
      | canvas and font                                               |
      | canvas and navigator                                          |
      | canvas and screen                                             |
      | canvas and webgl                                              |
      | canvas and webRTC                                             |
      | clientRects and font                                          |
      | clientRects and navigator                                     |
      | clientRects and screen                                        |
      | clientRects and webgl                                         |
      | clientRects and webRTC                                        |
      | font and navigator                                            |
      | font and screen                                               |
      | font and webgl                                                |
      | font and webRTC                                               |
      | navigator and screen                                          |
      | navigator and webgl                                           |
      | navigator and webRTC                                          |
      | screen and webgl                                              |
      | screen and webRTC                                             |
      | webgl and webRTC                                              |
      | audio and battery and canvas                                  |
      | audio and battery and clientRects                             |
      | audio and battery and font                                    |
      | audio and battery and navigator                               |
      | audio and battery and screen                                  |
      | audio and battery and webgl                                   |
      | audio and battery and webRTC                                  |
      | battery and canvas and clientRects                            |
      | battery and canvas and font                                   |
      | battery and canvas and navigator                              |
      | battery and canvas and screen                                 |
      | battery and canvas and webgl                                  |
      | battery and canvas and webRTC                                 |
      | canvas and clientRects and font                               |
      | canvas and clientRects and navigator                          |
      | canvas and clientRects and screen                             |
      | canvas and clientRects and webgl                              |
      | canvas and clientRects and webRTC                             |
      | clientRects and font and navigator                            |
      | clientRects and font and screen                               |
      | clientRects and font and webgl                                |
      | clientRects and font and webRTC                               |
      | font and navigator and screen                                 |
      | font and navigator and webgl                                  |
      | font and navigator and webRTC                                 |
      | navigator and screen and webgl                                |
      | navigator and screen and webRTC                               |
      | screen and webgl and webRTC                                   |
      | audio and battery and canvas and clientRects                  |
      | audio and battery and canvas and font                         |
      | audio and battery and canvas and navigator                    |
      | audio and battery and canvas and screen                       |
      | audio and battery and canvas and webgl                        |
      | audio and battery and canvas and webRTC                       |
      | audio and battery and clientRects and font                    |
      | audio and battery and clientRects and navigator               |
      | audio and battery and clientRects and screen                  |
      | audio and battery and clientRects and webgl                   |
      | audio and battery and clientRects and webRTC                  |
      | audio and battery and font and navigator                      |
      | audio and battery and font and screen                         |
      | audio and battery and font and webgl                          |
      | audio and battery and font and webRTC                         |
      | audio and battery and navigator and screen                    |
      | audio and battery and navigator and webgl                     |
      | audio and battery and navigator and webRTC                    |
      | audio and battery and screen and webgl                        |
      | audio and battery and screen and webRTC                       |
      | audio and battery and webgl and webRTC                        |
      | audio and canvas and clientRects and font                     |
      | audio and canvas and clientRects and navigator                |
      | audio and canvas and clientRects and screen                   |
      | audio and canvas and clientRects and webgl                    |
      | audio and canvas and clientRects and webRTC                   |
      | audio and canvas and font and navigator                       |
      | audio and canvas and font and screen                          |
      | audio and canvas and font and webgl                           |
      | audio and canvas and font and webRTC                          |
      | audio and canvas and navigator and screen                     |
      | audio and canvas and navigator and webgl                      |
      | audio and canvas and navigator and webRTC                     |
      | audio and canvas and screen and webgl                         |
      | audio and canvas and screen and webRTC                        |
      | audio and canvas and webgl and webRTC                         |
      | audio and clientRects and font and navigator                  |
      | audio and clientRects and font and screen                     |
      | audio and clientRects and font and webgl                      |
      | audio and clientRects and font and webRTC                     |
      | audio and clientRects and navigator and screen                |
      | audio and clientRects and navigator and webgl                 |
      | audio and clientRects and navigator and webRTC                |
      | audio and clientRects and screen and webgl                    |
      | audio and clientRects and screen and webRTC                   |
      | audio and clientRects and webgl and webRTC                    |
      | audio and font and navigator and screen                       |
      | audio and font and navigator and webgl                        |
      | audio and font and navigator and webRTC                       |
      | audio and font and screen and webgl                           |
      | audio and font and screen and webRTC                          |
      | audio and font and webgl and webRTC                           |
      | audio and navigator and screen and webgl                      |
      | audio and navigator and screen and webRTC                     |
      | audio and navigator and webgl and webRTC                      |
      | audio and screen and webgl and webRTC                         |
      | battery and canvas and clientRects and font                   |
      | battery and canvas and clientRects and navigator              |
      | battery and canvas and clientRects and screen                 |
      | battery and canvas and clientRects and webgl                  |
      | battery and canvas and clientRects and webRTC                 |
      | battery and canvas and font and navigator                     |
      | battery and canvas and font and screen                        |
      | battery and canvas and font and webgl                         |
      | battery and canvas and font and webRTC                        |
      | battery and canvas and navigator and screen                   |
      | battery and canvas and navigator and webgl                    |
      | battery and canvas and navigator and webRTC                   |
      | battery and canvas and screen and webgl                       |
      | battery and canvas and screen and webRTC                      |
      | battery and canvas and webgl and webRTC                       |
      | battery and clientRects and font and navigator                |
      | battery and clientRects and font and screen                   |
      | battery and clientRects and font and webgl                    |
      | battery and clientRects and font and webRTC                   |
      | battery and clientRects and navigator and screen              |
      | battery and clientRects and navigator and webgl               |
      | battery and clientRects and navigator and webRTC              |
      | battery and clientRects and screen and webgl                  |
      | battery and clientRects and screen and webRTC                 |
      | battery and clientRects and webgl and webRTC                  |
      | battery and font and navigator and screen                     |
      | battery and font and navigator and webgl                      |
      | battery and font and navigator and webRTC                     |
      | battery and font and screen and webgl                         |
      | battery and font and screen and webRTC                        |
      | battery and font and webgl and webRTC                         |
      | battery and navigator and screen and webgl                    |
      | battery and navigator and screen and webRTC                   |
      | battery and navigator and webgl and webRTC                    |
      | battery and screen and webgl and webRTC                       |
      | canvas and clientRects and font and navigator                 |
      | canvas and clientRects and font and screen                    |
      | canvas and clientRects and font and webgl                     |
      | canvas and clientRects and font and webRTC                    |
      | canvas and clientRects and navigator and screen               |
      | canvas and clientRects and navigator and webgl                |
      | canvas and clientRects and navigator and webRTC               |
      | canvas and clientRects and screen and webgl                   |
      | canvas and clientRects and screen and webRTC                  |
      | canvas and clientRects and webgl and webRTC                   |
      | canvas and font and navigator and screen                      |
      | canvas and font and navigator and webgl                       |
      | canvas and font and navigator and webRTC                      |
      | canvas and font and screen and webgl                          |
      | canvas and font and screen and webRTC                         |
      | canvas and font and webgl and webRTC                          |
      | canvas and navigator and screen and webgl                     |
      | canvas and navigator and screen and webRTC                    |
      | canvas and navigator and webgl and webRTC                     |
      | canvas and screen and webgl and webRTC                        |
      | clientRects and font and navigator and screen                 |
      | clientRects and font and navigator and webgl                  |
      | clientRects and font and navigator and webRTC                 |
      | clientRects and font and screen and webgl                     |
      | clientRects and font and screen and webRTC                    |
      | clientRects and font and webgl and webRTC                     |
      | clientRects and navigator and screen and webgl                |
      | clientRects and navigator and screen and webRTC               |
      | clientRects and navigator and webgl and webRTC                |
      | clientRects and screen and webgl and webRTC                   |
      | font and navigator and screen and webgl                       |
      | font and navigator and screen and webRTC                      |
      | font and navigator and webgl and webRTC                       |
      | font and screen and webgl and webRTC                          |
      | navigator and screen and webgl and webRTC                     |
      | audio and battery and canvas and clientRects and font         |
      | audio and battery and canvas and clientRects and navigator    |
      | audio and battery and canvas and clientRects and screen       |
      | audio and battery and canvas and clientRects and webgl        |
      | audio and battery and canvas and clientRects and webRTC       |
      | audio and battery and canvas and font and navigator           |
      | audio and battery and canvas and font and screen              |
      | audio and battery and canvas and font and webgl               |
      | audio and battery and canvas and font and webRTC              |
      | audio and battery and canvas and navigator and screen         |
      | audio and battery and canvas and navigator and webgl          |
      | audio and battery and canvas and navigator and webRTC         |
      | audio and battery and canvas and screen and webgl             |
      | audio and battery and canvas and screen and webRTC            |
      | audio and battery and canvas and webgl and webRTC             |
      | audio and battery and clientRects and font and navigator      |
      | audio and battery and clientRects and font and screen         |
      | audio and battery and clientRects and font and webgl          |
      | audio and battery and clientRects and font and webRTC         |
      | audio and battery and clientRects and navigator and screen    |
      | audio and battery and clientRects and navigator and webgl     |
      | audio and battery and clientRects and navigator and webRTC    |
      | audio and battery and clientRects and screen and webgl        |
      | audio and battery and clientRects and screen and webRTC       |
      | audio and battery and clientRects and webgl and webRTC        |
      | audio and battery and font and navigator and screen           |
      | audio and battery and font and navigator and webgl            |
      | audio and battery and font and navigator and webRTC           |
      | audio and battery and font and screen and webgl               |
      | audio and battery and font and screen and webRTC              |
      | audio and battery and font and webgl and webRTC               |
      | audio and battery and navigator and screen and webgl          |
      | audio and battery and navigator and screen and webRTC         |
      | audio and battery and navigator and webgl and webRTC          |
      | audio and battery and screen and webgl and webRTC             |
      | audio and canvas and clientRects and font and navigator       |
      | audio and canvas and clientRects and font and screen          |
      | audio and canvas and clientRects and font and webgl           |
      | audio and canvas and clientRects and font and webRTC          |
      | audio and canvas and clientRects and navigator and screen     |
      | audio and canvas and clientRects and navigator and webgl      |
      | audio and canvas and clientRects and navigator and webRTC     |
      | audio and canvas and clientRects and screen and webgl         |
      | audio and canvas and clientRects and screen and webRTC        |
      | audio and canvas and clientRects and webgl and webRTC         |
      | audio and canvas and font and navigator and screen            |
      | audio and canvas and font and navigator and webgl             |
      | audio and canvas and font and navigator and webRTC            |
      | audio and canvas and font and screen and webgl                |
      | audio and canvas and font and screen and webRTC               |
      | audio and canvas and font and webgl and webRTC                |
      | audio and canvas and navigator and screen and webgl           |
      | audio and canvas and navigator and screen and webRTC          |
      | audio and canvas and navigator and webgl and webRTC           |
      | audio and canvas and screen and webgl and webRTC              |
      | audio and clientRects and font and navigator and screen       |
      | audio and clientRects and font and navigator and webgl        |
      | audio and clientRects and font and navigator and webRTC       |
      | audio and clientRects and font and screen and webgl           |
      | audio and clientRects and font and screen and webRTC          |
      | audio and clientRects and font and webgl and webRTC           |
      | audio and clientRects and navigator and screen and webgl      |
      | audio and clientRects and navigator and screen and webRTC     |
      | audio and clientRects and navigator and webgl and webRTC      |
      | audio and clientRects and screen and webgl and webRTC         |
      | audio and font and navigator and screen and webgl             |
      | audio and font and navigator and screen and webRTC            |
      | audio and font and navigator and webgl and webRTC             |
      | audio and font and screen and webgl and webRTC                |
      | audio and navigator and screen and webgl and webRTC           |
      | battery and canvas and clientRects and font and navigator     |
      | battery and canvas and clientRects and font and screen        |
      | battery and canvas and clientRects and font and webgl         |
      | battery and canvas and clientRects and font and webRTC        |
      | battery and canvas and clientRects and navigator and screen   |
      | battery and canvas and clientRects and navigator and webgl    |
      | battery and canvas and clientRects and navigator and webRTC   |
      | battery and canvas and clientRects and screen and webgl       |
      | battery and canvas and clientRects and screen and webRTC      |
      | battery and canvas and clientRects and webgl and webRTC       |
      | battery and canvas and font and navigator and screen          |
      | battery and canvas and font and navigator and webgl           |
      | battery and canvas and font and navigator and webRTC          |
      | battery and canvas and font and screen and webgl              |
      | battery and canvas and font and screen and webRTC             |
      | battery and canvas and font and webgl and webRTC              |
      | battery and canvas and navigator and screen and webgl         |
      | battery and canvas and navigator and screen and webRTC        |
      | battery and canvas and navigator and webgl and webRTC         |
      | battery and canvas and screen and webgl and webRTC            |
      | battery and clientRects and font and navigator and screen     |
      | battery and clientRects and font and navigator and webgl      |
      | battery and clientRects and font and navigator and webRTC     |
      | battery and clientRects and font and screen and webgl         |
      | battery and clientRects and font and screen and webRTC        |
      | battery and clientRects and font and webgl and webRTC         |
      | battery and clientRects and navigator and screen and webgl    |
      | battery and clientRects and navigator and screen and webRTC   |
      | battery and clientRects and navigator and webgl and webRTC    |
      | battery and clientRects and screen and webgl and webRTC       |
      | battery and font and navigator and screen and webgl           |
      | battery and font and navigator and screen and webRTC          |
      | battery and font and navigator and webgl and webRTC           |
      | battery and font and screen and webgl and webRTC              |
      | battery and navigator and screen and webgl and webRTC         |
      | canvas and clientRects and font and navigator and screen      |
      | canvas and clientRects and font and navigator and webgl       |
      | canvas and clientRects and font and navigator and webRTC      |
      | canvas and clientRects and font and screen and webgl          |
      | canvas and clientRects and font and screen and webRTC         |
      | canvas and clientRects and font and webgl and webRTC          |
      | canvas and clientRects and navigator and screen and webgl     |
      | canvas and clientRects and navigator and screen and webRTC    |
      | canvas and clientRects and navigator and webgl and webRTC     |
      | canvas and clientRects and screen and webgl and webRTC        |
      | canvas and font and navigator and screen and webgl            |
      | canvas and font and navigator and screen and webRTC           |
      | canvas and font and navigator and webgl and webRTC            |
      | canvas and font and screen and webgl and webRTC               |
      | canvas and navigator and screen and webgl and webRTC          |
      | clientRects and font and navigator and screen and webgl       |
      | clientRects and font and navigator and screen and webRTC      |
      | clientRects and font and navigator and webgl and webRTC       |
      | clientRects and font and screen and webgl and webRTC          |
      | clientRects and navigator and screen and webgl and webRTC     |
      | font and navigator and screen and webgl and webRTC            |