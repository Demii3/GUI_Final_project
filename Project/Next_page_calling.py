import Next_Page_class
import GUI_Class_file
import sqlite3

proj = Next_Page_class.Our_project()
proj2 = GUI_Class_file.MyGui2()
root = proj.root_lvl1_(800, 600)
root.geometry("670x900+1200+50")
x = 0
num = 0

# ______________________________FUNCTIONS____________________________________
def station_selected_and_fare(event):
    global num
    x = 0
    for i in options:
        x+=1
        if i == station_option.get():
            num = abs(x-5) * 13
            to_station.configure(text=f"To: {station_option.get()}")
    fare.configure(state= 'normal')
    fare.delete(0, 'end')
    fare.insert(0, "$ %.2f" % num)
    fare.configure(state= 'readonly')
    total_amount_indicator.configure(text=f"$ {num * int(no_of_tix.get())}")

def update_amount():
    total_amount_indicator.configure(text= f"$ {num * int(no_of_tix.get())}")

def update_change(event):
    print(currency_entry.get())
    change_indicator.configure(text= "$ %.2f" % (float(currency_entry.get()) - float(num * int(no_of_tix.get()))))
    if float(currency_entry.get()) - float(num * int(no_of_tix.get())) < 0:
        message_status.configure(text= "* Insufficient balance", fg= 'red')
    else:
        message_status.configure(text= "* The required balance is met", fg= 'green')
    print(event)

def clear():
    x = 0
    station_option.current(4)
    fare.configure(state= 'normal')
    fare.delete(0, 'end')
    fare.insert(0, "%.2f" % 0.00)
    fare.configure(state= 'readonly')
    no_of_tix.delete(0, 'end')
    no_of_tix.insert(0, 1)
    total_amount_indicator.configure(text= "$ 0")
    currency_entry.delete(0, 'end')
    change_indicator.configure(text= "$ %.2f" % 0.00)
    message_status.configure(text= '*')
    station_selected_and_fare(1)
    for i in entries_in_create_account:
        entries_in_create_account[x].delete(0, 'end')
        x += 1
        if x == len(entries_in_create_account):
            x = 0
    station_option_2.current(4)
    fare_2.configure(state='normal')
    fare_2.delete(0, 'end')
    fare_2.insert(0, "%.2f" % 0.00)
    fare_2.configure(state='readonly')
    no_of_tix_2.delete(0, 'end')
    no_of_tix_2.insert(0, 1)
    total_amount_indicator_2.configure(text="$ 0")
    currency_entry_2.delete(0, 'end')
    change_indicator_2.configure(text="$ %.2f" % 0.00)
    message_status_2.configure(text='*')
    station_selected_and_fare_2(1)
    message_info_3.configure(text= '*', fg= 'black')

def confirm():
    if currency_entry.get() == '' or float(currency_entry.get()) - float(num * int(no_of_tix.get())) < 0:
        message_status.configure(text="* Insufficient balance, cannot proceed", fg='red')
    else:
        proj2.create_messagebox("Update", "Ticket Purchased Successfully")
        message_status.configure(text="*")
        clear()
        proj.other_page(home_page_frame)


def save_new_user():
    if entries_in_create_account[3].get() == entries_in_create_account[5].get() == '':
        proj2.create_messagebox("Error", "Crucial Fields are unfilled")
    elif entries_in_create_account[5].get() != entries_in_create_account[6].get():
        proj2.create_messagebox("Error", "Password Mismatch")
    else:
        fields = ["First_name, Middle_name, Last_name, Username_, Email, Password"]
        values = ("'"+entries_in_create_account[0].get()+"','"+entries_in_create_account[1].get()+"','"+entries_in_create_account[2].get()+"',"
                  "'"+entries_in_create_account[3].get()+"','"+entries_in_create_account[4].get()+"','"+entries_in_create_account[5].get()+"'")
        proj2.save_data_into_database("OOP_Final_projectDB", "Use_Information", fields[0], values)
        proj.other_page(home_page_frame)
        clear()

def login():
    command = (f"SELECT Password "
               f"FROM Use_Information "
               f"WHERE Username_ == '{str(username.get())}'")
    ok = proj2.cursor_database("OOP_Final_projectDB", command)
    if password.get() == ok[0]:
        proj.other_page(user_frame)
        print(ok[0])
    else:
        proj2.create_messagebox("Error", "Password and Username Mismatch")

