import tkinter as tk
from tkinter import ttk

def display():
    tot = 0
    grades = {'A': 40, 'B': 36, 'C': 32, 'D': 28, 'P': 24, 'F': 0}
    subjects = [e4, e5, e6, e7]
    row = 3

    for e in subjects:
        grade = e.get().upper()
        credit = grades.get(grade, 0)
        tk.Label(master, text=str(credit), font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=row, column=4)
        tot += credit
        row += 1

    tk.Label(master, text=str(tot), font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=7, column=4)
    tk.Label(master, text=f"{tot/15:.2f}", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=8, column=4)

master = tk.Tk()
master.title("MARKSHEET")
master.geometry("700x300")
master.configure(bg='#641b30')

# Styling
style = ttk.Style(master)
style.theme_use("clam")
style.configure("TButton", background="#4CAF50", foreground="white", font=('Times New Roman', 12, 'bold'))
style.configure("TLabel", background="#641b30", foreground="white", font=('Times New Roman', 12))
style.configure("TEntry", font=('Times New Roman', 12))

tk.Label(master, text="Name", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=0, column=0)
tk.Label(master, text="Reg.No", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=0, column=3)
tk.Label(master, text="Roll.No", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=1, column=0)

tk.Label(master, text="Srl.No", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=2, column=0)
tk.Label(master, text="1", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=3, column=0)
tk.Label(master, text="2", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=4, column=0)
tk.Label(master, text="3", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=5, column=0)
tk.Label(master, text="4", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=6, column=0)

tk.Label(master, text="Subject", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=2, column=1)
tk.Label(master, text="Social", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=3, column=1)
tk.Label(master, text="Science", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=4, column=1)
tk.Label(master, text="Maths", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=5, column=1)
tk.Label(master, text="English", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=6, column=1)

tk.Label(master, text="Grade", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=2, column=2)
e4 = ttk.Entry(master)
e5 = ttk.Entry(master)
e6 = ttk.Entry(master)
e7 = ttk.Entry(master)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)

tk.Label(master, text="Sub Credit", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=2, column=3)
tk.Label(master, text="4", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=3, column=3)
tk.Label(master, text="4", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=4, column=3)
tk.Label(master, text="3", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=5, column=3)
tk.Label(master, text="4", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=6, column=3)

tk.Label(master, text="Credit obtained", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=2, column=4)

e1 = ttk.Entry(master)
e2 = ttk.Entry(master)
e3 = ttk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)

button1 = ttk.Button(master, text="Submit", command=display)
button1.grid(row=8, column=1)

tk.Label(master, text="Total credit", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=7, column=3)
tk.Label(master, text="SGPA", font=('Times New Roman', 12), bg='#641b30', fg='white').grid(row=8, column=3)

master.mainloop()
