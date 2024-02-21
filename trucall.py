
from tkinter import *
import requests


API = "YOUR API KEY"
heading = {
    "apikey": API
}


def finding():
    num = entry.get()
    URL = f"https://api.apilayer.com/number_verification/validate?number={num}"
    response = requests.get(url=URL, headers=heading)
    data = response.json()
    newdata=""
    for key,value in data.items():
        newdata+=f"{key} : {value}\n"
    result.delete(1.0,END)
    result.insert(END, newdata)


window = Tk()
window.config(bg="green")
window.title("True caller bot 🚩")

label1 = Label(window, text="Enter your Number :")
label1.grid(column=0, row=0)
entry = Entry(window)
entry.grid(column=2, row=0)
btn = Button(window, text="Find", command=finding)
btn.grid(column=1, row=2)
result = Text(window, width=50, height=20)
text = """Call Number Verification """
result.insert(END, text)
result.grid(column=1, row=3)
window.mainloop()