def forgot_password(event):
    proj.other_page(forgot_password_frame)

def station_selected_and_fare_2(event):
    global num_2
    x = 0
    for i in options:
        x+=1
        if i == station_option_2.get():
            num_2 = abs(x-5) * 13
            to_station_2.configure(text=f"To: {station_option_2.get()}")
    fare_2.configure(state= 'normal')
    fare_2.delete(0, 'end')
    fare_2.insert(0, "$ %.2f" % num_2)
    fare_2.configure(state= 'readonly')
    total_amount_indicator_2.configure(text=f"$ {num_2 * int(no_of_tix_2.get())}")

def update_amount_2():
    total_amount_indicator_2.configure(text= f"$ {num_2 * int(no_of_tix_2.get())}")

def update_change_2(event):
    print(currency_entry_2.get())
    change_indicator_2.configure(text= "$ %.2f" % (float(currency_entry_2.get()) - float(num * int(no_of_tix_2.get()))))
    if float(currency_entry_2.get()) - float(num_2 * int(no_of_tix_2.get())) < 0:
        message_status_2.configure(text= "* Insufficient balance", fg= 'red')
    else:
        message_status_2.configure(text= "* The required balance is met", fg= 'green')
        print(event)

def check_password_validity(event):
    if entries_in_create_account[5].get() != entries_in_create_account[6].get():
        message_info_3.configure(text= "Password Mismatch", font= ('Times New Roman', 10, 'italic'), fg= 'red')
    else:
        message_info_3.configure(text="Password Match", font=('Times New Roman', 10, 'italic'), fg='green')
# ______________________________FUNCTIONS____________________________________


# ____________________________________________________FRAMES___________________________________________________________
# _______________LVL 1:_____________________
main_frame = proj2.create_labelframe(root, '', None, 0, 0, 20, 0, 20, 0, 'w')
# _______________LVL 1:_____________________

# _______________LVL 2: frames contained in main_frame_____________________
home_page_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')

buy_ticket_onetime_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')

buy_ticket_as_user_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')

create_account_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')

forgot_password_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')

user_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')
# _______________LVL 2: frames contained in main_frame_____________________

# _______________________________________LVL 3:_______________________________________________________
# ______________LVL 3: frames contained in home_page_frame ________________
frame_holder = proj2.create_frame(home_page_frame, None, 0, 0,
                                  100, 0, 15, 15, 'news')
frame_holder.pack()
# ______________LVL 3: frames contained in home_page_frame ________________

# _______________LVL 3: frames contained in buy_ticket_onetime_frame_____________________
one_time_ticket_purchase = proj2.create_labelframe(buy_ticket_onetime_frame, ' One-time Ticket Purchase', None,
                                                0, 0, 30, 30, 30, 30, 'w')
one_time_ticket_purchase.pack()
one_time_ticket_purchase.configure(font= ('Times New Roman', 25, 'bold'))
# _______________LVL 3: frames contained in buy_ticket_onetime_frame_____________________

# _______________LVL 3: frames contained in create_account_frame_____________________
create_account_label_frame = proj2.create_labelframe(create_account_frame, ' Create an Account', None,
                                                0, 0, 30, 30, 30, 30, 'n')
create_account_label_frame.pack(padx= (30, 30), pady= (30, 30))
create_account_label_frame.configure(font= ('Times New Roman', 25, 'bold'))
# _______________LVL 3: frames contained in create_account_frame_____________________

# _______________LVL 3: frames contained in buy_ticket_as_user_frame_____________________
buy_as_user_labelframe = proj2.create_labelframe(buy_ticket_as_user_frame, 'Log-in', None, 0, 0, 0, 0, 0, 0, 'w')
buy_as_user_labelframe.pack()
buy_as_user_labelframe.configure(font= ('Times New Roman', 25, 'bold'))

# _______________LVL 3: frames contained in buy_ticket_as_user_frame_____________________

# _______________LVL 3: frames contained in user_frame_____________________
welcome_labelframe = proj2.create_labelframe(user_frame, 'Welcome', None, 0, 0, 0, 0, 0, 0, 'n')
welcome_labelframe.pack()
welcome_labelframe.configure(font= ('Times New Roman', 25, 'bold'))
# _______________LVL 3: frames contained in user_frame_____________________
# _______________________________________LVL 3:_______________________________________________________


