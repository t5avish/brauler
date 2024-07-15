from data_parser import Parser

class Lesson:
    def __init__(self, type, day, start, finish, lecturer):
        self.type = type
        self.day = day
        self.start = start
        self.finish = finish
        self.lecturer = lecturer

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
        try:
            self.points = float(about_list[0].split(" ")[5])
            for index in range(1, len(about_list)):
                self.about += str(about_list[index])
        except:
                try:
                    self.points = float(about_list[0].split(" ")[3])
                except:
                    self.about = "Error loading data."

    def get_course_data(self):
        data = Parser(self.id)
        self.name = data.get_name()
        about_list = data.get_about()
        self.about_parser(about_list)
        for i in range(len(data.data_list)):
            type = data.types_list[i]
            row = [row.text.strip() for row in data.data_list[i].find_all('div', class_="row")[1]]
            lesson = Lesson(type, row[3], row[5], row[7], row[9])
            
            match type:
                case "הרצאה":
                    self.add_lecture(lesson)
                case "תרגיל":
                    self.add_practice(lesson)
                case "מעבדה":
                    self.add_lab(lesson)
                case _:
                    pass