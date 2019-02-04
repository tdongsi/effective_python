
class SimpleGradebook(object):

    def __init__(self):
        self._grade = {}

    def add_student(self, name):
        self._grade[name] = []

    def report_grade(self, name, score):
        self._grade[name].append(score)

    def average_grade(self, name):
        grades = self._grade[name]
        return sum(grades) / len(grades)


class BySubjectGradebook(object):

    def __init__(self):
        self._grade = {}

    def add_student(self, name):
        self._grade[name] = []

    def report_grade(self, name, score):
        self._grade[name].append(score)

    def average_grade(self, name):
        grades = self._grade[name]
        return sum(grades) / len(grades)


def main_simple():
    book = SimpleGradebook()
    book.add_student('Isaac')

    book.report_grade('Isaac', 90)
    book.report_grade('Isaac', 85)
    book.report_grade('Isaac', 95)

    print(book.average_grade('Isaac'))


if __name__ == '__main__':
    main_simple()
