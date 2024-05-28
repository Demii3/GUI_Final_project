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
    entries_in_create_account[6].configure(state= 'readonly')
    username.delete(0, 'end')
    password.delete(0, 'end')
    username_forgor.delete(0, 'end')
    email_.delete(0, 'end')
    new_password.delete(0, 'end')
    confirm_new_password.delete(0, 'end')
    new_password.configure(state='readonly')
    confirm_new_password.configure(state='readonly')
    message_info_4.configure(text= '*', fg= 'black')

def confirm():
    if currency_entry.get() == '' or float(currency_entry.get()) - float(num * int(no_of_tix.get())) < 0:
        message_status.configure(text="* Insufficient balance, cannot proceed", fg='red')
    else:
        proj2.create_messagebox("Update", "Ticket Purchased Successfully")
        message_status.configure(text="*")
        clear()
        proj.other_page(home_page_frame)


def save_new_user():
    if entries_in_create_account[3].get() and entries_in_create_account[5].get() != '':
        if entries_in_create_account[5].get() != entries_in_create_account[6].get():
            proj2.create_messagebox("Error", "Password Mismatch")
        else:
            try:
                command = (f"SELECT Username_ "
                           f"FROM Use_Information "
                           f"WHERE Username_ == '{str(entries_in_create_account[3].get())}'")
                ok = proj2.cursor_database("OOP_Final_projectDB", command)
                if entries_in_create_account[3].get() == ok[0]:
                    proj2.create_messagebox("Error", "Username Already exists")

            except TypeError:
                fields = ["First_name, Middle_name, Last_name, Username_, Email, Password"]
                values = ("'" + entries_in_create_account[0].get() + "','" + entries_in_create_account[1].get() + "',"
                          "'" +entries_in_create_account[2].get() + "','" + entries_in_create_account[3].get() + "',"
                          "'" +entries_in_create_account[4].get() + "','" + entries_in_create_account[5].get() + "'")
                proj2.save_data_into_database("OOP_Final_projectDB", "Use_Information", fields[0], values)
                proj2.create_messagebox("Success", "Account Created Successfully")
                proj.other_page(home_page_frame)
                clear()
    else:
        proj2.create_messagebox("Error", "Crucial Fields are unfilled")

def login():
    if username.get() != '':
        try:
            command = (f"SELECT Password, Username_, User_total_points "
                       f"FROM Use_Information "
                       f"WHERE Username_ == '{str(username.get())}'")
            ok = proj2.cursor_database("OOP_Final_projectDB", command)
            greetings.configure(text= f'Hello user, {ok[1]}')
            total_points.configure(text= f'Your total points is: {ok[2]}')
            if password.get() == ok[0]:
                proj.other_page(user_frame)
                print(ok[2])
            else:
                proj2.create_messagebox("Error", "Password and Username Mismatch")
        except TypeError:
            proj2.create_messagebox("Error", "Username does not exist")
    else:
        proj2.create_messagebox("Error", "Username unfilled")

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
    entries_in_create_account[6].configure(state= 'normal')
    if entries_in_create_account[6].get() != entries_in_create_account[5].get():
        message_info_3.configure(text= "Password Mismatch", font= ('helvetica', 10, 'italic'), fg= 'red')
    else:
        message_info_3.configure(text="Password Match", font=('helvetica', 10, 'italic'), fg='green')

def confirm_2():
    if currency_entry_2.get() == '' or float(currency_entry_2.get()) - float(num_2 * int(no_of_tix_2.get())) < 0:
        message_status_2.configure(text="* Insufficient balance, cannot proceed", fg='red')
    else:
        command = (f"SELECT User_total_points "
                   f"FROM Use_Information "
                   f"WHERE Username_ == '{str(username.get())}'")
        ok1 = proj2.cursor_database("OOP_Final_projectDB", command)
        command = ("""UPDATE Use_Information SET User_total_points = ? WHERE Username_ = ?""",(float(ok1[0]) + 1, str(username.get())))
        proj2.cursor_database2("OOP_Final_projectDB", command)
        proj2.create_messagebox("Update", "Ticket Purchased Successfully")
        proj2.create_messagebox("Update", f"Your Total Points is now: {float(ok1[0]) + 1}")
        message_status_2.configure(text="*")
        clear()
        proj.other_page(home_page_frame)