# _______________________________________LVL 4:_______________________________________________________
# _______________LVL 4: Homepage frames_____________________
purchase_ticket_frame = proj2.create_labelframe(frame_holder, 'Purchase Ticket', None,
                                                1, 0, 0, 0, 10, 10, 'n')
purchase_ticket_frame.configure(font= ('Times New Roman', 20, 'italic bold'))
create_user_frame = proj2.create_labelframe(frame_holder, 'Create Account', None,
                                                2, 0, 0, 0, 10, 10, 'n')
create_user_frame.configure(font= ('Times New Roman', 20, 'italic bold'))
# _______________LVL 4: Homepage frames_____________________

# _______________LVL 4: Buy ticket onetime frames_____________________
mini_frames = []
for i in range(9):
    frame = proj2.create_frame(one_time_ticket_purchase, None,
                               x, 0, 15, 15, 10, 10, 'n')
    x += 1
    mini_frames.append(frame)
    if len(mini_frames) == 9:
        x = 0
        # _______________LVL 5: Buy ticket onetime frames_____________________
        frame = proj2.create_frame(mini_frames[2], None,
                                   1, 0, 0, 0, 0, 0, 'w')
        # _______________LVL 5: Buy ticket onetime frames_____________________
        mini_frames.append(frame)
# _______________LVL 4: Buy ticket onetime frames_____________________

# _______________LVL 4: Create Account frames_____________________
frame_holder_2 = proj.frame_lvl_(create_account_label_frame, None, 0, 0, 'n')
frame_holder_2.pack()
mini_frames_2 = []
for i in range(7):
    frame1 = proj2.create_frame(frame_holder_2, None, x, 0, 10, 0, 10, 0, 'w')
    mini_frames_2.append(frame1)
    x += 1
    if len(mini_frames_2) == 7:
        mini_frames_2[2].configure()
        x = 0
# _______________LVL 4: Create Account frames_____________________

# _______________LVL 4: Buy ticket as user frames_____________________
frame_holder_3 = proj.frame_lvl_(buy_as_user_labelframe, None, 0, 0, 'n')
frame_holder_3.pack(padx= (10, 20), pady= (20, 20))

mini_frames_3 = []
for i in range(7):
    frame2 = proj2.create_frame(frame_holder_3, None, x, 0, 0, 0, 15, 0, 'n')
    mini_frames_3.append(frame2)
    x += 1
    if len(mini_frames_3) == 7:
        x = 0
# _______________LVL 4: Buy ticket as user frames_____________________

# _______________LVL 4: User frame frames_____________________
frame_holder_4 = proj.frame_lvl_(welcome_labelframe, None, 0, 0, 'n')
frame_holder_4.pack(padx= 80, pady= (0, 20))

mini_frames_4 = []
for i in range(10):
    frame3 = proj2.create_frame(frame_holder_4, None, x, 0, 10, 10, 10, 0, 'n')
    mini_frames_4.append(frame3)
    x += 1
    if len(mini_frames_4) == 10:
        frame3 = proj2.create_frame(mini_frames_4[3], None, 1, 0, 0, 0, 15, 0, 'n')
        mini_frames_4.append(frame3)
        x = 0
# _______________LVL 4: User frame frames_____________________
# _______________________________________LVL 4:_______________________________________________________


# ____________________________________________________FRAMES___________________________________________________________



# ____________________________________________________CONTENTS__________________________________________________________

# ___________________________________LVL 2:_________________________________________________
# _______________________LVL 2: Homepage content________________________________
main_label = proj2.create_label(frame_holder, 'Ticket Trove Machine',
                                0, 0, 1, 0, 0, 0, 10, 'n')
main_label.configure(font= ('Cambria', 30, 'bold'))
purchase_button1 = proj.button(purchase_ticket_frame, 'Purchase Ticket (One Time)', 25, 1,
                               0, 0, 15, 15, 20, 0)
purchase_button1.configure(font= ('Times New Roman', 15, 'bold'), command= lambda :proj.other_page(buy_ticket_onetime_frame))
purchase_button2 = proj.button(purchase_ticket_frame, 'Purchase Ticket (As a user)', 25, 1,
                               1, 0, 10, 10, 20, 20)
purchase_button2.configure(font= ('Times New Roman', 15, 'bold'), command= lambda : proj.other_page(buy_ticket_as_user_frame))
create_account_button = proj.button(create_user_frame, 'Create an Account', 25, 1,
                                1, 0, 10, 10, 20, 20)
