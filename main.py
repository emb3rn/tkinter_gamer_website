import tkinter as tk

window = tk.Tk("Website", None)
window.configure(background="white")
window.geometry("1000x800")

class colors:
    background = "#ECECEC"

main_frame = tk.Frame(window,
                      width=1000,
                      height=900,
                      bg=colors.background,
                      highlightbackground="black",
                      highlightthickness=3).pack(padx=50, pady=50)

l_title    = tk.Label(main_frame,
                   text="Gamer's Website",
                   font=("Times New Roman Bold Italic", 34),
                   fg="#388E9A",
                   bg=colors.background).place(x=100, y=80)

l_desc     = tk.Label(main_frame,
                  text="Welcome to our website. In order to play our games you need to complete the registration form below.", 
                  font=("Arial Regular", 16),
                  fg="black",
                  bg=colors.background,
                  wraplength=650,
                  justify=tk.LEFT).place(x=100, y=150)

n_offsets = {
    "x": -20,
    "y": -20
}

f_first_name = tk.LabelFrame(main_frame,
                             width=200,
                             height=40,
                             bg=colors.background,
                             highlightbackground="black",
                             highlightthickness=1,
                             border=0).place(x=100, y=250)

l_first_name = tk.Label(f_first_name,
                        text="First Name",
                        fg="black",
                        bg=colors.background,
                        font=("Arial Regular", 12)).place(x=105, y=255)

f_last_name = tk.LabelFrame(main_frame,
                             width=200,
                             height=40,
                             bg=colors.background,
                             highlightbackground="black",
                             highlightthickness=1,
                             border=0).place(x=100, y=300)

l_last_name = tk.Label(f_first_name,
                        text="Last Name",
                        fg="black",
                        bg=colors.background,
                        font=("Arial Regular", 12)).place(x=105, y=305)

e_first_name = tk.Entry(main_frame,
                        font=("Arial Regular", 24),
                        width=20,
                        highlightbackground="black",
                        highlightthickness=1,
                        border=0).place(x=305, y=250)

e_last_name = tk.Entry(main_frame,
                        font=("Arial Regular", 24),
                        width=20,
                        highlightbackground="black",
                        highlightthickness=1,
                        border=0).place(x=305, y=300)

b_quit = tk.Button(main_frame,
                   text="QUIT",
                   font=("Arial Regular", 10),
                   height=2,
                   width=12,
                   highlightbackground="#000000",
                   highlightthickness=5,
                   border=0).place(x=650, y=650)

b_submit = tk.Button(main_frame,
                   text="SUBMIT",
                   font=("Arial Regular", 10),
                   height=2,
                   width=12,
                   highlightbackground="black",
                   highlightthickness=5,
                   border=0).place(x=775, y=650)



window.mainloop()