def search_username():
    command = ("SELECT Email "
               "FROM Use_Information "
               f"WHERE Username_ == '{str(username_forgor.get())}'")
    ok1 = proj2.cursor_database("OOP_Final_projectDB", command)
    print(ok1[0])
    if email_.get() != ok1[0]:
        proj2.create_messagebox("Error", "Username's Email does not match")
    else:
        proj2.create_messagebox("Update", "Email does match")
        new_password.configure(state= 'normal')
        confirm_new_password.configure(state= 'normal')

def check_password_validity_2(event):
    if new_password.get() != confirm_new_password.get():
        message_info_4.configure(text= "Password Mismatch", font= ('helvetica', 10, 'italic'), fg= 'red')
    else:
        message_info_4.configure(text="Password Match", font=('helvetica', 10, 'italic'), fg='green')

def confirm_3():
    if new_password.get() != confirm_new_password.get():
        message_status_2.configure(text="* Password mismatch, cannot proceed", fg='red')
    else:
        if new_password.get() == '' and confirm_new_password.get() == '':
            proj2.create_messagebox("Error", 'Password field unfilled')
            message_info_4.configure(text= 'Password unfilled', fg= 'red')
        else:
            command = ("""UPDATE Use_Information SET Password = ? WHERE Username_ = ?""",
                       ((str(new_password.get())), str(username_forgor.get())))
            proj2.cursor_database2("OOP_Final_projectDB", command)
            message_info_4.configure(text='*', fg='black')
            proj2.create_messagebox("Update", "Password Changed Successfully")
            proj.other_page(home_page_frame)


# ______________________________FUNCTIONS____________________________________


# ____________________________________________________FRAMES___________________________________________________________
# _______________LVL 1:_____________________
main_frame = proj2.create_labelframe(root, '', None, 0, 0, 20, 0, 20, 0, 'w')
# _______________LVL 1:_____________________

# _______________LVL 2: frames contained in main_frame_____________________
home_page_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')

buy_ticket_onetime_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')

create_account_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')

buy_ticket_as_user_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')

user_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')

forgot_password_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')
# _______________LVL 2: frames contained in main_frame_____________________

# _______________________________________LVL 3:_______________________________________________________
# ______________LVL 3: frames contained in home_page_frame ________________
frame_holder_1 = proj2.create_frame(home_page_frame, None, 0, 0,
                                  100, 0, 15, 15, 'news')
frame_holder_1.pack()
# ______________LVL 3: frames contained in home_page_frame ________________

# _______________LVL 3: frames contained in buy_ticket_onetime_frame_____________________
one_time_ticket_purchase = proj2.create_labelframe(buy_ticket_onetime_frame, ' One-time Ticket Purchase', None,
                                                0, 0, 30, 30, 30, 30, 'w')
one_time_ticket_purchase.pack()
one_time_ticket_purchase.configure(font= ('helvetica', 23, 'bold'))
# _______________LVL 3: frames contained in buy_ticket_onetime_frame_____________________

# _______________LVL 3: frames contained in create_account_frame_____________________
create_account_label_frame = proj2.create_labelframe(create_account_frame, ' Create an Account', None,
                                                0, 0, 300, 30, 30, 30, 'n')
create_account_label_frame.pack(padx= (30, 30), pady= (30, 30))
create_account_label_frame.configure(font= ('helvetica', 23, 'bold'))
frame_holder_2 = proj.frame_lvl_(create_account_label_frame, None, 0, 0, 'n')
frame_holder_2.pack()
# _______________LVL 3: frames contained in create_account_frame_____________________

# _______________LVL 3: frames contained in buy_ticket_as_user_frame_____________________
buy_as_user_labelframe = proj2.create_labelframe(buy_ticket_as_user_frame, 'Log-in', None, 0, 0, 0, 0, 0, 0, 'w')
buy_as_user_labelframe.pack()
buy_as_user_labelframe.configure(font= ('helvetica', 25, 'bold'))
frame_holder_3 = proj.frame_lvl_(buy_as_user_labelframe, None, 0, 0, 'n')
frame_holder_3.pack(padx= (10, 20), pady= (20, 20))
# _______________LVL 3: frames contained in buy_ticket_as_user_frame_____________________

