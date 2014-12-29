import requests
import random


def get_all_courses():
    temp_result = []
    result = []
    temp = requests.get('http://hackbulgaria.com/api/students/', verify=False)
    for students in temp.json():
        for courses in range(0, len(students["courses"])):
            temp_result.append(students["courses"][courses]["name"])
    temp = set(temp_result)
    for key in temp:
        result.append(key)
    return result


def get_online_people_from_course(course, group):
    temp_result = []
    result = []
    temp = requests.get('http://hackbulgaria.com/api/students/', verify=False)
    for students in temp.json():
        for courses in range(0, len(students["courses"])):
            if (students["courses"][courses]["name"] == course) and (students["courses"][courses]["group"] == group) and students["available"]:
                temp_result.append(students["name"])
    temp = set(temp_result)
    for key in temp:
        result.append(key)
    return result


def match_command():
    print("Hello, you can use one the the following commands:\nlist_courses - this lists all the courses that are available now.\n\nlist_courses\nHere are the courses:")
    new_courses = get_all_courses()
    for idx, elem in enumerate(new_courses):
        print("[{}] {}".format(idx + 1, elem))

    input_str = input()
    flag = True
    for chars in range(0, 12):
        if input_str[chars] != "match_teams "[chars]:
            flag = False

    if flag:
        if (int(input_str[12]) > 0 and int(input_str[12]) < 10) and (int(input_str[16]) > 0 and int(input_str[16]) < 3):
            temp = sorted(get_online_people_from_course(new_courses[int(input_str[12]) - 1], int(input_str[16])), key=lambda k: random.random())
            for idx, elem in enumerate(temp):
                if idx % int(input_str[14]) == 0:
                    print("==========================")
                print(elem)
        else:
            print("match_teams <course_id>, <team_size>, <group_time>")
    else:
        print("match_teams <course_id>, <team_size>, <group_time>")


if __name__ == '__main__':
    match_command()