import tkinter as tk
from tkinter import Entry , Label ,Button
import webbrowser

# define the main window
root = tk.Tk()
root.title("YOUR ASSISTANT")

#ADDINNG THE BACKGROUND COLOR
root.configure(bg='steelblue')

#define the function to automate youtube search
#https://www.youtube.com/results?search_query=code+with+harry+python
def search_youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)


#define the function to automate instagram search

def search_instagram():
    Username=entry.get()#.repalce('@',"") #ensure username is clean of @
    url = f"https://www.instagram.com/{Username}/"
    webbrowser.open(url)
   

    
#define the function to automate google search

def search_google():
    query = entry.get()
    url = f"http://www.google.com/search?q={query}"
    webbrowser.open(url)  


#define the function to automate facebook search

def search_facebook():
    query = entry.get()
    url = f"https://www.facebook.com/result?search_query={query}"
    webbrowser.open(url)    


#create  input field, labels,and buttons
Label(root,text="Enter your command : ").pack(pady=10)
entry=Entry(root,width=15)
entry.pack(pady=10)
#create a button

Button(root,text="search on youtube",command=search_youtube).pack(pady=5)
Button(root,text="Search on google",command=search_google).pack(pady=5)
Button(root,text="Search on instagram",command=search_instagram).pack(pady=5)
Button(root,text="Search in facebook",command=search_facebook).pack(pady=5)

#run the GUI event loop
root.mainloop()