# _______________LVL 3: frames contained in user_frame_____________________
welcome_labelframe = proj2.create_labelframe(user_frame, 'Welcome', None, 0, 0, 0, 0, 0, 0, 'n')
welcome_labelframe.pack()
welcome_labelframe.configure(font= ('helvetica', 25, 'bold'))
frame_holder_4 = proj.frame_lvl_(welcome_labelframe, None, 0, 0, 'n')
frame_holder_4.pack(padx= 80, pady= (0, 20))
# _______________LVL 3: frames contained in user_frame_____________________

# _______________ LVL 3: frames contained in forgot_password_frame _____________________
forgor_password = proj2.create_labelframe(forgot_password_frame, 'Forgor Password?', None, 0, 0, 0, 0, 0, 0, 'n')
forgor_password.configure(font= ('helvetica', 25, 'bold'))
forgor_password.pack()
frame_holder_5 = proj.frame_lvl_(forgor_password, None, 0, 0, 'n')
# _______________ LVL 3: frames contained in forgot_password_frame _____________________
# _______________________________________LVL 3:_______________________________________________________


# _______________________________________LVL 4:_______________________________________________________
# _______________LVL 4: frames contained in frame_holder_1(a frame inside home_page_frame)_____________________
purchase_ticket_frame = proj2.create_labelframe(frame_holder_1, 'Purchase Ticket', None,
                                                1, 0, 0, 0, 10, 30, 'n')
purchase_ticket_frame.configure(font= ('helvetica', 15, 'bold'))
create_user_frame = proj2.create_labelframe(frame_holder_1, 'Create Account', None,
                                                5, 0, 0, 0, 10, 10, 'n')
create_user_frame.configure(font= ('helvetica', 15, 'bold'))
# _______________LVL 4: frames contained in frame_holder_1(a frame inside home_page_frame)_____________________

# _______________LVL 4: frames contained in one_time_ticket_purchase(a frame inside buy_ticket_onetime_frame)_____________________
mini_frames = []
for i in range(9):
    frame = proj2.create_frame(one_time_ticket_purchase, None,
                               x, 0, 15, 15, 10, 10, 'n')
    x += 1
    mini_frames.append(frame)
    if len(mini_frames) == 9:
        x = 0
        # _______________LVL 5: frame contained in mini_frames[2](a frame inside one_time_ticket_purchase)_____________________
        frame = proj2.create_frame(mini_frames[2], None,
                                   1, 0, 0, 0, 0, 0, 'w')
        # _______________LVL 5: frame contained in mini_frames[2](a frame inside one_time_ticket_purchase)_____________________
        mini_frames.append(frame)
# _______________LVL 4: frames contained in one_time_ticket_purchase(a frame inside buy_ticket_onetime_frame)_____________________

# _______________LVL 4: frames contained in frame_holder_2 (a frame contained in create_account_frame) _____________________
mini_frames_2 = []
for i in range(7):
    frame1 = proj2.create_frame(frame_holder_2, None, x, 0, 10, 0, 10, 0, 'w')
    mini_frames_2.append(frame1)
    x += 1
    if len(mini_frames_2) == 7:
        mini_frames_2[2].configure()
        x = 0
# _______________LVL 4: frames contained in frame_holder_2 (a frame contained in create_account_frame) _____________________

# _______________LVL 4: frames contained in frame_holder_3 (a frame contained in buy_ticket_as_user_frame) _____________________
mini_frames_3 = []
for i in range(7):
    frame2 = proj2.create_frame(frame_holder_3, None, x, 0, 0, 0, 15, 0, 'n')
    mini_frames_3.append(frame2)
    x += 1
    if len(mini_frames_3) == 7:
        x = 0
# _______________LVL 4: frames contained in frame_holder_3 (a frame contained in buy_ticket_as_user_frame) _____________________

# _______________LVL 4: frames contained in frame_holder_4 (a frame contained in user_frame) _____________________
mini_frames_4 = []
for i in range(10):
    frame3 = proj2.create_frame(frame_holder_4, None, x, 0, 10, 10, 10, 0, 'n')
    mini_frames_4.append(frame3)
    x += 1
    if len(mini_frames_4) == 10:
        frame3 = proj2.create_frame(mini_frames_4[3], None, 1, 0, 0, 0, 15, 0, 'n')
        mini_frames_4.append(frame3)
        x = 0
# _______________LVL 4: frames contained in frame_holder_4 (a frame contained in user_frame) _____________________

