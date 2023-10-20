import tkinter as tk

userInt = tk.Tk()
userInt.geometry("300x500")
userInt.title("My calculator")
userInt.configure(bg='pink')
label = tk.Label(userInt, text="My calculator", font=('Times New Roman', 18), bg='pink')
label.pack(padx=20, pady=20)

textbox = tk.Text(userInt, height=5, font=('Arial', 16), state='disabled')
textbox.pack(padx=10, pady=10)

#button = tk.Button(root, text="Click me!", font=('Arial', 18))
#button.pack(padx=10, pady=10)

buttonFrame = tk.Frame(userInt)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text="1", font=('Times New Roman', 18, 'bold'), bg='#E4C8D4', border='3')
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonFrame, text="2", font=('Times New Roman', 18, 'bold'), bg='#E4C8D4', border='3')
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame, text="3", font=('Times New Roman', 18, 'bold'), bg='#E4C8D4', border='3')
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text="4", font=('Times New Roman', 18, 'bold'), bg='#E4C8D4', border='3')
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text="5", font=('Times New Roman', 18, 'bold'), bg='#E4C8D4', border='3')
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="6", font=('Times New Roman', 18, 'bold'), bg='#E4C8D4', border='3')
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text="7", font=('Times New Roman', 18, 'bold'), bg='#E4C8D4', border='3')
btn4.grid(row=2, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text="8", font=('Times New Roman', 18, 'bold'), bg='#E4C8D4', border='3')
btn5.grid(row=2, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="9", font=('Times New Roman', 18, 'bold'), bg='#E4C8D4', border='3')
btn6.grid(row=2, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text="0", font=('Times New Roman', 18, 'bold'), bg='#E4C8D4', border='3')
btn4.grid(row=3, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text="+", font=('Times New Roman', 18, 'bold'), bg='#B3EB8A', border='3')
btn5.grid(row=3, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="-", font=('Times New Roman', 18, 'bold'), bg='#B3EB8A', border='3')
btn6.grid(row=3, column=2, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="*", font=('Times New Roman', 18, 'bold'), bg='#B3EB8A', border='3')
btn6.grid(row=4, column=0, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="/", font=('Times New Roman', 18, 'bold'), bg='#B3EB8A', border='3')
btn6.grid(row=4, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="=", font=('Times New Roman', 18, 'bold'), bg='#B3EB8A', border='3')
btn6.grid(row=4, column=2, sticky=tk.W+tk.E)

clearButton = tk.Button(buttonFrame, text='Clear', font=('Times New Roman', 18, 'bold'), bg='#bae1ff', border='3')
clearButton.grid(row=5, columnspan = 2, sticky=tk.W + tk.E)

decimalPoint = tk.Button(buttonFrame, text=".", font=('Times New Roman', 18, 'bold'), bg='#B3EB8A', border='3')
decimalPoint.grid(row=5, column=2, sticky=tk.W + tk.E)

buttonFrame.pack(fill='x')


userInt.mainloop()