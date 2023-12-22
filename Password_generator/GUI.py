import tkinter as tk
from customtkinter import *
from Password_generator import *

class Frame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label for password generator
        self.title = CTkLabel(self, text='Password Generator', font=('Helvetica', 16, 'bold'))
        self.title.grid(row=0, column=0, padx=(10,10), pady=(10, 10), sticky="nse")

        # Slider for length of password
        self.slider = CTkSlider(master=self, from_=5, to=20, command=self.slider_event)
        self.slider.grid(row=1, column=0, padx=(10,10), pady=(10, 10), sticky="nse")
        self.slider.set(5)
        
        # Slider Label
        self.text_var_length = tk.IntVar(value=5)
        self.slider_label = CTkLabel(self, textvariable=self.text_var_length, font=('Helvetica', 16, 'bold'),text_color='white')
        self.slider_label.grid(row=1, column=1, padx=(10,10), pady=(10, 10), sticky="nse")

        # Checkbox if user wants to use letters in password
        self.checkbox_var_1 = tk.BooleanVar()
        checkbox_1_text = 'Use letters'
        self.checkbox_1 = CTkCheckBox(master=self, text=checkbox_1_text, variable=self.checkbox_var_1, 
                               fg_color='#4158D0', hover_color='#C850C0', checkbox_height=20, checkbox_width=20, corner_radius=15)
        self.checkbox_1.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Checkbox if user wants to use numbers in password
        self.checkbox_var_2 = tk.BooleanVar()
        checkbox_2_text = 'Use numbers'
        self.checkbox_2 = CTkCheckBox(master=self, text=checkbox_2_text, variable=self.checkbox_var_2, 
                               fg_color='#4158D0', hover_color='#C850C0', checkbox_height=20, checkbox_width=20, corner_radius=15)
        self.checkbox_2.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        
        # Checkbox if user wants to use special signs in password
        self.checkbox_var_3 = tk.BooleanVar()
        checkbox_3_text = 'Use special sign'
        self.checkbox_3 = CTkCheckBox(master=self, text=checkbox_3_text, variable=self.checkbox_var_3, 
                               fg_color='#4158D0', hover_color='#C850C0', checkbox_height=20, checkbox_width=20, corner_radius=15)
        self.checkbox_3.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        
        button = CTkButton(master=self, text="Generate Password", command=self.button_function)
        button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        self.text_var_password = tk.StringVar(value='')
        self.password_label = CTkLabel(self, textvariable=self.text_var_password, font=('Helvetica', 16, 'bold'), text_color='white')
        self.password_label.grid(row=6, column=0, padx=(10,10), pady=(10, 10), sticky="nsew")



    def slider_event(self, value):
        self.text_var_length.set(f'{int(self.slider.get())}')
        

    def button_function(self):
        unique_password = Password(int(self.slider.get()),self.checkbox_1.get(),self.checkbox_2.get(),self.checkbox_3.get())
        self.text_var_password.set(f'{unique_password.set_password()}')
        

class Program(CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Password Generator")
        self.geometry('400x300')
        self.configure(fg_color=('#E7E9F1','#18122B')) 
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        set_appearance_mode("dark")  # Modes: system (default), light, dark
        set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)




if __name__ == "__main__":
    window = Program()
    window.mainloop()