# _______________LVL 4: frames contained in frame_holder_5 (a frame contained in forgot_password_frame) _____________________
mini_frames_5 = []
for i in range(10):
    frame4 = proj2.create_frame(frame_holder_5, None, x, 0, 10, 10, 15, 0, 'n')
    mini_frames_5.append(frame4)
    x += 1
    if len(mini_frames_5) == 10:
        x = 0
# _______________LVL 4: frames contained in frame_holder_5 (a frame contained in forgot_password_frame) _____________________
# _______________________________________LVL 4:_______________________________________________________
# ____________________________________________________FRAMES___________________________________________________________



# ____________________________________________________CONTENTS__________________________________________________________
# ___________________________________LVL 2:_________________________________________________

# ___________________________________LVL 2: Contents seen in home_page-frame_________________________________________________
main_label = proj2.create_label(frame_holder_1, 'Star Rail Transit',
                                0, 0, 1, 0, 0, 30, 50, 'n')
main_label.configure(font= ('helvetica', 30, 'bold'))
purchase_button1 = proj.button(purchase_ticket_frame, 'Purchase Ticket (One Time)', 25, 2,
                               0, 0, 15, 15, 20, 0, '#FF3131', 'white')
purchase_button1.configure(font= ('helvetica', 12, 'bold'), command= lambda :proj.other_page(buy_ticket_onetime_frame))
purchase_button2 = proj.button(purchase_ticket_frame, 'Purchase Ticket (As a user)', 25, 2,
                               1, 0, 10, 10, 20, 20, '#FF3131', 'white')
purchase_button2.configure(font= ('helvetica', 12, 'bold'), command= lambda : proj.other_page(buy_ticket_as_user_frame))
create_account_button = proj.button(create_user_frame, 'Create an Account', 25, 2,
                                1, 0, 10, 10, 20, 20, '#209B3D', 'white')
create_account_button.configure(font= ('helvetica', 12, 'bold'), command= lambda :(proj.other_page(create_account_frame)))
# ___________________________________LVL 2: Contents seen in home_page-frame_________________________________________________


# ___________________________________LVL 2: Contents seen in buy_ticket_onetime_frame_________________________________________________
options = ["Station -4","Station -3","Station -2","Station -1","Station 0","Station 1","Station 2", "Station 3",
           "Station 4"]
current_station_label = proj2.create_label(mini_frames[0], "You're in: Station 0",
                                           0, 0, 1, 0, 90, 10, 0,'w')
current_station_label.configure(font= ('helvetica', 18, 'bold'))
station_option = proj2.create_combobox_with_label(mini_frames[1], 'Your Destination: ', 'helvetica',
                                                  15, '', options, None, 15,0, 0, 1, 0,
                                                  10, 130, 0, 0, 'w')
station_option.configure(font=('helvetica', 15))
station_option.current(4)
station_option.bind("<<ComboboxSelected>>", station_selected_and_fare)

journey = proj2.create_label(mini_frames[2], "Journey: ",
                                           0, 0, 1, 0, 230, 0, 0,'news')
journey.configure(font= ('helvetica', 15))
from_station = proj2.create_label(mini_frames[9], "From: Station 0",
                                           0, 0, 1, 0, 200, 0, 0,'news')
from_station.configure(font= ('helvetica', 12))
to_station = proj2.create_label(mini_frames[9], "To: Station 0",
                                           1, 0, 1, 0, 220, 0, 0,'news')
to_station.configure(font= ('helvetica', 12))

fare = proj2.create_entry_with_label(mini_frames[3], 'Fare: ', 'helvetica', 15, '', None, 8,
                                           0, 0, 1, 0, 0, 220, 0, 0, 'w')
fare.insert(0, "$ 0")
fare.configure(font= ('helvetica', 15), state= 'readonly')

no_of_tix = proj2.create_spinbox_with_label(mini_frames[4], 'Number of Tickets: ', 'helvetica', 15, '', None, 1, 10, 8,
                                           0, 0, 1, 0, 0, 140, 0, 0, 'w')
no_of_tix.configure(font=('helvetica', 15), command= update_amount)
total_amount_label = proj2.create_label(mini_frames[5], "Total Amount: ",
                                           0, 0, 1, 0, 0, 0, 0,'w')
total_amount_label.configure(font=('helvetica', 15))
total_amount_indicator = proj2.create_label(mini_frames[5], "$ 0",
                                           0, 3, 1, 0, 160, 0, 0,'w')
