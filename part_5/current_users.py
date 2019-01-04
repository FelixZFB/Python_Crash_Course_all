current_users = ['Felix','Feibi','Aric','Jodan','Kobi','Qibox']
new_users = ['Felix','Sony','Aric']

for new_user in new_users:
    if new_user in current_users:
        print("Sorry, " + new_user + " has been used, please try again.")
    else:
        print("You can use " + new_user + " as your name.")