create_account_button.configure(font= ('Times New Roman', 15, 'bold'), command= lambda :(proj.other_page(create_account_frame)))
# _______________________LVL 2: Homepage content________________________________


# ___________________LVL 2: Buy ticket one time content_________________________
options = ["Station -4","Station -3","Station -2","Station -1","Station 0","Station 1","Station 2", "Station 3",
           "Station 4"]
current_station_label = proj2.create_label(mini_frames[0], "You're in: Station 0",
                                           0, 0, 1, 0, 0, 0, 0,'w')
current_station_label.configure(font= ('Times New Roman', 15))
station_option = proj2.create_combobox_with_label(mini_frames[1], 'Your Destination: ', 'Times New Roman',
                                                  15, '', options, None, 15,0, 0, 1, 0,
                                                  10, 10, 0, 0, 'n')
station_option.configure(font=('Times New Roman', 15))
station_option.current(4)
station_option.bind("<<ComboboxSelected>>", station_selected_and_fare)

journey = proj2.create_label(mini_frames[2], "Journey: ",
                                           0, 0, 1, 0, 0, 0, 0,'news')
journey.configure(font= ('Times New Roman', 15))
from_station = proj2.create_label(mini_frames[9], "From: Station 0",
                                           0, 0, 1, 0, 0, 0, 0,'news')
from_station.configure(font= ('Times New Roman', 12))
to_station = proj2.create_label(mini_frames[9], "To: Station 0",
                                           1, 0, 1, 0, 0, 0, 0,'news')
to_station.configure(font= ('Times New Roman', 12))

fare = proj2.create_entry_with_label(mini_frames[3], 'Fare: ', 'Times New Roman', 15, '', None, 10,
                                           0, 0, 1, 0, 20, 20, 0, 0, 'n')
fare.insert(0, "$ 0")
fare.configure(font= ('Times New Roman', 15), state= 'readonly')

no_of_tix = proj2.create_spinbox_with_label(mini_frames[4], 'Number of Tickets: ', 'Times New Roman', 15, '', None, 1, 10, 10,
                                           0, 0, 1, 0, 0, 0, 0, 0, 'n')
no_of_tix.configure(font=('Times New Roman', 15), command= update_amount)
total_amount_label = proj2.create_label(mini_frames[5], "Total Amount: ",
                                           0, 0, 1, 0, 0, 0, 0,'w')
total_amount_label.configure(font=('Times New Roman', 15))
total_amount_indicator = proj2.create_label(mini_frames[5], "$ 0",
                                           0, 1, 1, 0, 0, 0, 0,'w')
total_amount_indicator.configure(font=('Times New Roman', 15))
currency_entry = proj2.create_entry_with_label(mini_frames[6], "Enter Currency Amount: ", 'Times New Roman', 15, '', None, 10,
                                           0, 0, 1, 0, 0, 0, 0, 0, 'n')
currency_entry.configure(font=('Times New Roman', 15))
currency_entry.bind('<KeyRelease>', update_change)
change_label = proj2.create_label(mini_frames[7], "Change: ",
                                           0, 0, 1, 0, 0, 0, 0,'w')
change_label.configure(font=('Times New Roman', 15))
change_indicator = proj2.create_label(mini_frames[7], "$ 0",
                                           0, 1, 1, 0, 0, 0, 0,'w')
message_status = proj2.create_label(mini_frames[7], '*', 1, 0, 2, 0, 0, 0, 0, 'w')
change_indicator.configure(font=('Times New Roman', 15))

return_button_1 = proj.button(mini_frames[8], 'Return', 15, 1,
                            0, 0, 0, 0, 0, 0)
return_button_1.configure(command= lambda :(clear(), proj.other_page(home_page_frame)))
clear_button = proj.button(mini_frames[8], 'Clear', 15, 1,
                            0, 1, 10, 10, 0, 0)
clear_button.configure(command= clear)
confirm_button = proj.button(mini_frames[8], 'Confirm', 15, 1,
                            0, 2, 0, 0, 0, 0)
confirm_button.configure(command=confirm)
# ___________________LVL 2: Buy ticket one time content_________________________

# ___________________LVL 2: Create Account content_________________________
message_info_1 = proj2.create_label(mini_frames_2[0], '* Inserting an image is optional',
                                    0, 1, 1, 0, 0, 0, 0, 'n')
message_info_1_ = proj2.create_label(mini_frames_2[0], ' * Fields containing * are needed',
                                    0, 1, 1, 0, 0, 25, 0, 'n')
