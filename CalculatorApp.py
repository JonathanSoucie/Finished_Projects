import customtkinter as ctk

#window
window = ctk.CTk(fg_color = ('#D7F0E9','#06142E'))
window.title('calculator')
window.geometry('600x400')
window.minsize(200,400)

expression = ''

#dark and light mode switch
def switch_event():
    if(switch_var.get() == 'on'):
        ctk.set_appearance_mode('Dark')
    else:
        ctk.set_appearance_mode('Light')              
switch_var = ctk.StringVar(value="on")
switch = ctk.CTkSwitch(window, text="", command=switch_event,variable=switch_var, onvalue="on", offvalue="off",fg_color=('#06142E','#D7F0E9'), progress_color=('black', '#F1F1F1'))

#button press function
def buttonpress(value):
    global expression
    expression = expression + str(value)
    equation.set(expression)
    
#equals is pressed
def solve():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""
        
#clear        
def AC():
    global expression
    expression = ""
    equation.set("")
    
#positive negative button 
def neg():
    try:
        global expression
        expression = str(int(expression)*-1)
        equation.set(expression)
    except:
        equation.set(" error ")
        expression = ""
      
#percent button
def percent():
    try:
        global expression
        expression = str(int(expression)/100)
        equation.set(expression)
    except:
        equation.set(" error ")
        expression = ""
        
#displayed equation string
equation = ctk.StringVar()

# widgets 

#Darkmode 
#fg window color = #06142E
#fg button  color = #1B3358 main buttons
#fg button color = #473E66
#text color = #D7F0E9

#lightmode
#fg window color = #D7F0E9
#fg button  color =  #6FABD0 main buttons hover : #92C0D7
#fg button color = #477977 hover: #B0D5C7
#text color = #06142E

#row 0
label1 = ctk.CTkLabel(window, text = '0', justify='right', textvariable= equation, fg_color = ('#D7F0E9','#06142E'), text_color=('#06142E','#D7F0E9'), anchor = 'e', padx = 30, font = ('Work Sans', 40))

#row 1
button1 = ctk.CTkButton(window, text = 'AC', command= AC,  font = ('Work Sans', 25), fg_color = ('#477977','#473E66'), text_color=('#06142E','#D7F0E9'), hover_color= ('#B0D5C7', '#8765AD'), corner_radius= 0)
button2 = ctk.CTkButton(window, text = '+/-', command = neg, font = ('Work Sans', 25), fg_color = ('#477977','#473E66'), text_color=('#06142E','#D7F0E9'), hover_color= ('#B0D5C7', '#8765AD'), corner_radius= 0)
button3 = ctk.CTkButton(window, text = '%', command= percent, font = ('Work Sans', 25), fg_color = ('#477977','#473E66'), text_color=('#06142E','#D7F0E9'), hover_color= ('#B0D5C7', '#8765AD'), corner_radius= 0)
button4 = ctk.CTkButton(window, text = '/', command=lambda: buttonpress('/'), font = ('Work Sans', 25), fg_color = ('#477977','#473E66'), text_color=('#06142E','#D7F0E9'), hover_color= ('#B0D5C7', '#8765AD'), corner_radius= 0)

