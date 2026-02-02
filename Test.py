import tkinter

window = tkinter.Tk()

window.title("Test")
window.geometry("500x800+500+200")
window.resizable(True, True)

op = ""

def tal():
    global op
    op += "자동차 세계로 오신 걸 환영합니다. "
    label1.config(text=op)

label = tkinter.Label(window, text="🚗 Welcome Car Project 🚗", relief="solid", width=22, height=2, state="active", activebackground="green", activeforeground="white")
label.pack()

entry = tkinter.Entry(window, justify="center")
entry.pack()

label1 = tkinter.Label(window)
label1.pack()

button = tkinter.Button(window, overrelief="solid", width=12, text="메시지 확인하기", compound="left", command=tal)
button.pack()

listbox = tkinter.Listbox(window, selectmode = 'extended', height=3)
listbox.insert(0, "현대")
listbox.insert(1, "기아")
listbox.insert(2, "대우")
listbox.pack()

label2 = tkinter.Label(window, text="당신은 자동차를 좋아합니까?")
label2.pack()
check1 = tkinter.Checkbutton(window, text="예")
check1.pack()
check2 = tkinter.Checkbutton(window, text="아니요")
check2.pack()

window.mainloop()