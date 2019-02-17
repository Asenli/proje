import win32gui
import subprocess
import time
import win32api
import win32con
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


m = PyMouse()  # 创建鼠标实例
k = PyKeyboard()  # 创建键盘实例


def qq_load(account, password, qq_exe):
    qq_exe = qq_exe
    subprocess.Popen([qq_exe])  # 用subprocess模块打开qq程序
    time.sleep(3)  # 给qq留点启动时间
    handle = win32gui.FindWindow(None, 'QQ')  # 获取窗口的句柄，参数1：类名，参数2：标题
    left, top, right, bottom = win32gui.GetWindowRect(handle)
    print(left, top, right, bottom)
    time.sleep(2)
    new_x = int(left + (right - left) / 2) - 70  # 账号输入框坐标
    new_y = int(top + (bottom - top) / 2) + 10  # 账号输入框坐标
    m.click(new_x, new_y, 1, 2)  # 移动鼠标到账号输入框并按下鼠标

    # 模拟键盘输入字符串
    print('%s 正在登陆……' % account)
    time.sleep(3)

    k.tap_key(0)
    m.click(new_x, new_y, 1, 2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 按下鼠标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(3)
    k.type_string(account)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 按下鼠标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 放开鼠标
    k.tap_key(9)  # 点击tab键，键盘对应的kyecode码
    time.sleep(3)
    k.type_string(password)  # 模拟键盘输入字符串
    time.sleep(3)
    k.tap_key(13)
    window = win32gui.FindWindow(None, 'QQ')  # 获取打开的qq窗口的句柄
    # print(w)
    w = win32gui.FindWindow('TXGuiFoundation', 'QQ')
    # 最小化窗口
    win32gui.CloseWindow(w)
    # win32gui.CloseWindow(window)  # 最小化窗口


def qq_data(f,qq_exe):
    with open(f, 'r') as f:
        # f = f.readline() #单条测试用代码
        # account = f.split('----')[0]
        # password = f.split('----')[1]
        # print(account,password)
        # qq_load(account,password)
        i = 1
        for f in f.readlines():
            if i % 10 == 0:
                os.system('taskkill /f /im TXPlatform.exe')  # 杀死腾讯QQ多客户端管理服务
                account = f.split('----')[0]
                password = f.split('----')[1]
                qq_load(account, password,qq_exe)
                time.sleep(2.5)
                i += 1
                continue
            else:
                time.sleep(5)
                account = f.split('----')[0]
                password = f.split('----')[1]
                qq_load(account, password,qq_exe)
                time.sleep(2.5)
                i += 1
            print(i)





    # f = 'C:\\Users\\Administrator\\AppData\Local\\Programs\\Python\\Python35\\QQ.txt'
    # qq_data(f)
