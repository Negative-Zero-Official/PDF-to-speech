import pyttsx3
from PyPDF2 import PdfReader
import threading
import keyboard
import time

pdf = None
stop_thread = False
pause_thread = False

def play(PdfReader):
    global pdf
    global stop_thread
    
    speaker = pyttsx3.init()
    
    for page_num in range(len(PdfReader.pages)):
        text = PdfReader.pages[page_num].extract_text()
        # for each_line in text.split("\n"):
        #     if stop_thread:
        #         break
        #     while pause_thread:
        #         time.sleep(0.1)
        #     print(each_line)
        #     speaker.say(each_line)
        #     speaker.runAndWait()
        sentences = [
            ' '.join(sent.split())
            for sent in text.split('.')
            if sent.strip()
        ]
        for sentence in sentences:
            if stop_thread:
                break
            while pause_thread:
                time.sleep(0.1)
            print(sentence, end=".\n")
            speaker.say(sentence)
            speaker.runAndWait()
        
    speaker.stop()
    
def pause_playback():
    global pause_thread
    pause_thread = not pause_thread
    print("\nPlayback " + ("paused" if pause_thread else "resumed") + ".")   

def stop_playback():
    global stop_thread
    stop_thread = True
    
def main():
    global pdf
    while True:
        file = input("Enter PDF file name: ")
        try:
            pdf = PdfReader(file)
            break
        except Exception as e:
            print("Error: ", e)
            print("Enter file name again.")
    
    playback_thread = threading.Thread(target=play, args=(pdf,))
    playback_thread.start()
    
    keyboard.add_hotkey("q", stop_playback)
    keyboard.add_hotkey("space", pause_playback)
    
    playback_thread.join()
    
if __name__ == "__main__":
    main()