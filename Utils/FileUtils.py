'''
    author: Sun Hai Lang
    date: 2019-09-03

'''

import os, json

'''
json.loads()解码python json格式
json.load()加载python json格式文件

'''

import itchat
import requests
import wxpy

import win32gui
import win32con
import win32clipboard as w

def getText():
    """获取剪贴板文本"""
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    """设置剪贴板文本"""
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def send_qq(to_who, msg):
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    # 将消息写到剪贴板
    setText(msg)
    # 获取qq窗口句柄
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# 测试
to_who='xxx'
msg='这是测试消息'
send_qq(to_who, msg)

if __name__ == "__main__":
    # 自动登录方法，hotReload=True可以缓存，不用每次都登录,但是第一次执行时会出现一个二维码，需要手机微信扫码登录
    #itchat.auto_login(hotReload=True)

    # 搜索好友，search_friends("xxx"),其中"xxx"为好友昵称，备注或微信号不行
    #userfinfo = itchat.search_friends("Zero")   # "智能群管家014"为好友昵称

    #print(userfinfo) #获取userinfo中的UserName参数
    #userid = userfinfo[0]["UserName"]   # 获取用户id

    # 调用微信接口发送消息
    #itchat.send("hello dear", userid)  # 通过用户id发送信息
    # 或
    #itchat.send_msg(msg='hello dear', toUserName=userid)  # 发送纯文本信息
    #bot = wxpy.Bot()
    #myself = bot.self
    #bot.file_helper.send('Hello')
