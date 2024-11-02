#project start
from tkinter import Button, Label, Tk, Toplevel, Entry

# Function to generate the first story with user inputs
def Story11(parent):
    story_window = Toplevel(parent)
    story_window.title("A Memorable Day Story")
    story_window.geometry("300x300")
    story_window.config(bg="#FFDAB9")  # Light peach color

    # Prompt user for inputs
    Label(story_window, text="Enter a place:", bg="#FFDAB9", fg="#800000").pack(pady=5)  # Maroon text
    place = Entry(story_window, bg="#FFFACD", borderwidth=2, relief="groove")  # Lemon chiffon background
    place.pack()

    Label(story_window, text="Enter an activity:", bg="#FFDAB9", fg="#800000").pack(pady=5)
    activity = Entry(story_window, bg="#FFFACD", borderwidth=2, relief="groove")
    activity.pack()

    Label(story_window, text="Enter a friend's name:", bg="#FFDAB9", fg="#800000").pack(pady=5)
    friend = Entry(story_window, bg="#FFFACD", borderwidth=2, relief="groove")
    friend.pack()

    # Function to display the final story
    def display_story():
        story_text = f"One day, I went to {place.get()} with my friend {friend.get()}. We decided to {activity.get()} all day. It was unforgettable!"
        Label(story_window, text=story_text, wraplength=280, bg="#FFDAB9", fg="#000080").pack(pady=20)  # Navy blue text

    Button(story_window, text="Show Story", command=display_story, bg="#8B0000", fg="white").pack(pady=10)  # Dark red button

# Function for the second story
def Story12(parent):
    story_window = Toplevel(parent)
    story_window.title("A Funny Incident")
    story_window.geometry("300x300")
    story_window.config(bg="#E6E6FA")  # Lavender color

    Label(story_window, text="Enter an animal:", bg="#E6E6FA", fg="#4B0082").pack(pady=5)  # Indigo text
    animal = Entry(story_window, bg="#F5FFFA", borderwidth=2, relief="groove")  # Mint cream background
    animal.pack()

    Label(story_window, text="Enter a food:", bg="#E6E6FA", fg="#4B0082").pack(pady=5)
    food = Entry(story_window, bg="#F5FFFA", borderwidth=2, relief="groove")
    food.pack()

    Label(story_window, text="Enter an action:", bg="#E6E6FA", fg="#4B0082").pack(pady=5)
    action = Entry(story_window, bg="#F5FFFA", borderwidth=2, relief="groove")
    action.pack()

    def display_story():
        story_text = f"One day, I saw a {animal.get()} trying to {action.get()} with a {food.get()} in its mouth. It was hilarious!"
        Label(story_window, text=story_text, wraplength=280, bg="#E6E6FA", fg="#2E8B57").pack(pady=20)  # Sea green text

    Button(story_window, text="Show Story", command=display_story, bg="#4B0082", fg="white").pack(pady=10)  # Indigo button

# Function for the third story
def Story13(parent):
    story_window = Toplevel(parent)
    story_window.title("An Adventure")
    story_window.geometry("300x300")
    story_window.config(bg="#FFF0F5")  # Lavender blush color

    Label(story_window, text="Enter a vehicle:", bg="#FFF0F5", fg="#483D8B").pack(pady=5)  # Dark slate blue text
    vehicle = Entry(story_window, bg="#FAFAD2", borderwidth=2, relief="groove")  # Light goldenrod yellow background
    vehicle.pack()

    Label(story_window, text="Enter a destination:", bg="#FFF0F5", fg="#483D8B").pack(pady=5)
    destination = Entry(story_window, bg="#FAFAD2", borderwidth=2, relief="groove")
    destination.pack()

    Label(story_window, text="Enter a number:", bg="#FFF0F5", fg="#483D8B").pack(pady=5)
    number = Entry(story_window, bg="#FAFAD2", borderwidth=2, relief="groove")
    number.pack()

    def display_story():
        story_text = f"I traveled in a {vehicle.get()} to {destination.get()} with {number.get()} friends. It was the best adventure!"
        Label(story_window, text=story_text, wraplength=280, bg="#FFF0F5", fg="#8B4513").pack(pady=20)  # Saddle brown text

    Button(story_window, text="Show Story", command=display_story, bg="#483D8B", fg="white").pack(pady=10)  # Dark slate blue button

# Main window setup
Screen11 = Tk()  
Screen11.title("Mad Libs Generator")  
Screen11.geometry('400x400')  
Screen11.config(bg="#FFC0CB")  # Light pink background
Label(Screen11, text='Mad Libs Generator', font=("Calibri New Roman", 16, "bold"), bg="#FFC0CB", fg="#000080").place(x=120, y=20)  # Navy blue text

# Creating buttons for different stories
Story111Button = Button(Screen11, text='A Memorable Day', font=("Calibri New Roman", 13), command=lambda: Story11(Screen11), bg="#8B4513", fg="white")  
Story111Button.place(x=140, y=90)

Story112Button = Button(Screen11, text='A Funny Incident', font=("Calibri New Roman", 13), command=lambda: Story12(Screen11), bg="#8B4513", fg="white")  
Story112Button.place(x=140, y=150)

Story113Button = Button(Screen11, text='An Adventure', font=("Calibri New Roman", 13), command=lambda: Story13(Screen11), bg="#8B4513", fg="white")  
Story113Button.place(x=140, y=210)

Screen11.mainloop()
