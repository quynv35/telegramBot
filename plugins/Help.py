#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import config
from telegram import Update
from telegram.ext import CallbackContext

ID = config.ID
TOKEN = config.TOKEN
host = "https://api.telegram.org/bot"+TOKEN


def Help():
	text = """
🔰 Danh sách các lệnh có thể sử dụng:
----------

.play : Chơi nhạc từ youtube.
*Cách dùng : .play <mp3/mp4> <link/keyword>
Ko khuyến khích sử dụng định dạng mp4 - đơn giản vì lúc upload lên sẽ lâu hơn mp3 ;)
*VD: 
  .play mp3 https://www.youtube.com/abcdef123456
  .play mp4 https://www.youtube.com/abcdef123456
  .play mp3 nang tho
  .play mp3 nàng thơ
  .play mp4 nang tho
  .play mp4 nàng thơ

~~~~~

.say : Chuyển văn bản sang giọng nói (Text to Speech).
*Cách dùng: .say <ngôn ngữ> <văn bản>
Tiếng Việt: .say vi Quý
Tiếng Anh: .say en hello

~~~~~

.spam : Spam sms sđt nào đó :))) 
*Cách dùng : .spam <sđt> <text>
*VD: .spam 0123456789 (spam sms đến sđt 0123456789)

.spam 0123456789 abc123 (gửi tin nhắn abc123 đến sđt 0123456789)

‼️ Vì tính chất "nguy hiểm" của tool spam nên số lượng sms sẽ bị giới hạn đối với 1 sđt :)
🚫 Nghiêm cấm sử dụng chức năng .spam để gạ đòn gạ djt, Admin ko chịu trách nhiệm với những gì các bạn làm, nếu để Admin phát hiện thì bot sẽ đéo rep bạn nữa!

~~~~~

.lookup : Kiểm tra sđt nào đó 🔎🔎🔎
*Cách dùng: .lookup <sđt>
*VD: .lookup 0123456789

~~~~~

.call : Gọi nặc danh đến sđt nào đó (làm xong rồi nhưng ko biết có nên public ko :v).
*Cách dùng: .call <sđt>
*VD: .call 0123456789

~~~~~
Chưa nghĩ ra tính năng mới :3

⚠️ Con bot này ăn nói hơi cục và láo toét :) Đề nghị thí chủ ko nên chọc nó, nó bực lên Admin cũng ko ngăn đc 😓

Để mua bot, cần hỗ trợ hay gì gì đó hãy liên hệ: https://fb.com/quymaxlaayf

©️Copyright 2021 for NguyenQuy. All right reserved 👌

	"""
	return(text)
