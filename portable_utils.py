from PIL import Image, ImageTk
import os

################################################# WINDOWS ############################################

import win32com.client 
from win32com.shell import shell, shellcon
import win32api
import win32con
import win32ui
import win32gui


def saveExecutableIcon(exe, out="tmp/icon.png"):
    shell = win32com.client.Dispatch("WScript.Shell")
    ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
    ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)
    large, small = win32gui.ExtractIconEx(exe, 0)
    win32gui.DestroyIcon(small[0])
    hdc = win32ui.CreateDCFromHandle( win32gui.GetDC(0) )
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap( hdc, ico_x, ico_x )
    hdc = hdc.CreateCompatibleDC()
    hdc.SelectObject( hbmp )
    hdc.DrawIcon( (0,0), large[0] )
    hbmp.SaveBitmapFile( hdc, out)
    img = Image.open(out)
    img.save(out, 'png')


def followLink(link: str):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(lnk)
    return (shortcut.Targetpath, shortcut.Arguments)

