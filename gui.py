import customtkinter as ctk
from course import Course

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def add_course():
    id = add_course_entry.get()
    try:
        course = Course(int(id))
    except Exception as e:
        add_course_entry.configure(text_color="red")
        add_course_entry.after(1000,lambda: add_course_entry.configure(text_color="white"))
        add_course_entry.after(1000,lambda: add_course_entry.delete(0, 'end'))
        return

    course_frame = ctk.CTkFrame(master=top_right_frame)
    course_frame.pack(padx=10, pady=10,fill="both", expand="True")

    course_remove_button = ctk.CTkButton(master=course_frame, text="הסר", font=("Narkisim", 18), command = lambda : course_frame.destroy())
    course_remove_button.pack(pady=10, padx=10, side="left")

    about_button = ctk.CTkButton(master=course_frame, text="פרטים", font=("Narkisim", 18), command = lambda : course_info(course))
    about_button.pack(pady=10, padx=10, side="left")

    label_text = str(course.id) + " - " + str(course.name)
    course_label = ctk.CTkLabel(master=course_frame, text=label_text, font=('Narkisim', 18), justify="left")
    course_label.pack(pady=10, padx=10, side="right")

    add_course_entry.delete(0, 'end')

def course_info(course):
    remove_all_widgets(left_frame)
    title_label = ctk.CTkLabel(master=left_frame, text="פרטי קורס " + str(course.name), font=('Narkisim', 30), justify="right")
    title_label.pack(pady=10, padx=10)
    point_label = ctk.CTkLabel(master=left_frame, text="נקודות זכות: " + str(course.points), font=('Narkisim', 22), justify="right")
    point_label.pack(pady=10, padx=10)
    about_label = ctk.CTkLabel(master=left_frame, text=course.about, font=('Narkisim', 14), justify="right", wraplength=len(course.about))
    about_label.pack(padx=10)

    if len(course.lectures) > 0:
        lecture_topic_label = ctk.CTkLabel(master=left_frame, text="הרצאות", font=('Narkisim', 22), justify="right")
        lecture_topic_label.pack(padx=10)

        for lecture in course.lectures:
            lecture_info = lecture.day + " " +  lecture.start + " " +  lecture.finish + " " +  lecture.lecturer
            lecture_label = ctk.CTkLabel(master=left_frame, text=lecture_info, font=('Narkisim', 14), justify="right")
            lecture_label.pack(padx=10)

    if len(course.practices) > 0:
        practices_topic_label = ctk.CTkLabel(master=left_frame, text="תרגולים", font=('Narkisim', 22), justify="right")
        practices_topic_label.pack(padx=10)

        for practice in course.practices:
            practice_info = practice.day + " " +  practice.start + " " +  practice.finish + " " +  practice.lecturer
            practice_label = ctk.CTkLabel(master=left_frame, text=practice_info, font=('Narkisim', 14), justify="right")
            practice_label.pack(padx=10)

    if len(course.labs) > 0:
        labs_topic_label = ctk.CTkLabel(master=left_frame, text="מעבדות", font=('Narkisim', 22), justify="right")
        labs_topic_label.pack(padx=10)

        for lab in course.labs:
            lab_info = lab.day + " " +  lab.start + " " +  lab.finish + " " +  lab.lecturer
            lab_label = ctk.CTkLabel(master=left_frame, text=lab_info, font=('Narkisim', 14), justify="right")
            lab_label.pack(padx=10)

    about_button = ctk.CTkButton(master=left_frame, text="סגור", font=("Narkisim", 18), command = lambda : remove_all_widgets(left_frame))
    about_button.pack(pady=10, padx=10)

def remove_all_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.update_idletasks()
    frame_width = 200  
    frame_height = 100
    frame.configure(width=frame_width, height=frame_height)

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