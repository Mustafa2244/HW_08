import datetime

known_users = [
    {
        "name": "Adam",
        "birthday": datetime.date(2023, 4, 23)
    },
    {
        "name": "Bred",
        "birthday": datetime.date(2023, 4, 24)
    },
    {
        "name": "John",
        "birthday": datetime.date(2023, 4, 22)
    },
    {
        "name": "Nick",
        "birthday": datetime.date(2023, 4, 25)
    },
    {
        "name": "Bart",
        "birthday": datetime.date(2023, 4, 21)
    },
]


def get_birthday_per_week(users):
    congratulations = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    week_time = datetime.timedelta(days=7)
    for user in users:
        if datetime.date.today() < user["birthday"] < (datetime.date.today() + week_time):
            if 6 <= user["birthday"].isoweekday() <= 7:
                congratulations["Monday"].append(user["name"])
            else:
                day_index = user["birthday"].isoweekday() - 1
                day_name = list(congratulations.keys())[day_index]
                congratulations[day_name].append(user["name"])
    return congratulations


if __name__ == '__main__':
    birthdays = get_birthday_per_week(known_users)
    for day in birthdays:
        if birthdays[day]:
            print(f"{day}: {', '.join(birthdays[day])}")
