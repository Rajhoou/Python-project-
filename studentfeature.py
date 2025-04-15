

students = {
    "user1":"Ram",
    "user2":"shiva"

}
def view_profile(username):
    if username in students:
        print(f"\nYour profile:\nID: {username},Name: {students[username]}")
    else:
        print ("profile not found.")