message_info_1.configure(font= ('Times New Roman', 10, 'italic'))
message_info_1_.configure(font= ('Times New Roman', 10, 'italic'))
label_names_1 = ['First Name', 'Middle Name', 'Last Name']
label_names_2 = ['Password*', 'Confirm Password*']
entries_in_create_account = []
for i in label_names_1:
    entry = proj2.create_entry_with_label(mini_frames_2[1], i, 'Times New Roman', 13, '', None, 18,
                                        0, x, 1, x, 0, 10, 0, 0, 'w')
    entries_in_create_account.append(entry)
    x += 1
    if x == len(label_names_1):
        x = 0

username_acc = proj2.create_entry_with_label(mini_frames_2[2], 'Username*', 'Times New Roman', 13, '', None,
                                      23, 0, 0, 1, 0, 0, 10, 0, 0, 'w')
entries_in_create_account.append(username_acc)

email = proj2.create_entry_with_label(mini_frames_2[2], 'Email', 'Times New Roman', 13, '', None,
                                      30, 0, 1, 1, 1, 0, 0, 0, 0, 'w')
entries_in_create_account.append(email)

message_info_2 = proj2.create_label(mini_frames_2[2], '* Incase of Access loss',
                                    3, 1, 1, 0, 0, 0, 0,'w')
message_info_2.configure(font= ('Times New Roman', 10, 'italic'))


for i in label_names_2:
    entry2 = proj2.create_entry_with_label(mini_frames_2[3], i, 'Times New Roman', 13, '', None, 18,
                                        0, x, 1, x, 0, 10, 0, 0, 'w')
    entries_in_create_account.append(entry2)
    x += 1
    if x == len(label_names_2):
        x = 0
        for index in [5, 6]:
            entries_in_create_account[index].configure(show= '*')
            entries_in_create_account[6].bind('<KeyRelease>', check_password_validity)
message_info_3 = proj2.create_label(mini_frames_2[3], '*', 0, 2, 1, 0, 0, 0, 0, 'w')


return_button_2 = proj.button(mini_frames_2[4], 'Return', 15, 1,
                            0, 0, 0, 10, 0, 0)
return_button_2.configure(command= lambda :(clear() ,proj.other_page(home_page_frame)))
clear_button_2 = proj.button(mini_frames_2[4], 'Clear', 15, 1,
                             0, 1, 0, 0, 0, 0, )
clear_button_2.configure(command= clear)
save_button = proj.button(mini_frames_2[4], 'Create Account', 15, 1,
                          0, 3, 10, 0, 0, 0, )
save_button.configure(command= save_new_user)

# ___________________LVL 2: Create Account content_________________________


# ___________________LVL 2: Buy ticket as user content_________________________
username = proj2.create_entry_with_label(mini_frames_3[1], 'Username: ', 'Times New Roman', 15, '',
                                         None, 20, 0, 0, 0, 1, 0, 0, 0, 0, 'w')
password = proj2.create_entry_with_label(mini_frames_3[2], 'Password: ', 'Times New Roman', 15, '',
                                         None, 20, 1, 0, 1, 1, 0, 0, 0, 0, 'w')
password.configure(show= '*')
log_in = proj.button(mini_frames_3[3], 'Log in', 15, 1, 0, 0, 0, 0 ,0, 0)
log_in.configure(command= login)
forgor_password = proj2.create_label(mini_frames_3[4], 'Forgot Password?',
                                     0, 0, 1, 0, 0, 0, 0, 'w')
forgor_password.configure(cursor= 'hand2')
forgor_password.bind('<Button-1>', forgot_password)

return_button_3 = proj.button(mini_frames_3[6], 'Return', 15, 1,
                              0, 0, 0, 0, 0, 0)
return_button_3.configure(command= lambda :(clear(), proj.other_page(home_page_frame)))
# ___________________LVL 2: Buy ticket as user content_________________________

# ___________________LVL 2: User frame content_________________________
label_info_frame = proj.frame_lvl_(mini_frames_4[0], None, 0, 1, 'n')
greetings = proj2.create_label(label_info_frame, 'Hello, User!',
                               0, 0, 1, 0, 0, 0, 0,'nw')
greetings.configure(font= ('Times New Roman', 10, 'italic'))
total_points = proj2.create_label(label_info_frame, 'Your Total points is: ',
                                  1 , 0, 1, 0, 0, 0, 0,'nw')
