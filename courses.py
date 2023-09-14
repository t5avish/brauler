import requests
from bs4 import BeautifulSoup
from bidi.algorithm import get_display
import re
from lesson import Course, Lesson

url = "https://info.braude.ac.il/yedion/fireflyweb.aspx?APPNAME=&PRGNAME=S_LOOK_FOR_NOSE&ARGUMENTS=SubjectCode&R1C19=0&SubjectCode=61778&R1C2=1&R1C5=1&R1C6=+1&R1C7=1&R1C8=++54&R1C9=++54&R1C10=&R1C28=++54&R1C29=0&R1C30=0&R1C20=0&Location=0&R1C21=12%2F09%2F2023&R1C22=12%2F09%2F2023"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")


types_list = doc.find_all(string=re.compile("קורס מסוג"))
for number, type_string in enumerate(types_list):
    types_list[number] = re.sub(r'\s+', '', type_string).replace("קורסמסוג",'')


info_list = doc.find_all("tbody")

last_index = len(info_list)
for number, info in enumerate(info_list):
    child = info_list[number].findChildren("tr")
    if child == []:
        last_index = number
        break

info_list = info_list[0:last_index]

course = Course(12345)

for i in range(len(info_list)):
    type = types_list[i]
    row = [row.text.strip() for row in info_list[i].find_all('td')]
    lesson = Lesson(type, row[1], row[2], row[3], row[4])
    match type:
        case "הרצאה":
            course.add_lecture(lesson)
        case "תרגיל":
            course.add_practice(lesson)
        case "מעבדה":
            course.add_lab(lesson)
        case _:
            pass

print(course)
            
            
    
        








"""
with open("work.html", "r", encoding="utf-8") as f:
    doc = BeautifulSoup(f, "html.parser")
"""





"""
with open("try.txt", "w", encoding="utf-8") as f:
    f.write(doc.prettify())
"""































#url = "https://info.braude.ac.il/yedion/fireflyweb.aspx?APPNAME=&PRGNAME=S_LOOK_FOR_NOSE&ARGUMENTS=SubjectCode&R1C19=0&SubjectCode=61752&R1C2=1&R1C5=1&R1C6=+1&R1C7=1&R1C8=++54&R1C9=++54&R1C10=&R1C28=++54&R1C29=0&R1C30=0&R1C20=0&Location=0&R1C21=12%2F09%2F2023&R1C22=12%2F09%2F2023"

#result = requests.get(url)
#doc = BeautifulSoup(result.text, "html.parser")
#type = doc.find_all(text=)