total_amount_indicator.configure(font=('helvetica', 15))
currency_entry = proj2.create_entry_with_label(mini_frames[6], "Enter Currency Amount: ", 'helvetica', 15, '', None, 10,
                                           0, 0, 1, 0, 0, 100, 0, 0, 'w')
currency_entry.configure(font=('helvetica', 15))
currency_entry.bind('<KeyRelease>', update_change)
change_label = proj2.create_label(mini_frames[7], "Change: ",
                                           0, 0, 1, 0, 0, 0, 0,'w')
change_label.configure(font=('helvetica', 15))
change_indicator = proj2.create_label(mini_frames[7], "$ 0",
                                           0, 1, 1, 0, 210, 0, 0,'w')
message_status = proj2.create_label(mini_frames[7], '*', 1, 0, 2, 0, 0, 0, 0, 'w')
change_indicator.configure(font=('helvetica', 15))

return_button_1 = proj.button(mini_frames[8], 'Return', 15, 2,
                            0, 0, 0, 0, 0, 0, '#1181C8', 'white')
return_button_1.configure(command= lambda :(clear(), proj.other_page(home_page_frame)))
clear_button = proj.button(mini_frames[8], 'Clear', 15, 2,
                            0, 1, 10, 10, 0, 0, '#00A8A8', 'white')
clear_button.configure(command= clear)
confirm_button = proj.button(mini_frames[8], 'Confirm', 15, 2,
                            0, 2, 0, 0, 0, 0, '#209B3D', 'white')
confirm_button.configure(command=confirm)
# ___________________________________LVL 2: Contents seen in buy_ticket_onetime_frame_________________________________________________

# ___________________________________LVL 2: Contents seen in create_account_frame_________________________________________________
message_info_1 = proj2.create_label(mini_frames_2[0], '* Inserting an image is optional',
                                    0, 1, 1, 0, 0, 0, 0, 'n')
message_info_1_ = proj2.create_label(mini_frames_2[0], ' * Fields containing * are needed',
                                    0, 1, 1, 0, 0, 25, 0, 'n')
message_info_1.configure(font= ('helvetica', 10, 'italic'))
message_info_1_.configure(font= ('helvetica', 10, 'italic'))
label_names_1 = ['First Name', 'Middle Name', 'Last Name']
label_names_2 = ['Password*', 'Confirm Password*']
entries_in_create_account = []
for i in label_names_1:
    entry = proj2.create_entry_with_label(mini_frames_2[1], i, 'helvetica', 13, '', None, 18,
                                        0, x, 1, x, 0, 10, 0, 0, 'w')
    entries_in_create_account.append(entry)
    x += 1
    if x == len(label_names_1):
        x = 0

username_acc = proj2.create_entry_with_label(mini_frames_2[2], 'Username*', 'helvetica', 13, '', None,
                                      23, 0, 0, 1, 0, 0, 10, 0, 0, 'w')
entries_in_create_account.append(username_acc)

email = proj2.create_entry_with_label(mini_frames_2[2], 'Email', 'helvetica', 13, '', None,
                                      30, 0, 1, 1, 1, 0, 0, 0, 0, 'w')
entries_in_create_account.append(email)

message_info_2 = proj2.create_label(mini_frames_2[2], '* Incase of Access loss',
                                    3, 1, 1, 0, 0, 0, 0,'w')
message_info_2.configure(font= ('helvetica', 10, 'italic'))


for i in label_names_2:
    entry2 = proj2.create_entry_with_label(mini_frames_2[3], i, 'helvetica', 13, '', None, 18,
                                        0, x, 1, x, 0, 10, 0, 0, 'w')
    entries_in_create_account.append(entry2)
    x += 1
    if x == len(label_names_2):
        x = 0
        for index in [5, 6]:
            entries_in_create_account[index].configure(show='*')
            entries_in_create_account[index].bind('<KeyRelease>', check_password_validity)
            entries_in_create_account[6].configure(state='readonly')
message_info_3 = proj2.create_label(mini_frames_2[3], '*', 0, 2, 1, 0, 0, 0, 0, 'w')


return_button_2 = proj.button(mini_frames_2[4], 'Return', 15, 1,
                            0, 0, 0, 10, 0, 0, '#1181C8', 'white')
