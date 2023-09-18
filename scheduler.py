from itertools import combinations
from datetime import datetime

def do_lessons_overlap(lesson1, lesson2):
    start_datetime1 = datetime.strptime(lesson1.start, '%H:%M')
    finish_datetime1 = datetime.strptime(lesson1.finish, '%H:%M')
    start_datetime2 = datetime.strptime(lesson2.start, '%H:%M')
    finish_datetime2 = datetime.strptime(lesson2.finish, '%H:%M')

    if lesson1.day == lesson2.day:
        if start_datetime1 <= finish_datetime2 and start_datetime2 <= finish_datetime1:
            return True
    return False

def find_non_overlapping_lessons(course, max_lectures, max_labs, max_practices):
    all_lessons = course.lectures + course.practices + course.labs
    for size in range(1, len(all_lessons) + 1):
        for combo in combinations(all_lessons, size):
            lectures = [lesson for lesson in combo if lesson.type == 'הרצאה']
            labs = [lesson for lesson in combo if lesson.type == 'מעבדה']
            practices = [lesson for lesson in combo if lesson.type == 'תרגיל']

            if (len(lectures) <= max_lectures and len(labs) <= max_labs and len(practices) <= max_practices and
                all(not do_lessons_overlap(lesson1, lesson2) for lesson1, lesson2 in combinations(combo, 2))
            ):
                yield combo

def find_best_schedule(courses, max_lectures, max_labs, max_practices):
    best_schedule = None
    best_score = -1

    for schedule in generate_schedules(courses, max_lectures, max_labs, max_practices):
        score = calculate_schedule_score(schedule)    
        if score > best_score:
            best_schedule = schedule
            best_score = score
    return best_schedule

def generate_schedules(courses, max_lectures, max_labs, max_practices):
    if not courses:
        yield []
        return

    first_course, rest_courses = courses[0], courses[1:]  
    for schedule in generate_schedules(rest_courses, max_lectures, max_labs, max_practices):
        for lessons in find_non_overlapping_lessons(first_course, max_lectures, max_labs, max_practices):
            if all(not any(do_lessons_overlap(lesson1, lesson2) for _, lessons2 in schedule for lesson2 in lessons2 if lesson2.type == 'הרצאה') for lesson1 in lessons):
                if has_required_lessons(first_course, lessons):
                    yield [(first_course, lessons)] + schedule

def calculate_schedule_score(schedule):
    return sum(len(lessons) for _, lessons in schedule)

def has_required_lessons(course, lessons):
    has_lecture = any(lesson.type == 'הרצאה' for lesson in lessons)
    has_lab = any(lesson.type == 'מעבדה' for lesson in lessons)
    has_practice = any(lesson.type == 'תרגיל' for lesson in lessons)
    return (not course.lectures or has_lecture) and (not course.labs or has_lab) and (not course.practices or has_practice)

def scheduler(courses):
    schedule = find_best_schedule(courses, 1, 1, 1)
    latest = datetime.strptime("8:30", '%H:%M').strftime("%H:%M")
    for _, lessons in schedule:
        for lesson in lessons:
            time = datetime.strptime(lesson.finish, '%H:%M').strftime("%H:%M")
            if time > latest:
                latest = time
    return schedule, latest