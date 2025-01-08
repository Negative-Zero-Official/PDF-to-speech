import tkinter as tk
from tkinter import filedialog, messagebox
from Main import start_playback, pause_playback, stop_playback, pdf, stop_thread, pause_thread

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def gui_start_playback():
    file_path = file_entry.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a PDF file.")
        return
    start_playback(file_path)
    status_label.config(text="Status: Playing", fg="green")

def gui_pause_playback():
    pause_playback()
    if pause_thread:
        status_label.config(text="Status: Paused", fg="red")
    else:
        status_label.config(text="Status: Playing", fg="green")

def gui_stop_playback():
    stop_playback()
    status_label.config(text="Status: Idle", fg="blue")

root = tk.Tk()
root.title("PDF Reader")

file_frame = tk.Frame(root)
file_frame.pack(pady=10)

file_label = tk.Label(file_frame, text="Select PDF file:")
file_label.pack(side=tk.LEFT)

file_entry = tk.Entry(file_frame, width=50)
file_entry.pack(side=tk.LEFT, padx=5)

btnBrowse = tk.Button(file_frame, text="Browse", command=select_file)
btnBrowse.pack(side=tk.LEFT)

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

btnPlay = tk.Button(control_frame, text="Play", command=gui_start_playback)
btnPlay.pack(side=tk.LEFT, padx=5)

btnPause = tk.Button(control_frame, text="Pause/Resume", command=gui_pause_playback)
btnPause.pack(side=tk.LEFT, padx=5)

btnStop = tk.Button(control_frame, text="Stop", command=gui_stop_playback)
btnStop.pack(side=tk.LEFT, padx=5)

status_label = tk.Label(root, text="Status: Idle", fg="blue")
status_label.pack(pady=10)

root.mainloop()