return_button_2.configure(command= lambda :(clear() ,proj.other_page(home_page_frame)))
clear_button_2 = proj.button(mini_frames_2[4], 'Clear', 15, 1,
                             0, 1, 0, 0, 0, 0, '#00A8A8', 'white')
clear_button_2.configure(command= clear)
save_button = proj.button(mini_frames_2[4], 'Create Account', 15, 1,
                          0, 3, 10, 0, 0, 0, '#209B3D', 'white')
save_button.configure(command= save_new_user)
# ___________________________________LVL 2: Contents seen in create_account_frame_________________________________________________


# ___________________________________LVL 2: Contents seen in buy_ticket_as_user_frame_________________________________________________
username = proj2.create_entry_with_label(mini_frames_3[1], 'Username: ', 'helvetica', 15, '',
                                         None, 20, 0, 0, 0, 1, 0, 0, 0, 0, 'w')
password = proj2.create_entry_with_label(mini_frames_3[2], 'Password: ', 'helvetica', 15, '',
                                         None, 20, 1, 0, 1, 1, 0, 0, 0, 0, 'w')
password.configure(show= '*')
log_in = proj.button(mini_frames_3[5], 'Log in', 15, 1, 0, 0, 130, 0 ,0, 0, '#209B3D', 'white')
log_in.configure(command= login)
forgor_password = proj2.create_label(mini_frames_3[3], 'Forgot Password?',
                                     0, 0, 1, 100, 0, 0, 0, 'w')
forgor_password.configure(cursor= 'hand2')
forgor_password.bind('<Button-1>', forgot_password)

return_button_3 = proj.button(mini_frames_3[5], 'Return', 15, 1,
                              0, 0, 0, 130, 0, 0, '#1181C8', 'white')
return_button_3.configure(command= lambda :(clear(), proj.other_page(home_page_frame)))
# ___________________________________LVL 2: Contents seen in buy_ticket_as_user_frame_________________________________________________


# ___________________________________LVL 2: Contents seen in user_frame_________________________________________________
label_info_frame = proj.frame_lvl_(mini_frames_4[0], None, 0, 1, 'n')
greetings = proj2.create_label(label_info_frame, 'Hello, User!',
                               0, 0, 1, 0, 0, 0, 0,'nw')
greetings.configure(font= ('helvetica', 10, 'italic'))
total_points = proj2.create_label(label_info_frame, 'Your Total points is: ',
                                  1 , 0, 1, 0, 0, 0, 0,'nw')
total_points.configure(font= ('helvetica', 10, 'italic'))

current_station_label_2 = proj2.create_label(mini_frames_4[1], "You're in: Station 0",
                                           0, 0, 1, 0, 0, 0, 0,'w')
current_station_label_2.configure(font= ('helvetica', 15))
station_option_2 = proj2.create_combobox_with_label(mini_frames_4[2], 'Your Destination: ', 'helvetica',
                                                  15, '', options, None, 15,0, 0, 1, 0,
                                                  10, 10, 0, 0, 'n')
station_option_2.configure(font=('helvetica', 15))
station_option_2.current(4)
station_option_2.bind("<<ComboboxSelected>>", station_selected_and_fare_2)

journey_2 = proj2.create_label(mini_frames_4[3], "Journey: ",
                                           0, 0, 1, 0, 0, 0, 0,'news')
journey_2.configure(font= ('helvetica', 15))
from_station_2 = proj2.create_label(mini_frames_4[10], "From: Station 0",
                                           0, 0, 1, 0, 0, 0, 0,'news')
from_station_2.configure(font= ('helvetica', 12))
to_station_2 = proj2.create_label(mini_frames_4[10], "To: Station 0",
                                           1, 0, 1, 0, 0, 0, 0,'news')
to_station_2.configure(font= ('helvetica', 12))
fare_2 = proj2.create_entry_with_label(mini_frames_4[4], 'Fare: ', 'helvetica', 15, '', None, 10,
                                           0, 0, 1, 0, 20, 20, 0, 0, 'n')
fare_2.insert(0, "$ 0")
fare_2.configure(font= ('helvetica', 15), state= 'readonly')

no_of_tix_2 = proj2.create_spinbox_with_label(mini_frames_4[4], 'Number of Tickets: ', 'helvetica', 15, '', None, 1, 10, 10,
                                           0, 0, 1, 0, 0, 0, 0, 0, 'n')
