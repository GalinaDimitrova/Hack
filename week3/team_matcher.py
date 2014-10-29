import requests
from random import shuffle

def list_courses(r):
    courses_list = []
    for i in range(len(r.json())):
        for j in range(len(r.json()[i]["courses"])):
            if r.json()[i]["courses"][j]["name"] not in courses_list:
                courses_list.append(r.json()[i]["courses"][j]["name"])

    for index, item in enumerate(courses_list):
        print("[{}] {}".format(index + 1, item))
    return courses_list


def match_team(r, course_id, team_size, group_time):
    courses_list = list_courses(r)
    course = courses_list[course_id - 1]
    list_of_students = []

    for i in range(len(r.json())):
        if r.json()[i]["available"] == True:
            for j in range(len(r.json()[i]["courses"])):
                if r.json()[i]["courses"][j]["name"] == course:
                    if r.json()[i]["courses"][j]["group"] == group_time:
                        list_of_students.append(r.json()[i]["name"])
    random_match(list_of_students, team_size)


def random_match(list_of_students, team_size):
    shuffle(list_of_students)
    for i in range(0, len(list_of_students)):
        if i % team_size == 0:
            print("============")
        print(list_of_students[i])


def main():
    r = requests.get("https://hackbulgaria.com/api/students/", verify=False)
    r.status_code

    match_team(r, 5, 2, 1)
    match_team(r, 5, 3, 1)


if __name__ == "__main__":
    main()
