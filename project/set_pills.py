import tkinter as tk
from tkinter.constants import END
import tkinter.messagebox
import json
import paho.mqtt.client as mqtt
import uuid

# prepare mqtt data sending
client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/pilldispenser'

# function to save values to csv for usage by pill dispenser
def save():
    def read_input(button):
        val = button.get()
        return 0 if len(val) == 0 else int(val)
    try:
        out_dict = {k: list(map(read_input, v)) for k, v in in_dict.items()}
        out_json = json.dumps(out_dict)
        client.publish(topic, out_json)
    except ValueError:
        tk.messagebox.showinfo("Title", "Input must be a whole number or blank.")

# function that clears input
def clear():
    for button_a, button_b in in_dict.values():
        button_a.delete(0, END)
        button_b.delete(0, END)

# create main window
master = tk.Tk()

# set size of window
master.geometry("425x275")

# Describe header row for window
header_row = 0
tk.Label(master, text="Enter your pill usage!").grid(row=header_row, column=0, columnspan=3)

# Add series names for pills
pill_row = header_row + 1
tk.Label(master, text="Pill A").grid(row=pill_row,column=1)
tk.Label(master, text="Pill B").grid(row=pill_row,column=2)

# add label, entry field
start_row_days = pill_row + 1
in_dict = {}
for idx, day in enumerate(['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']):
    row = start_row_days+idx
    tk.Label(master, text=day).grid(row=row)
    pill_a = tk.Entry(master)
    pill_a.grid(row=row, column=1)

    pill_b = tk.Entry(master)
    pill_b.grid(row=row, column=2)
    
    in_dict[idx] = [pill_a, pill_b]

# add buttons
button_row = start_row_days + 8

save_button = tk.Button(master, text="Save", command=save)
save_button.grid(row=button_row,column=2)

clear_button = tk.Button(master, text="Clear", command=clear)
clear_button.grid(row=button_row,column=1)

master.mainloop()