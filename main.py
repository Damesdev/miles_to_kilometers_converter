from tkinter import *

###Creating Window
window = Tk()
# window.minsize(width= 500, height= 500)
window.title("Distance Converter")

#Entry
distance_input = Entry(width= 10)
distance_input.grid(row=1, column=2)

###Making Radio Buttons

#Radio button function (did not use function instead included in calculate function line.42)
# def button_used():
#     choice = (button_state.get())
#     if choice == 1:
#         unit_label['text'] = "Km's"
#     elif choice == 2:
#         unit_label['text'] = 'Miles'

#returns value as integer variable
button_state = IntVar()

to_km_button = Radiobutton(text= "Miles", value=1, variable=button_state)
to_miles_button = Radiobutton(text= "Kilometers", value=2, variable=button_state)

to_km_button.grid(row= 1, column= 4)
to_miles_button.grid(row =1, column = 3)

###Labels
#Unit label either Km or Miles(dynamic)
unit_label = Label(text="distance unit")
unit_label.grid(row=3,column=3)

#Integer of converted amount(dynamic)
distance_amount_label = Label(text=" 0 ")
distance_amount_label.grid(row=3,column=2)

#Doesnt change unless wanted to say other phrase (static)
transition_label= Label(text="is equal to")
transition_label.grid(row=3, column= 1)

###Button
#Button Function converts unit from selected unit to correct end unit. Updates unit label at same time.
def calculate_unit():
    choice = (button_state.get())
    raw_distance = int(distance_input.get())
    if choice == 1:
        unit_label['text'] = "Km's"
        converted_amount = raw_distance * 1.60934
        distance_amount_label['text'] = ("{:.2f}".format(converted_amount))
    elif choice == 2:
        unit_label['text'] = 'Miles'
        converted_amount = raw_distance / 1.60934
        distance_amount_label['text'] = ("{:.2f}".format(converted_amount))


###Create Button
calculate_button = Button(text="calculate", command=calculate_unit)
calculate_button.grid(column= 2 ,row=4)

window.mainloop()