#row 2
button5 = ctk.CTkButton(window, text = '7', command=lambda: buttonpress(7), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button6 = ctk.CTkButton(window, text = '8', command=lambda: buttonpress(8), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button7 = ctk.CTkButton(window, text = '9', command=lambda: buttonpress(9), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button8 = ctk.CTkButton(window, text = 'X', command=lambda: buttonpress('*'), font = ('Work Sans', 25), fg_color = ('#477977','#473E66'), text_color=('#06142E','#D7F0E9'), hover_color= ('#B0D5C7', '#8765AD'), corner_radius= 0)

#row 3
button9 = ctk.CTkButton(window, text = '4', command=lambda: buttonpress(4), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button10 = ctk.CTkButton(window, text = '5', command=lambda: buttonpress(5), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button11 = ctk.CTkButton(window, text = '6', command=lambda: buttonpress(6), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button12 = ctk.CTkButton(window, text = '-', command=lambda: buttonpress('-'), font = ('Work Sans', 25), fg_color = ('#477977','#473E66'), text_color=('#06142E','#D7F0E9'), hover_color= ('#B0D5C7', '#8765AD'), corner_radius= 0)

#row 4
button13 = ctk.CTkButton(window, text = '1', command=lambda: buttonpress(1), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button14 = ctk.CTkButton(window, text = '2', command=lambda: buttonpress(2), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button15 = ctk.CTkButton(window, text = '3', command=lambda: buttonpress(3), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button16 = ctk.CTkButton(window, text = '+', command=lambda: buttonpress('+'), font = ('Work Sans', 25), fg_color = ('#477977','#473E66'), text_color=('#06142E','#D7F0E9'), hover_color= ('#B0D5C7', '#8765AD'), corner_radius= 0)

#row 5
button17 = ctk.CTkButton(window, text = '0', command=lambda: buttonpress(0), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button18 = ctk.CTkButton(window, text = '.', command=lambda: buttonpress('.'), font = ('Work Sans', 25), fg_color = ('#6FABD0','#1B3358'), text_color=('#06142E','#D7F0E9'), hover_color= ('#92C0D7','#4C51A5'), corner_radius= 0)
button19 = ctk.CTkButton(window, text = '=', command= solve, font = ('Work Sans', 25), fg_color = ('#477977','#473E66'), text_color=('#06142E','#D7F0E9'), hover_color= ('#B0D5C7', '#8765AD'), corner_radius= 0)

#number keypress
window.bind('<KeyPress-1>', lambda event:buttonpress(1))
window.bind('<KeyPress-2>', lambda event:buttonpress(2))
window.bind('<KeyPress-3>', lambda event:buttonpress(3))
window.bind('<KeyPress-4>', lambda event:buttonpress(4))
window.bind('<KeyPress-5>', lambda event:buttonpress(5))
window.bind('<KeyPress-6>', lambda event:buttonpress(6))
window.bind('<KeyPress-7>', lambda event:buttonpress(7))
window.bind('<KeyPress-8>', lambda event:buttonpress(8))
window.bind('<KeyPress-9>', lambda event:buttonpress(9))
window.bind('<KeyPress-0>', lambda event:buttonpress(0))

# define a grid
window.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
window.rowconfigure(0, weight = 4, uniform = 'a')
window.rowconfigure((1,2,3,4), weight = 1, uniform = 'a')

# place widgets in grid
label1.grid(row = 0, column = 1,columnspan=4, sticky = 'nsew', )
switch.grid(row = 0, column = 0, sticky = 'nw')

#row 1
button1.grid(row = 1, column= 0, sticky= 'nsew', padx = 2, pady= 2)
button2.grid(row = 1, column= 1, sticky= 'nsew', padx = 2, pady= 2)
button3.grid(row = 1, column= 2, sticky= 'nsew', padx = 2, pady= 2)
button4.grid(row = 1, column= 3, sticky= 'nsew', padx = 2, pady= 2)

#row 2
button5.grid(row = 2, column= 0, sticky= 'nsew', padx = 2, pady= 2)
button6.grid(row = 2, column= 1, sticky= 'nsew', padx = 2, pady= 2)
button7.grid(row = 2, column= 2, sticky= 'nsew', padx = 2, pady= 2)
button8.grid(row = 2, column= 3, sticky= 'nsew', padx = 2, pady= 2)

#row 3 
button9.grid(row = 3, column= 0, sticky= 'nsew', padx = 2, pady= 2)
button10.grid(row = 3, column= 1, sticky= 'nsew', padx = 2, pady= 2)
button11.grid(row = 3, column= 2, sticky= 'nsew', padx = 2, pady= 2)
button12.grid(row = 3, column= 3, sticky= 'nsew', padx = 2, pady= 2)

#row 4
button13.grid(row = 4, column= 0, sticky= 'nsew', padx = 2, pady= 2)
button14.grid(row = 4, column= 1, sticky= 'nsew', padx = 2, pady= 2)
button15.grid(row = 4, column= 2, sticky= 'nsew', padx = 2, pady= 2)
button16.grid(row = 4, column= 3, sticky= 'nsew', padx = 2, pady= 2)

#row 5
button17.grid(row = 5, column= 0,columnspan=2,sticky='nsew', padx = 2, pady= 2)
button18.grid(row = 5, column= 2, sticky= 'nsew', padx = 2, pady= 2)
button19.grid(row = 5, column= 3, sticky= 'nsew', padx = 2, pady= 2)


#run
window.mainloop()

