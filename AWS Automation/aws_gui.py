from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os


window = Tk()
window.title("aws key rotate")
window.geometry('450x200')


def browse():
    filename = filedialog.askopenfilename()
    txt.insert(0, filename)


txt = Entry(window, width=50)
txt.grid(column=1, row=0)


browse_btn = Button(window, text="Browse", command=browse)
browse_btn.grid(column=2, row=0)


def get_environment_name(credentials_path):
    profile_name = []
    with open(credentials_path, 'r') as file:
        file_data = file.read()
        environment = re.findall('\[.*?\]', file_data)
        for x in environment:
            profile_name.append(x[1:-1])
    print(profile_name)
    combo = Combobox(window)
    combo['values'] = profile_name
    # combo.current(1)  # set the selected item
    combo.grid(column=2, row=1)
    #return profile_name


env_btn = Button(window, text="Environment", command=lambda: get_environment_name(txt.get()))
env_btn.grid(column=1, row=1)






window.mainloop()
