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
        self.lectures = []
        self.labs = []
        self.practices = []
    
    def add_lecture(self, lecture):
        self.lectures.append(lecture)

    def add_lab(self,lab):
        self.labs.append(lab)
    
    def add_practice(self, practice):
        self.practices.append(practice)

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
