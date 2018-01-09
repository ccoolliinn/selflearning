import datetime
import collections


def get_birthday():
    day = datetime.date.today()
    delta = datetime.timedelta(days=1)

    while True:
        day_str = day.strftime("%Y%m%d")
        if is_all_diff(day_str):
            print(day)
            break

        day -= delta


def is_all_diff(l):
    counter = collections.Counter(l)

    return counter.most_common(1)[0][1] == 1


if __name__ == '__main__':
    get_birthday()