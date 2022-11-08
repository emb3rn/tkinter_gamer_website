#MACOS VERSION
import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk("Website", None)
window.configure(background="white")
window.geometry("1000x900")

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

#NAME INPUT

name_text = ["First name", "Last name"]

for name in range(0,2):
    frame = tk.LabelFrame(main_frame,
                            width=200,
                            height=40,
                            bg=colors.background,
                            highlightbackground="black",
                            highlightthickness=1,
                            border=0).place(x=100, y=250+name*50)

    name = tk.Label(frame,
                        text=name_text[name],
                        fg="black",
                        bg=colors.background,
                        font=("Arial Regular", 12)).place(x=105, y=255+name*50)    

#ENTRY BOXES
for entry in range(0, 2):
    entry = tk.Entry(main_frame,
                        font=("Arial Regular", 30),
                        width=20,
                        highlightbackground="black",
                        highlightthickness=1,
                        border=0,
                        bg="white",
                        fg="black").place(x=305, y=250+entry*50)

#GENDER SELECTION
l_gender = tk.Label(text="Gender?",
                    font=("Arial Regular", 14),
                    fg="black",
                    bg=colors.background).place(x=95, y=375)

rb_options = ["Male", "Female", "Prefer not to say"]

for option in range(0,3):
    radio_button = tk.Radiobutton(text=f"  {rb_options[option]}",
                            font=("Arial Regular", 14),
                            fg="black",
                            bg=colors.background)
    radio_button.place(x=95, y=(420+option*40))
 

#KIND OF GAMES
l_games_play = tk.Label(text="Which games do you like to play?",
                    font=("Arial Regular", 14),
                    fg="black",
                    bg=colors.background).place(x=500, y=375)

cb_names = ["Quizzes", "Cards", "Dice", "Other"]

for name in range(0,4):
    checkbox = tk.Checkbutton(text=cb_names[name],
                            font=("Arial Regular", 14),
                            fg="black",
                            bg=colors.background)
    checkbox.place(x=500, y=(415 + name*40))

#AGE SELECTION

l_games_play = tk.Label(text="Age? If over 30 choose 30.",
                    font=("Arial Regular", 14),
                    fg="black",
                    bg=colors.background).place(x=95, y=575)

s_age_slider = tk.Scale(main_frame,
                        from_=0,
                        to=30,
                        font=("Arial Regular", 10),
                        digits=True,
                        fg="black",
                        bg=colors.background,
                        orient="horizontal").place(x=95, y=600)

#QUIT/SUBMIT BUTTONS
b_quit = tk.Button(main_frame,
                   text="QUIT",
                   font=("Arial Regular", 10),
                   height=2,
                   width=12,
                   highlightbackground="#000000",
                   border=0,
                   highlightthickness=1).place(x=650, y=750)

b_submit = tk.Button(main_frame,
                   text="SUBMIT",
                   font=("Arial Regular", 10),
                   height=2,
                   width=12,
                   highlightbackground="black",
                   border=0,
                   highlightthickness=1).place(x=775, y=750)



window.mainloop()