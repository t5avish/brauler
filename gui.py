import customtkinter as ctk
from course import Course

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def add_course():
    id = add_course_entry.get()
    
    try:
        course = Course(int(id))
    except:
        add_course_entry.configure(text_color="red")
        add_course_entry.after(1000,lambda: add_course_entry.configure(text_color="white"))
        add_course_entry.after(1000,lambda: add_course_entry.delete(0, 'end'))
        return

    course_frame = ctk.CTkFrame(master=top_right_frame)
    course_frame.pack(padx=10, pady=10, fill="both", expand="True")

    course_remove_button = ctk.CTkButton(master=course_frame, text="הסר", font=("Narkisim", 18), command = lambda : course_frame.destroy())
    course_remove_button.pack(pady=10, padx=10, side="left")

    label_text = str(course.id) + " - " + str(course.name)
    course_label = ctk.CTkLabel(master=course_frame, text=label_text, font=('Narkisim', 18), justify="left")
    course_label.pack(pady=10, padx=10, side="left")

    add_course_entry.delete(0, 'end')

app = ctk.CTk()

main_frame = ctk.CTkFrame(master=app)
main_frame.pack(padx=40, pady=20, fill="both", expand="True")

topic_label = ctk.CTkLabel(master=main_frame, text="בניית מערכת שעות", font=('Narkisim', 50), justify="right")
topic_label.pack(pady=10, padx=10)

left_frame = ctk.CTkFrame(master=main_frame)
left_frame.pack(padx=10, pady=10, fill="both", expand="True", side="left")

right_frame = ctk.CTkFrame(master=main_frame)
right_frame.pack(padx=10, pady=10, fill="both", expand="True", side="left")

top_right_frame = ctk.CTkFrame(master=right_frame)
top_right_frame.pack(padx=10, pady=10, fill="both", expand="True")

bottom_right_frame = ctk.CTkFrame(master=right_frame)
bottom_right_frame.pack(padx=10, pady=10, fill="both", expand="True")

top_right_label = ctk.CTkLabel(master=top_right_frame, text="הקורסים שנוספו עד כה", font=('Narkisim', 30), justify="right")
top_right_label.pack(pady=10, padx=10)

bottom_right_label = ctk.CTkLabel(master=bottom_right_frame, text="הוספת קורס חדש", font=('Narkisim', 30), justify="right")
bottom_right_label.pack(pady=10, padx=10)

add_course_entry = ctk.CTkEntry(master = bottom_right_frame)
add_course_entry.pack(pady=10, padx=10)

add_course_button = ctk.CTkButton(master = bottom_right_frame, text="הוסף",font=("Narkisim",18), command=add_course)
add_course_button.pack(pady=10, padx=10)

app.mainloop()
