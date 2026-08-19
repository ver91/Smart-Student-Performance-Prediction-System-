import tkinter as tk
from tkinter import messagebox
import pickle
import pandas as pd

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
    
def load_model():

    global model
    global model_name

    try:

        with open(
            "student_performance_model.pkl",
            "rb"
        ) as file:

            model_package = pickle.load(file)

        model = model_package["model"]
        model_name = model_package["model_name"]

        messagebox.showinfo(
            "Model Loaded",
            "Logistic Regression model loaded successfully!"
        )

        print("==========================================")
        print("MODEL LOADED SUCCESSFULLY")
        print("Algorithm:", model_name)
        print("==========================================")

    except FileNotFoundError:

        messagebox.showerror(
            "Model Not Found",
            "student_performance_model.pkl was not found.\n\n"
            "Please train the model first."
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            "Unable to load model.\n\n" + str(e)
        )
        
def save_to_excel(
    sid,
    name,
    attendance,
    study_hours,
    internal_marks,
    assignment,
    previous_score,
    performance,
    risk_level,
    recommendation_text
):

    output_file = "student_data_changed.xlsx"

    new_data = pd.DataFrame([
        {
            "Student ID": sid,
            "Student Name": name,
            "Attendance": attendance,
            "Study Hours": study_hours,
            "Internal Marks": internal_marks,
            "Assignment": assignment,
            "Previous Score": previous_score,
            "Performance": performance,
            "Risk Level": risk_level,
            "Recommendation": recommendation_text
        }
    ])

    try:

        existing_data = pd.read_excel(output_file)

        final_data = pd.concat(
            [existing_data, new_data],
            ignore_index=True
        )

    except FileNotFoundError:

        final_data = new_data

    final_data.to_excel(
        output_file,
        index=False
    )

    messagebox.showinfo(
        "Prediction Saved",
        "Prediction completed successfully!\n\n"
        "Result saved to:\n"
        "student_data_changed.xlsx"
    )

def predict_performance():

    try:

        sid = student_id.get()
        name = student_name.get()

        if sid == "" or name == "":
            messagebox.showerror(
                "Missing Information",
                "Please enter Student ID and Student Name."
            )
            return
        if "model" not in globals():

            messagebox.showerror(
                "Model Not Loaded",
                "Please click the Load button first."
            )

            return

        attendance = float(
            academic_entries[0].get()
        )

        study_hours = float(
            academic_entries[1].get()
        )

        internal_marks = float(
            academic_entries[2].get()
        )

        assignment = float(
            academic_entries[3].get()
        )

        previous_score = float(
            academic_entries[4].get()
        )

        input_data = pd.DataFrame(
    [[
        attendance,
        study_hours,
        internal_marks,
        assignment,
        previous_score
    ]],
    columns=[
        "Attendance",
        "Study Hours",
        "Internal Marks",
        "Assignment",
        "Previous Score"
    ]
)
        performance = model.predict(
            input_data
        )[0]
        if performance == "Excellent":

            risk_level = "Low"

            recommendation_text = (
                "Keep up the excellent performance."
            )

        elif performance == "Good":

            risk_level = "Low"

            recommendation_text = (
                "Good performance. Continue regular studies."
            )

        elif performance == "Average":

            risk_level = "Medium"

            recommendation_text = (
                "Improve attendance, study hours "
                "and academic practice."
            )

        else:

            risk_level = "High"

            recommendation_text = (
                "Needs immediate improvement "
                "and regular guidance."
            )
            
        save_to_excel(
    sid,
    name,
    attendance,
    study_hours,
    internal_marks,
    assignment,
    previous_score,
    performance,
    risk_level,
    recommendation_text
)
        prediction.config(
            state="normal"
        )

        prediction.delete(
            0,
            tk.END
        )

        prediction.insert(
            0,
            performance
        )

        prediction.config(
            state="readonly"
        )
        risk.config(
            state="normal"
        )

        risk.delete(
            0,
            tk.END
        )

        risk.insert(
            0,
            risk_level
        )

        risk.config(
            state="readonly"
        )
        recommendation.config(
            state="normal"
        )

        recommendation.delete(
            "1.0",
            tk.END
        )

        recommendation.insert(
            "1.0",
            recommendation_text
        )

        recommendation.config(
            state="disabled"
        )
        print("==========================================")
        print("SMART STUDENT PERFORMANCE SYSTEM")
        print("==========================================")

        print("Student ID       :", sid)
        print("Student Name     :", name)

        print("\nAcademic Information")

        print(
            "Attendance       :",
            attendance,
            "%"
        )

        print(
            "Study Hours      :",
            study_hours,
            "hours/day"
        )

        print(
            "Internal Marks   :",
            internal_marks,
            "%"
        )

        print(
            "Assignment       :",
            assignment,
            "%"
        )

        print(
            "Previous Score   :",
            previous_score,
            "%"
        )

        print("\nPrediction Information")

        print(
            "Prediction       :",
            performance
        )

        print(
            "Risk Level       :",
            risk_level
        )

        print(
            "Recommendation   :",
            recommendation_text
        )

        print(
            "Model            :",
            model_name
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter values in all academic fields."
        )
