from tkinter import *
def main():

    def harcknow(): # Definide "harck" executor (on right click on harck button)
        harck_window = Tk()
        harck_window.geometry("240x140")
        harck_window.resizable(False, False)
        harck_window.title("Suces !")
        success = Label(harck_window, text=" BIN AKÉ", font=("arial", 20, "bold"), fg="black").place(x=0, y=50)
    window = Tk()
    window.geometry("720x480")
    window.resizable(False, False)
    window.title("HARCK EVERYONE")
    harck = Label(window, text="SE LOGICIÈL PE AKÉ TUTE PERSONE !!!!!!!!!!!!!!!!!!!!!!!!!", font=("arial", 20, "bold"), fg="black").place(x=10, y=100)
    harcknow = Button(window, text="AKE !!!!!!!!!!", width=30, height=5, bg="white", command=harcknow).place(x=120, y=250)
    mainloop()


if __name__ == '__main__':
    main()
