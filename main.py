import tkinter as tk
from tkinter import ttk
from random import choice
import cv2
from PIL import Image, ImageTk

root = tk.Tk()
root.maxsize(900, 600)
root.title('Tkinter Hub')

options_frame = tk.Frame(root, bg='#c3c3c3')

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=200, height=900)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=900, width=600)

home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=10,y=50)

home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=3, y=50, width=5, height=40)

history_btn = tk.Button(options_frame, text='History', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3' , command=lambda: indicate(history_indicate, history_page))
history_btn.place(x=10,y=100)

history_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
history_indicate.place(x=3, y=100, width=5, height=40)

msg_btn = tk.Button(options_frame, text='Send a Message', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(msg_indicate, msg_page))
msg_btn.place(x=10,y=150)

msg_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
msg_indicate.place(x=3, y=150, width=5, height=40)

def home_page():
    home_frame = tk.Frame(main_frame)
    home_frame.pack()

    label = tk.Label(home_frame, width=500, height=500)
    label.pack()

    cap = cv2.VideoCapture(0)
    def update_frame():
        ret, home_frame = cap.read()
        if ret:
            home_frame = cv2.resize(home_frame, (500, 500)) # resize the frame to 200x200
            img = cv2.cvtColor(home_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            label.imgtk = imgtk
            label.configure(image=imgtk)
        root.after(10, update_frame)
    update_frame()

def history_page():
    history_frame = tk.Frame(main_frame)

    first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
    last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

    # treeview 
    table = ttk.Treeview(history_frame, columns = ('first', 'last', 'email'), show = 'headings')
    table.heading('first', text = 'First name')
    table.heading('last', text = 'Surname')
    table.heading('email', text = 'Email')
    table.pack(fill = 'both', expand = True)

    # insert values into a table
    # table.insert(parent = '', index = 0, values = ('John', 'Doe', 'JohnDoe@email.com'))
    for i in range(100):
        first = choice(first_names)
        last = choice(last_names)
        email = f'{first[0]}{last}@email.com'
        data = (first, last, email)
        table.insert(parent = '', index = 0, values = data)

    table.insert(parent = '', index = tk.END, values = ('XXXXX', 'YYYYY', 'ZZZZZ'))

    # events
    def item_select(_):
        print(table.selection())
        for i in table.selection():
            print(table.item(i)['values'])
        # table.item(table.selection())

    def delete_items(_):
        print('delete')
        for i in table.selection():
            table.delete(i)

    table.bind('<<TreeviewSelect>>', item_select)
    table.bind('<Delete>', delete_items)
    history_frame.pack()


def msg_page():
    msg_frame = tk.Frame(main_frame)

    lb = tk.Label(msg_frame, text='Send a Message.', font=('Bold', 30))
    lb.pack()

    msg_frame.pack(pady=20)

def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    history_indicate.config(bg='#c3c3c3')
    msg_indicate.config(bg='#c3c3c3')

def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_page()
    page()

root.mainloop()