no_of_tix_2.configure(font=('Times New Roman', 15), command= update_amount_2)
total_amount_label_2 = proj2.create_label(mini_frames_4[5], "Total Amount: ",
                                           0, 0, 1, 0, 0, 0, 0,'w')
total_amount_label_2.configure(font=('helvetica', 15))
total_amount_indicator_2 = proj2.create_label(mini_frames_4[5], "$ 0",
                                           0, 1, 1, 0, 0, 0, 0,'w')
total_amount_indicator_2.configure(font=('helvetica', 15))
currency_entry_2 = proj2.create_entry_with_label(mini_frames_4[6], "Enter Currency Amount: ", 'helvetica', 15, '', None, 10,
                                           0, 0, 1, 0, 0, 0, 0, 0, 'n')
currency_entry_2.configure(font=('helvetica', 15))
currency_entry_2.bind('<KeyRelease>', update_change_2)
change_label_2 = proj2.create_label(mini_frames_4[7], "Change: ",
                                           0, 0, 1, 0, 0, 0, 0,'w')
change_label_2.configure(font=('helvetica', 15))
change_indicator_2 = proj2.create_label(mini_frames_4[7], "$ 0",
                                           0, 1, 1, 0, 0, 0, 0,'w')
message_status_2 = proj2.create_label(mini_frames_4[7], '*', 1, 0, 2, 0, 0, 0, 0, 'w')
change_indicator_2.configure(font=('helvetica', 15))

return_button_4 = proj.button(mini_frames_4[9], 'Return', 15, 1, 0, 0, 0, 10, 0, 0, None, None)
return_button_4.configure(command= lambda :(clear(), proj.other_page(buy_ticket_as_user_frame)))

clear_button_3 = proj.button(mini_frames_4[9], 'Clear', 15, 1, 0, 1, 0, 0, 0, 0, None, None)
clear_button_3.configure(command= clear)

confirm_button_2 = proj.button(mini_frames_4[9], 'Confirm', 15, 1, 0, 2, 10, 0, 0, 0, None, None)
confirm_button_2.configure(command= confirm_2)
# ___________________________________LVL 2: Contents seen in user_frame_________________________________________________

# ___________________________________LVL 2: Contents seen in forgot_password_frame_________________________________________________
email_ = proj2.create_entry_with_label(mini_frames_5[1], 'Email: ', 'helvetica', 15, '', None,
                                       25, 1, 0, 1, 1, 0, 0, 0, 0, 'w')
username_forgor = proj2.create_entry_with_label(mini_frames_5[1], 'Username: ', 'helvetica', 15, '', None,
                                       25, 0, 0, 0, 1, 0, 0, 10, 0, 'w')
new_password = proj2.create_entry_with_label(mini_frames_5[2], 'New Password: ', 'helvetica', 12, '',
                                         None, 20, 0, 0, 0, 1, 0, 0, 0, 0, 'w')
confirm_new_password = proj2.create_entry_with_label(mini_frames_5[2], 'Confirm New Password: ', 'helvetica', 12, '',
                                         None, 20, 1, 0, 1, 1, 0, 0, 10, 0, 'w')
new_password.configure(state= 'readonly')
confirm_new_password.configure(state= 'readonly')
new_password.bind('<KeyRelease>', check_password_validity_2)
confirm_new_password.bind('<KeyRelease>', check_password_validity_2)

return_button_5 = proj.button(mini_frames_5[3], 'Return', 15, 1, 0, 0, 0, 10, 10, 0, None, None)
return_button_5.configure(command= lambda :(clear(), proj.other_page(home_page_frame)))

search = proj.button(mini_frames_5[3], 'Search User', 15, 1, 0, 1, 0, 0, 10, 0, None, None)
search.configure(command= search_username)

confirm_button_3 = proj.button(mini_frames_5[3], 'Confirm', 15, 1, 0, 2, 10, 0, 10, 0, None, None)
confirm_button_3.configure(command= lambda :(confirm_3()))

message_info_4 = proj.label(mini_frames_5[4], '*', 0, 0)
# ___________________________________LVL 2: Contents seen in forgot_password_frame_________________________________________________

# ___________________________________LVL 2:_________________________________________________
# ____________________________________________________CONTENTS__________________________________________________________
home_page_frame.tkraise()
root.mainloop()