def clear():
    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    for entry in academic_entries:
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
tk.Label(win,text="SMART STUDENT PERFORMANCE PREDICTION SYSTEM",font=("Arial", 28, "bold"),bg="#EAF2F8",fg="#154360").pack(pady=25)
top = tk.Frame(win)
top.pack(fill="both", expand=False, padx=25)
s = tk.LabelFrame(top,text="Student Information",font=("Arial", 16, "bold"),bg="#D6EAF8",fg="#154360")
s.pack(side="left", fill="both", expand=True, padx=10)
tk.Label(s,text="Student ID",font=("Arial", 13)).grid(row=0, column=0, padx=30, pady=35)
student_id = tk.Entry(s,font=("Arial", 13),bg="white",validate="key",validatecommand=(num, "%P"))
student_id.grid(row=0, column=1, sticky="ew")
tk.Label(s,text="Student Name",font=("Arial", 13)).grid(row=1, column=0, padx=30, pady=35)
student_name = tk.Entry(s,font=("Arial", 13),bg="white",validate="key",validatecommand=(txt, "%P"))
student_name.grid(row=1, column=1, sticky="ew")
s.columnconfigure(1, weight=1)
a = tk.LabelFrame( top, text="Academic Information", font=("Arial", 16, "bold"), bg="#D6EAF8", fg="#154360")
a.pack(side="left", fill="both", expand=True, padx=10)
fields = [
    "Attendance (%)",
    "Study Hours (per day)",
    "Internal Marks (%)",
    "Assignment (%)",
    "Previous Score (%)"
]
academic_entries = []

for i, field in enumerate(fields):
    tk.Label(
        a,
        text=field,
        font=("Arial", 13)
    ).grid(
        row=i,
        column=0,
        padx=20,
        pady=15
    )
    entry = tk.Entry(
        a,
        font=("Arial", 13),
        validate="key",
        validatecommand=(dec, "%P")
    )
    entry.grid(
        row=i,
        column=1,
        sticky="ew"
    )
    academic_entries.append(entry)
a.columnconfigure(1, weight=1)
buttons = tk.Frame(win)
buttons.pack(pady=20)
tk.Button(
    buttons,
    text="Load",
    width=18,
    font=("Arial", 13),
    bg="#8E44AD",
    fg="white",
    command=load_model
).pack(side="left", padx=15)
tk.Button(buttons,text="Predict Performance",width=22,font=("Arial", 13),bg="#3498DB",fg="white",command=predict_performance).pack(side="left", padx=25)
tk.Button(buttons,text="Clear",width=15,font=("Arial", 13),bg="#F39C12",fg="white",command=clear).pack(side="left", padx=25)
tk.Button(buttons,text="Exit", width=15, font=("Arial", 13), bg="#E74C3C", fg="white", command=win.destroy).pack(side="left", padx=25)
r = tk.LabelFrame(win,text="Prediction Results",font=("Arial", 16, "bold"),bg="#D5F5E3",fg="#196F3D")
r.pack(fill="x", padx=25, pady=5)
tk.Label(r,text="Prediction:",font=("Arial", 13)).grid(row=0, column=0, padx=25, pady=15)
prediction = tk.Entry(r,font=("Arial", 13),state="readonly")
prediction.grid(row=0, column=1, sticky="ew")
tk.Label(r,text="Risk Level:",font=("Arial", 13)).grid(row=1, column=0, padx=25, pady=15)
risk = tk.Entry(r,font=("Arial", 13),state="readonly")
risk.grid(row=1, column=1, sticky="ew")
tk.Label(r,text="Recommendation:",font=("Arial", 13)).grid(row=2, column=0, padx=25, pady=15)
recommendation = tk.Text(r,font=("Arial", 13),width=70,height=3,state="disabled")
recommendation.grid(row=2, column=1, sticky="nsew")
r.columnconfigure(1, weight=1)
win.mainloop()