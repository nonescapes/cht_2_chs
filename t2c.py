# Author: Noneescapes
# Date: 2023-1-04

from opencc import OpenCC as cc
import pyperclip
import keyboard
import time

#觸發按鍵設定
key_='f4'

#自定義修復詞
fix_text=[['捷径','快捷方式'],
['fps','帧数'],
['教学','教程'],
['文档夹','文件夹'],
['程序崩溃','程序闪退'],
['影片','视频'],['仿真器','模拟器'],['模块','模组'],['存盘','存档']]


while True:
    #esc 關閉功能
    if keyboard.read_key() == "esc": break
    if keyboard.read_key() == key_:
        keyboard.press_and_release("ctrl+c")
        time.sleep(0.02)
        text = cc('tw2sp').convert(pyperclip.paste())
        #自定義詞彙套用
        for i in fix_text:
            if i[0] in text:
                text=text.replace(i[0],i[1])
        pyperclip.copy(text)

        keyboard.press_and_release("ctrl+v")
        continue
