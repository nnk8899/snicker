#!/usr/bin/python


import os
import pynput
import threading
import datetime
import time
import win32com.client
import urllib
from urllib import parse,request
import socket
import struct 
import pyttsx3
import win32com


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.10.50.50', 6666))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip




def on_move(x, y):
    global current_active_time
    current_active_time = datetime.datetime.now()
    #print(current_active_time)
    
def on_click(x, y, button, pressed):
    global current_active_time
    current_active_time = datetime.datetime.now()
    #print(current_active_time)

def on_scroll(x, y, dx, dy):
    global current_active_time
    current_active_time = datetime.datetime.now()
    #print(current_active_time)

def on_press(key):
    global current_active_time
    current_active_time = datetime.datetime.now()
    #print(current_active_time)



def listener():
    with pynput.mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll),pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        

def alarming():
	host_ip = get_host_ip()
	while True:
		mutex.acquire()
		current_time = datetime.datetime.now()
		#global current_active_time
		time_delta = current_time-current_active_time
		mutex.release()
		if (((current_time.hour>=9 and current_time.hour<12) or (current_time.hour>=13 and current_time.hour<18)) and (time_delta.seconds>20)):
			url_1 = 'http://127.0.0.1:5000/alarm/' + str(host_ip)
			#url_1 = 'http://127.0.0.1:5000/alarm/127.0.0.1'
			alarm_record = {'update_timestamp':str(current_time)}
			data_1 = parse.urlencode(alarm_record).encode('utf-8')
			req = request.Request(url=url_1, data=data_1, method='PUT')
			f = request.urlopen(req)

		time.sleep(20)





if __name__ == '__main__':

	pid = os.getpid()
	fp = open("D://windowshide/app.pid", "wt")
	fp.write("%d" % pid)
	fp.close()
	
	mutex = threading.Lock()
	global current_active_time
	current_active_time = datetime.datetime.now()
	threads = []
	t1 = threading.Thread(target = listener)
	threads.append(t1)
	t2 = threading.Thread(target = alarming)
	threads.append(t2)
	for t in threads:
		t.setDaemon(True)
		t.start()
		
	while True:
		host_ip = get_host_ip()
		url_2 = 'http://127.0.0.1:5000/ips/' + str(host_ip)
		#url_2 = 'http://127.0.0.1:5000/ips/127.0.0.1'
		heart_beat = {'update_timestamp':str(datetime.datetime.now())}
		data_2 = parse.urlencode(heart_beat).encode('utf-8')
		requ = request.Request(url=url_2, data=data_2, method='PUT')
		f = request.urlopen(requ)
		time.sleep(1800)


