import requests
import tkinter as tk
import time
import sys
import psutil

# Terminate the script


def check_internet_connection():
    try:
        requests.get('http://www.google.com', timeout=3)
        return True
    except requests.ConnectionError:
        return False


def update_message(label,window):
    if not check_internet_connection():
        window.after(1000, update_message, label,window)

    elif check_internet_connection():
        label.config(text="internet connection established")
        window.after(1500, window.destroy)
 
def terminate_script():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'python.exe' and "main.py" in proc.cmdline():
            pid = proc.pid
            proc.terminate()
        if proc.info['name'] == 'jarvis_0.1.exe':
            pid = proc.pid
            proc.terminate()

def on_closing(window):

    terminate_script() 
    sys.exit()

def error_window():
    # Create the main window
    window = tk.Tk()
    window.title("error")
    window.resizable(False, False)
    

    # Create a frame
    frame = tk.Frame(window)
    frame.pack(padx=50, pady=50)  # Add some padding around the frame

    # Create a label with the message
    label = tk.Label(frame, text="internet connection required \n to start JARVIS",font=("Helvetica",18))
    label.pack()
    window.after(1000, update_message, label,window)

    # Run the main event loop
    window.protocol("WM_DELETE_WINDOW", lambda: on_closing(window))
    window.mainloop()

# Call the function with your message
#print(error_window())


