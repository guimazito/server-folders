from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from create_folder import *
from widget_tip import *

# PASTE DERIVED RELEASE (COPIED) ON ENTRY RELEASE BOX
def paste(event):
    excel_copy = root.clipboard_get().replace('\t', '_')
    a = excel_copy.strip()
    en_release.delete(0, 'end')
    en_release.insert(0, a)
    # PASTE RELEASE GROUP BASED ON RELEASE COPIED
    ap, cp, csc = a.split('_')
    group = csc[0:3]
    en_group.config(state='normal')
    en_group.delete(0, 'end')
    en_group.insert(0, group.strip())
    en_group.config(state='readonly')

root = Tk()
root.geometry("419x125")
root.title("Server Folders 1.0")
#root.resizable(0, 0)
# STARTING WITH MR PICKED
rd_value = tk.IntVar(value=1)
filename = ''

def create_folders():
    if en_save_local.get() == '' or en_project_name.get() == '' or en_release.get() == '' or filename == '':
        messagebox.showwarning(title='ERROR', message='Fill in all fields!')
        return
    subpath = en_save_local.get()
    project_name = en_project_name.get()
    release = en_release.get()
    radio_position = rd_value.get()
    buyer = buyer_list(filename)
    path_creation(subpath, project_name, release, radio_position, buyer) 
    # SHOWING PATHS CREATED
    msg_box = Toplevel()
    msg_box.geometry('1400x200')
    msg_box.title('DONE')
    Grid.rowconfigure(msg_box,0,weight=1)
    Grid.columnconfigure(msg_box,0,weight=1)
    t = Text(msg_box)
    t.grid(row=0, column=0, sticky="NSEW")
#    t.insert({VERSION}, '\n'.join('{}: {}'.format(*k) for k in enumerate(msg)))
    t.config(state='disabled')
    # CLEANING LAST MESSAGES
    msg.clear()
    
# OPEN BUYERS FILE.TXT    
def upload_buyers(): 
    global filename
    filename =  filedialog.askopenfilename(parent=root,title = "Select file",filetypes = (("Text files", "*.txt"),("All files","*.*")))
    en_buyer.config(state='normal')
    en_buyer.insert(END, filename)
    en_buyer.config(state='readonly')
    return filename

# CONVERT FILE.TXT IN TO A LIST
def buyer_list(filename):
    with open(r"{f}".format(f=filename)) as f:
        lines = f.read().splitlines()
    return lines

# FOLDER TYPE
lb_radio = Label(root, text='Folder Type')
lb_radio.grid(column=0, row=0, sticky='w')
rd_op1 = Radiobutton(root, text='Type A', variable=rd_value, value=1)
rd_op1.grid(column=1, row=0, sticky='w')
rd_op2 = Radiobutton(root, text='Type B', variable=rd_value, value=2, bd=-2)
rd_op2.grid(column=2, row=0, sticky='w')
rd_op3 = Radiobutton(root, text='Type C', variable=rd_value, value=3)
rd_op3.grid(column=3, row=0, sticky='w')

# PROJECT NAME
lb_project_name = Label(root, text='Project Name')
lb_project_name.grid(column=0, row=3, sticky='w')
en_project_name = Entry(root, width=40)
en_project_name.grid(column=1, row=3, sticky='w', columnspan=2)
en_project_tip = CreateToolTip(en_project_name, 'Ex:'+'\n'+'Project_ABC')

# RELEASE
lb_release = Label(root, text='Release')
lb_release.grid(column=0, row=4, sticky='w')
en_release = Entry(root, width=40)
en_release.grid(column=1, row=4, sticky='w', columnspan=2)
en_release_tip = CreateToolTip(en_release, 'Ex:'+'\n'+'AAA_BBB_CCC'+'\n'+'Copy and paste directly from your excel')

# RELEASE GROUP
en_group = Entry(root, width=6, state='readonly')
en_group.grid(column=3, row=4, sticky='w', padx=3)

# BUYER PATH
lb_buyer = Label(root, text='Buyers')
lb_buyer.grid(column=0, row=5, sticky='w')
en_buyer = Entry(root, state='readonly', width=40)
en_buyer.grid(column=1, row=5, sticky='w', columnspan=2)

# BUYER BUTTON
btn_buyers = Button(root, text='Upload File', command=upload_buyers, width=11, padx=3)
btn_buyers.grid(column=3, row=5, sticky='w')
btn_buyers_tip = CreateToolTip(btn_buyers, 'Ex file.txt:'+'\n'+'Banana'+'\n'+'Apple'+'\n'+'Each fruit must be on a line with no spaces')

# SAVE LOCATION
lb_save_local = Label(root, text='Save Location')
lb_save_local.grid(column=0, row=6, stick='w')
en_save_local = Entry(root, width=40)
en_save_local.grid(column=1, row=6, sticky='w', columnspan=2)

# BUTTONS
btn_save = Button(root, text='Create Folders', command=create_folders, width=11, padx=3)
btn_save.grid(column=3, row=6, stick='w')

# EVENT PAST RELEASE
en_release.bind("<1>", paste)
root.mainloop()