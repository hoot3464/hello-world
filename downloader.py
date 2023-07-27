import mouse
import pyautogui
import webbrowser

with open("themes.txt") as f: #open and read a text file
    for url in f: #finds every url
        pyautogui.moveTo(100, 100, duration=0.5) #killing time before the loop starts   
        webbrowser.open(url)
        pyautogui.moveTo(1769, 147, duration=6) #moves to download button with enough time for the page to load
        mouse.click('left')
        pyautogui.moveTo(960, 540)
        pyautogui.moveTo(1898, 16, duration=20) #moves to X button to close and restart the process, with plenty of time for the file to finish downloading
        mouse.click('left')


