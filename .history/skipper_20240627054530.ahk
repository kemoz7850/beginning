﻿#Requires AutoHotkey v2.0
MButton::
{
    sleep 50
    send "f"
    A_Clipboard := ""
    send "^l"
    sleep 1500
    loop 5
    {
        Send "^c"
    }
    path := "C:\Users\kem7\Documents\GitHub\beginning\python\clipboard.py "
    clip := string(A_Clipboard)
    all1 := path . clip
   msgbox A_Clipboard
}