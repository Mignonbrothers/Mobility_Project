import tkinter

window = tkinter.Tk()

window.title("Test")
window.geometry("500x800+500+200")
window.resizable(True, True)

menubar = tkinter.Menu(window)

menubutton = tkinter.Menubutton(window, text="자동차 회사", relief="raised", direction="right")
menubutton.pack(pady=(0,30))

op = ""

def tal():
    global op
    op += "자동차 세계로 오신 걸 환영합니다. "
    label1.config(text=op)

menu_1 = tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="하위 메뉴 1")
menu_1.add_checkbutton(label="Hi")
menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)


menu_2 = tkinter.Menu(menubutton, tearoff=0)
menu_2.add_checkbutton(label="Hyundai")
menu_2.add_checkbutton(label="Genesis")
menu_2.add_checkbutton(label="Kia")
menu_2.add_checkbutton(label="Ford")
# menubutton.add_cascade(label="상위 메뉴 1", menu=menu_2)

photo = tkinter.PhotoImage(file="image.png")

label0 = tkinter.Label(window, image=photo, width=700, height=500)
label0.pack(pady=(0,20))



label = tkinter.Label(window, text="🚗 Welcome Car Project 🚗", relief="solid", width=22, height=2, state="active", activebackground="green", activeforeground="white")
label.pack(pady=(0,20))


entry = tkinter.Entry(window, justify="center")
entry.pack(pady=(0,20))

label1 = tkinter.Label(window)
label1.pack(pady=(0,20))

button = tkinter.Button(window, overrelief="solid", width=12, text="메시지 확인하기", compound="left", command=tal)
button.pack(pady=(0,20))

listbox = tkinter.Listbox(window, selectmode = 'extended', height=3)
listbox.insert(0, "현대")
listbox.insert(1, "기아")
listbox.insert(2, "대우")
listbox.pack(pady=(0,20))

label2 = tkinter.Label(window, text="당신은 자동차를 좋아합니까?")
label2.pack(pady=(0,20))
check1 = tkinter.Checkbutton(window, text="예")
check1.pack()
check2 = tkinter.Checkbutton(window, text="아니요")
check2.pack()

# menu 창에 한정
window.config(menu=menubar)

# menubutton에 한정
menubutton["menu"]=menu_2

window.mainloop()