total_points.configure(font= ('Times New Roman', 10, 'italic'))

current_station_label_2 = proj2.create_label(mini_frames_4[1], "You're in: Station 0",
                                           0, 0, 1, 0, 0, 0, 0,'w')
current_station_label_2.configure(font= ('Times New Roman', 15))
station_option_2 = proj2.create_combobox_with_label(mini_frames_4[2], 'Your Destination: ', 'Times New Roman',
                                                  15, '', options, None, 15,0, 0, 1, 0,
                                                  10, 10, 0, 0, 'n')
station_option_2.configure(font=('Times New Roman', 15))
station_option_2.current(4)
station_option_2.bind("<<ComboboxSelected>>", station_selected_and_fare_2)

journey_2 = proj2.create_label(mini_frames_4[3], "Journey: ",
                                           0, 0, 1, 0, 0, 0, 0,'news')
journey_2.configure(font= ('Times New Roman', 15))
from_station_2 = proj2.create_label(mini_frames_4[10], "From: Station 0",
                                           0, 0, 1, 0, 0, 0, 0,'news')
from_station_2.configure(font= ('Times New Roman', 12))
to_station_2 = proj2.create_label(mini_frames_4[10], "To: Station 0",
                                           1, 0, 1, 0, 0, 0, 0,'news')
to_station_2.configure(font= ('Times New Roman', 12))
fare_2 = proj2.create_entry_with_label(mini_frames_4[4], 'Fare: ', 'Times New Roman', 15, '', None, 10,
                                           0, 0, 1, 0, 20, 20, 0, 0, 'n')
fare_2.insert(0, "$ 0")
fare_2.configure(font= ('Times New Roman', 15), state= 'readonly')

no_of_tix_2 = proj2.create_spinbox_with_label(mini_frames_4[4], 'Number of Tickets: ', 'Times New Roman', 15, '', None, 1, 10, 10,
                                           0, 0, 1, 0, 0, 0, 0, 0, 'n')
no_of_tix_2.configure(font=('Times New Roman', 15), command= update_amount_2)
total_amount_label_2 = proj2.create_label(mini_frames_4[5], "Total Amount: ",
                                           0, 0, 1, 0, 0, 0, 0,'w')
total_amount_label_2.configure(font=('Times New Roman', 15))
total_amount_indicator_2 = proj2.create_label(mini_frames_4[5], "$ 0",
                                           0, 1, 1, 0, 0, 0, 0,'w')
total_amount_indicator_2.configure(font=('Times New Roman', 15))
currency_entry_2 = proj2.create_entry_with_label(mini_frames_4[6], "Enter Currency Amount: ", 'Times New Roman', 15, '', None, 10,
                                           0, 0, 1, 0, 0, 0, 0, 0, 'n')
currency_entry_2.configure(font=('Times New Roman', 15))
currency_entry_2.bind('<KeyRelease>', update_change_2)
change_label_2 = proj2.create_label(mini_frames_4[7], "Change: ",
                                           0, 0, 1, 0, 0, 0, 0,'w')
change_label_2.configure(font=('Times New Roman', 15))
change_indicator_2 = proj2.create_label(mini_frames_4[7], "$ 0",
                                           0, 1, 1, 0, 0, 0, 0,'w')
message_status_2 = proj2.create_label(mini_frames_4[7], '*', 1, 0, 2, 0, 0, 0, 0, 'w')
change_indicator_2.configure(font=('Times New Roman', 15))


return_button_4 = proj.button(mini_frames_4[9], 'Return', 15, 1, 0, 0, 0, 0, 0, 0)
return_button_4.configure(command= lambda :(clear(), proj.other_page(home_page_frame)))
# ___________________LVL 2: User frame content_________________________

# ___________________LVL 2: Forgot password content_________________________
email_ = proj2.create_entry_with_label(forgot_password_frame, 'Email: ', 'Times New Roman', 15, '', None,
                                       25, 0, 0, 0, 1, 0, 0, 0, 0, 'w')
return_button_5 = proj.button(forgot_password_frame, 'Return', 15, 1, 0, 0, 0, 0, 0, 0)
return_button_5.configure(command= lambda :(proj.other_page(home_page_frame)))
# ___________________LVL 2: Forgot password content_________________________


# ___________________________________LVL 2:_________________________________________________

# ____________________________________________________CONTENTS__________________________________________________________
home_page_frame.tkraise()
root.mainloop()