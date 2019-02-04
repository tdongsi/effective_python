
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


def main_simple():
    book = SimpleGradebook()
    book.add_student('Isaac')

    book.report_grade('Isaac', 90)
    book.report_grade('Isaac', 85)
    book.report_grade('Isaac', 95)

    print(book.average_grade('Isaac'))


class BySubjectGradebook(object):

    def __init__(self):
        self._grade = {}

    def add_student(self, name):
        self._grade[name] = {}

    def report_grade(self, name, subject, score):
        by_subject = self._grade[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(score)

    def average_grade(self, name):
        by_subject = self._grade[name]
        total, count = 0.0, 0

        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)

        return total / count


def main_by_subject():
    book = BySubjectGradebook()
    book.add_student('Isaac')

    book.report_grade('Isaac', 'Math', 90)
    book.report_grade('Isaac', 'Math', 85)
    book.report_grade('Isaac', 'Gym', 95)
    book.report_grade('Isaac', 'Gym', 80)

    print(book.average_grade('Isaac'))


if __name__ == '__main__':
    # main_simple()
    main_by_subject()
