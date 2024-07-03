import pyperclip
import sys
import pygetwindow as gw
import keyboard
import pyautogui
import re

from typing import List


def ensure_english_letters(s):
    return re.sub(r'[^a-zA-Z]', '', s)


def lookUpWord():
    # 从剪贴板获取字符串
    text = pyperclip.paste()

    # 判空
    if len(text) == 0:
        return

    # 检查字符串是否全由英文字母组成
    if not ensure_english_letters(text):
        return

    # 查询单词
    windowTitle = "网易有道翻译"
    window = gw.getWindowsWithTitle(windowTitle)[0]
    # 这一窗口是否存在
    if window:
        # 软件"网易有道翻译"具有这样的性质：先最小化窗口，然后再恢复窗口，就可以输入单词了
        # 利用这样的性质，从剪贴板中复制单词进去
        if not window.isMinimized:
            window.minimize() #最小化窗口
        window.restore() #恢复窗口
        window.activate() #使这一窗口成为当前活动窗口

        if window.title == windowTitle: # if getActiveWindowTitle() == windowTitle:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('delete')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')

    pass


def getActiveWindowTitle():
    # 获取当前活跃窗口
    active_window = gw.getActiveWindow()
    if hasattr(active_window, "title"):
        return active_window.title
    else:
        return ""


def doLookUpWord():
    windowTitleStr = getActiveWindowTitle()
    if "WPS Office" in windowTitleStr:
        lookUpWord()


def on_ctrl_c():
    # print("Ctrl+C was pressed!")
    # 因为前一次Ctrl+C已经用于触发，所以现在再向机器输入一次Ctrl+C，不过在这之前要先清空剪贴板
    pyperclip.copy("")
    pyautogui.hotkey('ctrl', 'c')
    doLookUpWord()


def main():
    keyboard.add_hotkey('ctrl+c', on_ctrl_c)
    while True:
        keyboard.wait('ctrl+c')  # 单次Ctrl+C会起到触发的作用，但是不会具有复制的作用（因为Ctrl+C已经用掉了，用于触发了），这里存在冒险竞争


if __name__ == "__main__":
    main()
