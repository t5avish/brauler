from data_parser import Parser
from bidi.algorithm import get_display

class Lesson:
    def __init__(self, type, day, start, finish, lecturer):
        self.type = type
        self.day = day
        self.start = start
        self.finish = finish
        self.lecturer = lecturer

    def __str__(self):
        return get_display(self.type + " " + self.day + " " + self.start + " " + self.finish + " " + self.lecturer  + "\n")

class Course:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.points = 0.0
        self.lectures = []
        self.labs = []
        self.practices = []
        self.about = ""
        self.get_course_data()
    
    def add_lecture(self, lecture):
        self.lectures.append(lecture)

    def add_lab(self,lab):
        self.labs.append(lab)
    
    def add_practice(self, practice):
        self.practices.append(practice)

    def about_parser(self, about_list):
        self.points = float(about_list[0].split(" ")[5])
        for index in range(1, len(about_list)):
            self.about += str(about_list[index])

    def get_course_data(self):
        data = Parser(self.id)
        self.name = data.get_name()
        about_list = data.get_about()
        self.about_parser(about_list)
        for i in range(len(data.data_list)):
            type = data.types_list[i]
            row = [row.text.strip() for row in data.data_list[i].find_all('td')]
            lesson = Lesson(type, row[1], row[2], row[3], row[4])
            
            match type:
                case "הרצאה":
                    self.add_lecture(lesson)
                case "תרגיל":
                    self.add_practice(lesson)
                case "מעבדה":
                    self.add_lab(lesson)
                case _:
                    pass

    def __str__(self):
        str = ""
        str += "Course: "  + "\n"
        str += "LECS:" + "\n"
        for lec in self.lectures:
            str += lec.__str__() + "\n"
        str += "PRACS:" + "\n"
        for prac in self.practices:
           str += prac.__str__()  + "\n"
        str += "LABS:" + "\n"
        for lab in self.labs:
            str += lab.__str__()  + "\n"
        return str