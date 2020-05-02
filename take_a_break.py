import webbrowser
import time

total_breaks = 3
break_count=3

while(break_count<total_breaks):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/")
    break_count = break_count+1