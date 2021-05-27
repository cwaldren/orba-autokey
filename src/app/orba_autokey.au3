#include <MsgBoxConstants.au3>

; Hello! AutoKey works by clicking on various buttons in the Orba app automatically.
; Because everyone has different screen resolutions, and because the Orba app doesn't use standard Windows controls,
; calibration is required. 
;
; Launch the "AutoIt Window Info" application that installs automatically with AutoIt.
; 1. Make sure Orba app is fullscreen. 
; 2. Click on the "Finder Tool" in the AutoIt Window Info app (looks like a bullseye) and highlight the Orba window
; 3. Drag the cursor onto each of the following coordinates - described below - and fill them in. To see the coordinates, 
;    click the right-arrow icon until you see the "Mouse" tab, which has a "Position" property. 

; Center bullseye on the pencil icon at the top of Orba window. Make sure you're over the white part of the pencil, not the background.
Local $OrbaConnectedCoord[2] = [1057, 54]

; Click the pencil. Center the bullseye over the "Key" box.
Local $OrbaKeyCoord[2] = [858, 512]

; Center the bullseye over the mode (Maj / Min) box. 
Local $OrbaModeCoord[2] = [936, 502]

; All Done! Go back to the README.






; 1st cmdline arg is the desired key 
Local $Key = Number($CmdLine[1])

; 2nd cmdline arg is the desired mode (0 = minor, 1 = major)
Local $Mode = Number($CmdLine[2])

; Color of the white pencil icon that shows an Orba is connected
Local $OrbaConnectedColor = Number(16777215)

; Same deal, but if the edit dialog is already open, we have a tiny bit different color.
Local $OrbaConnnectedColor2 = Number(16711422)

; Color of the Major key in the key selection mode
Local $OrbaMajorMode = Number(1747937)

; Approximate height of each key field in pixels, so we can calculate how far down the list to click 
Local $OrbaKeyFieldHeight = Number(34)

; Use window-local coordinates
AutoItSetOption("MouseCoordMode", 0) 

; Save the current window and mouse pos so it can be restored when finished
$hCurrWin = WinGetHandle("[ACTIVE]")
$aMousePos = MouseGetPos()

WinWait("[REGEXPCLASS:JUCE_*]", "", 5)

If WinExists("[REGEXPCLASS:JUCE_*]") Then  

    WinActivate("[REGEXPCLASS:JUCE_*]")

    ; Early out if there is no Orba connected
    Local $PencilColor = PixelGetColor(1056, 57)
    If $PencilColor <> $OrbaConnectedColor And $PencilColor <> $OrbaConnnectedColor2 Then
        WinActivate($hCurrWin)
        Exit
    EndIf

    ; Open the edit menu if not already open
    If $PencilColor == $OrbaConnectedColor Then
        MouseClick ("left", $OrbaConnectedCoord[0], $OrbaConnectedCoord[1], 1, 3)
    EndIf

    ; Click on the key
    MouseClick("left", $OrbaKeyCoord[0], $OrbaKeyCoord[1], 1, 3)

    Local $OffsetY = $OrbaKeyFieldHeight + ($Key * $OrbaKeyFieldHeight)

    ; During testing this sleep seemed necessary or else sometimes the click won't register
    Sleep(250)

    ; Click on the correct key
    MouseClick("left", $OrbaKeyCoord[0], $OrbaKeyCoord[1] + $OffsetY, 1, 3)

    ; Select the correct mode
    Local $ModeColor = PixelGetColor($OrbaModeCoord[0],  $OrbaModeCoord[1])
    If $ModeColor == $OrbaMajorMode Then
        If $Mode == 0 Then
            MouseClick("left", $OrbaModeCoord[0], $OrbaModeCoord[1])
        EndIf
    Else
        If $Mode == 1 Then
            MouseClick("left", $OrbaModeCoord[0], $OrbaModeCoord[1])
        EndIf
    EndIf

    ; Move mouse back to original location
    MouseMove($aMousePos[0], $aMousePos[1], 0)

    WinActivate($hCurrWin)


EndIf