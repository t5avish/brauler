import customtkinter as ctk
from course import Course
from scheduler import scheduler

class GUI:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.app = ctk.CTk()
        self.app.title("Brauler")
        self.courses = []
        self.layout()
        self.app.mainloop()

    def layout(self):
        self.main_frame = ctk.CTkFrame(master=self.app)
        self.main_frame.pack(padx=40, pady=20, fill="both", expand="True")

        self.topic_label = ctk.CTkLabel(master=self.main_frame, text="בניית מערכת שעות", font=('Narkisim', 50), justify="right")
        self.topic_label.pack(pady=10, padx=10)

        self.left_frame = ctk.CTkFrame(master=self.main_frame)
        self.left_frame.pack(padx=10, pady=10, fill="both", expand="True", side="left")

        self.top_left_frame = ctk.CTkFrame(master=self.left_frame)
        self.top_left_frame.pack(padx=10, pady=10, fill="both", expand="True")

        self.scheduler_button = ctk.CTkButton(master=self.left_frame , text="צור מערכת",font=("Narkisim",18), command=lambda : self.generate_schedule())
        self.scheduler_button.pack(pady=10, padx=10)

        self.right_frame = ctk.CTkFrame(master=self.main_frame)
        self.right_frame.pack(padx=10, pady=10, fill="both", expand="True", side="left")

        self.top_right_frame = ctk.CTkFrame(master=self.right_frame)
        self.top_right_frame.pack(padx=10, pady=10, fill="both", expand="True")

        self.bottom_right_frame = ctk.CTkFrame(master=self.right_frame)
        self.bottom_right_frame.pack(padx=10, pady=10, fill="both", expand="True")

        self.top_right_label = ctk.CTkLabel(master=self.top_right_frame, text="הקורסים שנוספו עד כה", font=('Narkisim', 30), justify="right")
        self.top_right_label.pack(pady=10, padx=10)

        self.bottom_right_label = ctk.CTkLabel(master=self.bottom_right_frame, text="הוספת קורס חדש", font=('Narkisim', 30), justify="right")
        self.bottom_right_label.pack(pady=10, padx=10)

        self.add_course_entry = ctk.CTkEntry(master = self.bottom_right_frame)
        self.add_course_entry.pack(pady=10, padx=10)

        self.add_course_button = ctk.CTkButton(master = self.bottom_right_frame, text="הוסף",font=("Narkisim",18), command=self.add_course)
        self.add_course_button.pack(pady=10, padx=10)

    def add_course(self):
        id = self.add_course_entry.get()
        try:
            course = Course(int(id))
            self.courses.append(course)
        except:
            self.add_course_entry.configure(text_color="red")
            self.add_course_entry.after(1000,lambda: self.add_course_entry.configure(text_color="white"))
            self.add_course_entry.after(1000,lambda: self.add_course_entry.delete(0, 'end'))
            return

        course_frame = ctk.CTkFrame(master=self.top_right_frame)
        course_frame.pack(padx=10, pady=10,fill="both", expand="True")

        course_remove_button = ctk.CTkButton(master=course_frame, text="הסר", font=("Narkisim", 18), command = lambda : self.delete_course(course_frame, course))
        course_remove_button.pack(pady=10, padx=10, side="left")

        about_button = ctk.CTkButton(master=course_frame, text="פרטים", font=("Narkisim", 18), command = lambda : self.course_info(course))
        about_button.pack(pady=10, padx=10, side="left")

        label_text = str(course.id) + " - " + str(course.name)
        course_label = ctk.CTkLabel(master=course_frame, text=label_text, font=('Narkisim', 18), justify="left")
        course_label.pack(pady=10, padx=10, side="right")

        self.add_course_entry.delete(0, 'end')

    def delete_course(self, frame, course):
        self.courses.remove(course)
        frame.destroy()

    def course_info(self, course):
        self.remove_all_widgets(self.top_left_frame)
        title_label = ctk.CTkLabel(master=self.top_left_frame, text="פרטי קורס " + str(course.name), font=('Narkisim', 30), justify="right")
        title_label.pack(pady=10, padx=10)
        point_label = ctk.CTkLabel(master=self.top_left_frame, text="נקודות זכות: " + str(course.points), font=('Narkisim', 22), justify="right")
        point_label.pack(pady=10, padx=10)
        about_label = ctk.CTkLabel(master=self.top_left_frame, text=course.about, font=('Narkisim', 14), justify="right", wraplength=len(course.about))
        about_label.pack(padx=10)

        if len(course.lectures) > 0:
            lecture_topic_label = ctk.CTkLabel(master=self.top_left_frame, text="הרצאות", font=('Narkisim', 22), justify="right")
            lecture_topic_label.pack(padx=10)

            for lecture in course.lectures:
                lecture_info = lecture.day + " " +  lecture.start + " " +  lecture.finish + " " +  lecture.lecturer
                lecture_label = ctk.CTkLabel(master=self.top_left_frame, text=lecture_info, font=('Narkisim', 14), justify="right")
                lecture_label.pack(padx=10)

        if len(course.practices) > 0:
            practices_topic_label = ctk.CTkLabel(master=self.top_left_frame, text="תרגולים", font=('Narkisim', 22), justify="right")
            practices_topic_label.pack(padx=10)

            for practice in course.practices:
                practice_info = practice.day + " " +  practice.start + " " +  practice.finish + " " +  practice.lecturer
                practice_label = ctk.CTkLabel(master=self.top_left_frame, text=practice_info, font=('Narkisim', 14), justify="right")
                practice_label.pack(padx=10)

        if len(course.labs) > 0:
            labs_topic_label = ctk.CTkLabel(master=self.top_left_frame, text="מעבדות", font=('Narkisim', 22), justify="right")
            labs_topic_label.pack(padx=10)

            for lab in course.labs:
                lab_info = lab.day + " " +  lab.start + " " +  lab.finish + " " +  lab.lecturer
                lab_label = ctk.CTkLabel(master=self.top_left_frame, text=lab_info, font=('Narkisim', 14), justify="right")
                lab_label.pack(padx=10)

        about_button = ctk.CTkButton(master=self.top_left_frame, text="סגור", font=("Narkisim", 18), command = lambda : self.remove_all_widgets(self.top_left_frame))
        about_button.pack(pady=10, padx=10)

    def remove_all_widgets(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        frame.update_idletasks()
        frame_width = 200  
        frame_height = 100
        frame.configure(width=frame_width, height=frame_height)

    def generate_schedule(self):
        schedele, latest = scheduler(self.courses)

        if schedele:
            days = {'א' : 0, 'ב' : 1, 'ג' : 2, 'ד' : 3, 'ה' : 4, 'ו' : 5}
            hours_dict = {"08:30": 0, "09:30": 1, "10:30" : 2 ,"11:30": 3,"12:20": 4, "12:50": 4, "13:50": 5, "14:50": 6, "15:50": 7, "16:50": 8, "17:50": 9, "18:50": 10, "19:50": 11, "20:50": 12, "21:50": 13}
            hours_list = ["08:30", "09:30", "10:30", "11:30", "12:50", "13:50", "14:50", "15:50", "16:50", "17:50", "18:50", "19:50", "20:50", "21:50"]

            for index, value in enumerate(hours_list):
                if value == latest:
                    latest_index = index

            schedule_window = ctk.CTkToplevel()
            schedule_window.title("schedule")
            hours_frame = ctk.CTkFrame(master=schedule_window)
            hours_frame.pack(padx=10, pady=10, side="right", expand="True", fill="both")

            empty_label = ctk.CTkLabel(master=hours_frame, text="", font=('Narkisim', 30), justify="right")
            empty_label.pack(pady=20, padx=10)
            
            labels_list = []

            for index in range(latest_index + 1):
                hour_label = ctk.CTkLabel(master=hours_frame, text=hours_list[index], font=('Narkisim', 30), justify="right")
                hour_label.pack(pady=20, padx=10)
            for day in days:
                day_frame = ctk.CTkFrame(master=schedule_window)
                day_frame.pack(padx=10, pady=10, side="right", expand="True", fill="both")

                days_label = ctk.CTkLabel(master=day_frame, text=day, font=('Narkisim', 30), justify="right")
                days_label.pack(pady=20, padx=10)
                day_labels = []
                for index in range(latest_index + 1):
                    label = ctk.CTkLabel(master=day_frame, text="-", font=('Narkisim', 16), justify="right")
                    day_labels.append(label)
                    label.pack(pady=20, padx=10)
                labels_list.append(day_labels)
            
            for course, lessons in schedele:
                course_name = course.name
                for lesson in lessons:
                    type = lesson.type
                    lecturer = lesson.lecturer
                    day_index = days[lesson.day]
                    start_index = hours_dict[lesson.start]
                    finish_index = hours_dict[lesson.finish]
                    for i in range(start_index, finish_index):
                        info = course_name + "\n" + type + "   " + lecturer
                        labels_list[day_index][i].configure(text=info)
        else:
            return
