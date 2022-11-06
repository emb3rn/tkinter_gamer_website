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
                   font=("Times New Roman Bold Italic", 40),
                   fg="#388E9A",
                   bg=colors.background).place(x=100, y=100)

l_desc     = tk.Label(main_frame,
                  text="Welcome to our website. In order to play our games you need to complete the registration form below.", 
                  font=("Arial Regular", 18),
                  fg="black",
                  bg=colors.background,
                  wraplength=550,
                  justify=tk.LEFT).place(x=100, y=160)

f_first_name = tk.LabelFrame(main_frame,
                             width=200,
                             height=40,
                             bg=colors.background).place(x=100, y=250)

l_first_name = tk.Label(f_first_name,
                        text="First Name",
                        fg="black",
                        bg=colors.background,
                        font=("Arial Regular", 17)).place(x=105, y=255)
window.mainloop()
