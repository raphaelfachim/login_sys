from tkinter import *

def sign_up():
    user_list = refresh_list()
    user = username_entry.get()
    pw = password_entry.get()
    if user in user_list:
        existing_user_win()
    elif len(pw) > 0:
        with open('log.txt', 'a+') as file:
            file.write(user.casefold() + '\n')
        file.close()

        with open('pw.txt', 'a+') as file:
            file.write(pw + '\n')
        file.close()
        user_registered_win()
    else: Label(root, text='   Insert a valid password    ').grid(row=16, column=0)

    password_entry.delete(0, len(pw))

def log_in():
    user_list = refresh_list()
    user = str(username_entry.get()).casefold()
    with open('pw.txt', 'r') as file:
        pw_list = file.readlines()
    file.close()

    c = 0
    for p in pw_list:
        pw_list[c] = p.replace('\n', '')
        c += 1
    pw = password_entry.get()
    if user in user_list:
        if pw == pw_list[user_list.index(user)]:
            Label(root, text = 'OK! Redirecting...').grid(row = 16, column = 0)
        else: Label(root, text = '             Bad password.           ').grid(row = 16, column = 0)
    else:
        Label(root, text='   User not registered    ').grid(row=16, column=0)

    password_entry.delete(0, len(pw))

def refresh_list():
    with open('log.txt', 'r') as file:
        user_list = file.readlines()
    file.close()
    c = 0
    for u in user_list:
        user_list[c] = u.replace('\n', '')
        c += 1
    return user_list

def close_window(win):
    win.destroy()

def existing_user_win():
    ext_win = Toplevel(root)
    ext_win.geometry("200x80")
    Label(ext_win, text = 'User already exist').pack()
    Button(ext_win, text = 'Cancel', command = lambda: close_window(ext_win)).pack(pady = 10)

def user_registered_win():
    reg_win = Toplevel(root)
    reg_win.geometry("200x80")
    Label(reg_win, text='User registered!').pack()
    Button(reg_win, text='OK', command=lambda: close_window(reg_win)).pack(pady=10)

def exit_program():
    sys.exit()

root = Tk()
root.geometry("400x300")

frame = Frame(root)
frame.grid(column = 0, row = 0)

Label(frame, text = 'Como deseja prosseguir:').grid(column = 1, row = 0, pady = 5)
Label(frame, text = 'Username').grid(column = 2, row = 2, pady = 2)


username_entry = Entry(frame, width = 20)
username_entry.grid(column = 2, row = 4, pady = 2)

Label(frame, text = 'Password').grid(column = 2, row = 6, pady = 2)

password_entry = Entry(frame, width = 20, show = "*")
password_entry.grid(column = 2, row = 8, pady = 2)

Button(frame, text='Sign Up', command = sign_up).grid(column = 2, row = 10, pady = 6)

Button(frame, text='Log In', command = log_in).grid(column = 2, row = 12, pady = 6)

Button(frame, text='Exit', command = exit_program).grid(column = 2, row = 14, pady=6)

root.title("Software Design")
root.mainloop()


