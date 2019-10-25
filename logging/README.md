# ShitCollection/logging

What can be collected by javascript or php in the web?

This is tried in index.php and indexForward.php  :D

You may have heard about the User-Agent and IP, but what about the screen and window sizes?
In log-indexForward is example data:

| "Datum"               |  "IP"                             |  "Seite"                                                                        |  "Browser" |  "screenX" |  "screenY" |  "windowX" |  "windowY" | 
|-----------------------|-----------------------------------|---------------------------------------------------------------------------------|------------|------------|------------|------------|------------| 
| "25.10.2019 23:51:13" |  "127.0.0.1", "/indexForward.php" |  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0" |  "1920"    |  "1080"    |  "1920"    |  "926"     |            | 


We can see screenX == windowX so the browser could be in full sized mode. Only Y is a bit of. I measured that the window of the browser begins 150 px below the sreens edge so my taskbar is 24 px (1080-926-150 px) the standard for my Desktop environment (MATE). Of course this may sound wired, but this can be used as an OS-detection, when you group it with enough knowledge. I think Windows could be detected very good, because no one changes anything of the taskbar and the only differences are the browser offsets. The browser offsets are stable too for the same browser (no one changes the height of the addressbar). You only have to keep in mind the bookmark-bar you can show or hide in Firefox.

An other way to use this is recognising your users based on this. For example in an bruteforce protection.

## Future ideas
cookies
detection and storing if user has disabled javascript
