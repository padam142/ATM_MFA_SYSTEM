from tkinter import * 
from tkinter import ttk

class otp_auth_atm:
    def __init__(self, window):
        window.geometry("380x538+812+80")
        window.resizable(0, 0)
        window.configure(background="#0dd754")

        # Frame 2 - Design Purpose (Cash out Frame)
        self.frame2 = Frame(window, relief='groove', borderwidth=2, background="#d9d9d9")
        self.frame2.place(relx=0.282, rely=0.866, relheight=0.065
                          , relwidth=0.405)

        # Frame 3 - Design Purpose (Up Frame after word ATM)
        self.frame3 = Frame(window, relief='groove', background="#43c04d")
        self.frame3.place(relx=0.0, rely=0.102, relheight=0.046
                          , relwidth=1.011)

        # Frame 7 - ATM Screen main frame
        self.frame7 = Frame(window, relief="groove", background="#3cc851")
        self.frame7.place(relx=0.071, rely=0.112, relheight=0.418
                          , relwidth=0.853)

        # Frame 8 - Design Purpose (ATM Screen)
        self.frame8 = Frame(self.frame7, relief="groove", background="#e1e1e1", borderwidth="2")
        self.frame8.place(relx=0.160, rely=0.044, relheight=0.689
                          , relwidth=0.691)

        # Frame 6 - Design Purpose (ATM Keypad main Frame)
        self.frame6 = Frame(window, relief="groove", background="#50b461")
        self.frame6.place(relx=0.079, rely=0.485, relheight=0.299
                          , relwidth=0.853)

        # Frame 9 - Design Purpose (ATM Keypad)
        self.frame9 = Frame(self.frame6, relief="groove", background="#e1e1e1", borderwidth="2")
        self.frame9.place(relx=0.16, rely=0.041, relheight=0.925, relwidth=0.66)

        # Label 1 - Design Purpose
        self.label1 = Label(window, background="#0dd754",
                            font="-family {Segoe UI Variable Display Semib} -size 20 -weight bold",
                            foreground="#ffffff", text='''ATM''')
        self.label1.place(relx=0.263, rely=0.019, height=41, width=173)

        # Frame 4 - Design Purpose (Left Border Frame)
        self.frame4 = Frame(window, relief="groove", background="#43c04d")
        self.frame4.place(relx=0.0, rely=0.112, relheight=0.678
                          , relwidth=0.092)

        # Frame 5 - Design Purpose (Right Border Frame)
        self.frame5 = Frame(window, relief="groove", background="#43c04d")
        self.frame5.place(relx=0.921, rely=0.112, relheight=0.678
                          , relwidth=0.092)

        # Frame 1 - Design Purpose (Down Frame)
        self.frame1 = Frame(window, relief="groove", borderwidth=2, background="#0dd754")
        self.frame1.place(relx=-0.003, rely=0.786, relheight=0.214, relwidth=1.011)

        # Button 1 - Top Screen Left - 1
        self.button1 = Button(self.frame7, background="#d9d9d9", borderwidth=0)
        self.button1.place(relx=0.049, rely=0.20, height=24, width=27)

        # Button 2 - Top Screen Left - 2
        self.button2 = Button(self.frame7, background="#d9d9d9", borderwidth=0)
        self.button2.place(relx=0.049, rely=0.400, height=24, width=27)

        # Button 3 - Top Screen Left - 3
        self.button3 = Button(self.frame7, background="#d9d9d9", borderwidth=0)
        self.button3.place(relx=0.049, rely=0.600, height=24, width=27)

        # Button 01 - Top Screen Right - 1
        self.Button01 = Button(self.frame7, background="#d9d9d9", borderwidth=0)
        self.Button01.place(relx=0.88, rely=0.600, height=24, width=27)

        # Button 02 - Top Screen Right - 2
        self.Button02 = Button(self.frame7, background="#d9d9d9", borderwidth=0)
        self.Button02.place(relx=0.88, rely=0.400, height=24, width=27)

        # Button 03 - Top Screen Right - 3
        self.Button03 = Button(self.frame7, background="#d9d9d9", borderwidth=0)
        self.Button03.place(relx=0.88, rely=0.200, height=24, width=27)
        
        # Button 001 - Keypad numbers
        self.button001 = ttk.Button(self.frame9, text="1")
        self.button001.place(relx=0.050, rely=0.030, height=35, width=46)

        # Button 002 - Keypad numbers
        self.button002 = ttk.Button(self.frame9, text="2")
        self.button002.place(relx=0.270, rely=0.030, height=35, width=46)

        # Button 003 - Keypad numbers
        self.button003 = ttk.Button(self.frame9, text="3")
        self.button003.place(relx=0.490, rely=0.030, height=35, width=46)

        # Button 004 - Keypad numbers
        self.button004 = ttk.Button(self.frame9, text="4")
        self.button004.place(relx=0.050, rely=0.260, height=35, width=46)

        # Button 005 - Keypad numbers
        self.button005 = ttk.Button(self.frame9, text="5")
        self.button005.place(relx=0.270, rely=0.260, height=35, width=46)

        # Button 006 - Keypad numbers
        self.button006 = ttk.Button(self.frame9, text="6")
        self.button006.place(relx=0.490, rely=0.260, height=35, width=46)

        # Button 007 - Keypad numbers
        self.button007 = ttk.Button(self.frame9, text="7")
        self.button007.place(relx=0.050, rely=0.500, height=35, width=46)

        # Button 008 - Keypad numbers
        self.button008 = ttk.Button(self.frame9, text="8")
        self.button008.place(relx=0.270, rely=0.500, height=35, width=46)

        # Button 009 - Keypad numbers
        self.button009 = ttk.Button(self.frame9, text="9")
        self.button009.place(relx=0.490, rely=0.500, height=35, width=46)

        # Button 010 - Keypad numbers
        self.button010 = ttk.Button(self.frame9, text=" ")
        self.button010.place(relx=0.050, rely=0.740, height=35, width=46)

        # Button 000 - Keypad numbers
        self.button000 = ttk.Button(self.frame9, text="0")
        self.button000.place(relx=0.270, rely=0.740, height=35, width=46)

        # Button 011 - Keypad numbers
        self.button011 = ttk.Button(self.frame9, text=" ")
        self.button011.place(relx=0.490, rely=0.740, height=35, width=46)

        

if __name__ == "__main__":
    window = Tk()
    otp_auth_atm(window)
    window.mainloop()