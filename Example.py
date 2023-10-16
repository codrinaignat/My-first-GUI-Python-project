import tkinter as tk

userInt = tk.Tk()
userInt.geometry("500x400")
userInt.title("My calculator")
label = tk.Label(userInt, text="My calculator", font=('Times New Roman', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(userInt, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

#button = tk.Button(root, text="Click me!", font=('Arial', 18))
#button.pack(padx=10, pady=10)

buttonFrame = tk.Frame(userInt)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text="1", font=('Times New Roman', 18), bg='red')
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonFrame, text="2", font=('Times New Roman', 18), bg='green')
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame, text="3", font=('Times New Roman', 18), bg='blue')
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text="4", font=('Times New Roman', 18), bg='green')
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text="5", font=('Times New Roman', 18), bg='red')
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="6", font=('Times New Roman', 18), bg='pink')
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text="7", font=('Times New Roman', 18), bg='blue')
btn4.grid(row=2, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text="8", font=('Times New Roman', 18), bg='green')
btn5.grid(row=2, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="9", font=('Times New Roman', 18), bg='red')
btn6.grid(row=2, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text="0", font=('Times New Roman', 18), bg='green')
btn4.grid(row=3, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text="+", font=('Times New Roman', 18), bg='pink')
btn5.grid(row=3, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="-", font=('Times New Roman', 18), bg='blue')
btn6.grid(row=3, column=2, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="*", font=('Times New Roman', 18), bg='pink')
btn6.grid(row=4, column=0, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="/", font=('Times New Roman', 18), bg='blue')
btn6.grid(row=4, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="=", font=('Times New Roman', 18), bg='pink')
btn6.grid(row=4, column=2, sticky=tk.W+tk.E)

buttonFrame.pack(fill='x')

#myentry = tk.Entry(root)
#myentry.pack()

userInt.mainloop()