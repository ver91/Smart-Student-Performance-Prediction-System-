import tkinter as tk
from tkinter import messagebox
win = tk.Tk()
win.title("Smart Student Performance Prediction System")
win.state("zoomed")
win.configure(bg="#EAF2F8")

def number(value):
    if value == "":
        return True
    if value.isdigit():
        return True
    print("Invalid Input: Numbers only!")
    messagebox.showerror("Invalid Input", "Numbers only!")
    return False

def text(value):
    if value == "":
        return True
    if all(x.isalpha() or x.isspace() for x in value):
        return True
    print("Invalid Input: Letters only!")
    messagebox.showerror("Invalid Input", "Letters only!")
    return False

def decimal(value):
    if value == "":
        return True
    try:
        float(value)
        return True
    except:
        print("Invalid Input: Numbers only!")
        messagebox.showerror("Invalid Input", "Numbers only!")
        return False

def clear():
    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    for entry in a.winfo_children():
        if isinstance(entry, tk.Entry):
            entry.delete(0, tk.END)
    prediction.config(state="normal")
    prediction.delete(0, tk.END)
    prediction.config(state="readonly")
    risk.config(state="normal")
    risk.delete(0, tk.END)
    risk.config(state="readonly")
    recommendation.config(state="normal")
    recommendation.delete("1.0", tk.END)
    recommendation.config(state="disabled")

num = win.register(number)
txt = win.register(text)
dec = win.register(decimal)

tk.Label(win, text="SMART STUDENT PERFORMANCE PREDICTION SYSTEM",font=("Arial", 28, "bold"),bg="#EAF2F8",fg="#154360").pack(pady=25)

top = tk.Frame(win)
top.pack(fill="both", expand=False, padx=25)

s = tk.LabelFrame(top, text="Student Information",font=("Arial", 16, "bold"),  bg="#D6EAF8",fg="#154360")
s.pack(side="left", fill="both", expand=True, padx=10)

tk.Label(s, text="Student ID",font=("Arial", 13)).grid(row=0, column=0, padx=30, pady=35)

student_id = tk.Entry(s, font=("Arial", 13),bg="white",validate="key",validatecommand=(num, "%P"))
student_id.grid(row=0, column=1, sticky="ew")

tk.Label(s, text="Student Name",font=("Arial", 13)).grid(row=1, column=0, padx=30, pady=35)

student_name = tk.Entry(s, font=("Arial", 13),bg="white",validate="key", validatecommand=(txt, "%P"))
student_name.grid(row=1, column=1, sticky="ew")

s.columnconfigure(1, weight=1)

a = tk.LabelFrame(top, text="Academic Information",font=("Arial", 16, "bold"),bg="#D6EAF8",fg="#154360")
a.pack(side="left", fill="both", expand=True, padx=10)

fields = ["Attendance (%)", "Study Hours (per day)","Internal Marks (%)", "Assignment (%)","Previous Score (%)"]

for i, field in enumerate(fields):
    tk.Label(a, text=field,font=("Arial", 13)).grid(row=i, column=0,padx=20, pady=15)

    tk.Entry(a, font=("Arial", 13),validate="key",validatecommand=(dec, "%P")).grid(row=i, column=1, sticky="ew")

a.columnconfigure(1, weight=1)

buttons = tk.Frame(win)
buttons.pack(pady=20)

tk.Button(buttons, text="Predict Performance",width=22, font=("Arial", 13),bg="#3498DB", fg="white").pack(side="left", padx=25)

tk.Button(buttons, text="Clear", width=15,font=("Arial", 13),bg="#F39C12", fg="white", command=clear).pack(side="left", padx=25)
tk.Button(buttons, text="Exit",width=15, font=("Arial", 13),bg="#E74C3C", fg="white",command=win.destroy).pack(side="left", padx=25)

r = tk.LabelFrame(win, text="Prediction Results",font=("Arial", 16, "bold"),bg="#D5F5E3",fg="#196F3D")
r.pack(fill="x", padx=25, pady=5)
tk.Label(r, text="Prediction:",font=("Arial", 13)).grid(row=0, column=0, padx=25, pady=15)
prediction = tk.Entry(r, font=("Arial", 13), state="readonly")
prediction.grid(row=0, column=1, sticky="ew")
tk.Label(r, text="Risk Level:",font=("Arial", 13)).grid(row=1, column=0, padx=25, pady=15)
risk = tk.Entry(r, font=("Arial", 13), state="readonly")
risk.grid(row=1, column=1, sticky="ew")
tk.Label(r, text="Recommendation:",font=("Arial", 13)).grid(row=2, column=0, padx=25, pady=15)

recommendation = tk.Text(r,font=("Arial", 13),width=70,height=3,state="disabled")
recommendation.grid(row=2, column=1, sticky="nsew")

r.columnconfigure(1, weight=1)

win.mainloop()