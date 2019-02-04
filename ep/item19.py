
from collections import defaultdict


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
    """ Change SimpleGradebook to include grades by subject.
    """

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


class WeightedGradebook(object):
    """
    Change WeightedGradebook to make the score in each subject is weighted.
    For example, final is more weighted than homework.
    """

    def __init__(self):
        self._grade = {}

    def add_student(self, name):
        self._grade[name] = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grade[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grade[name]
        total, count = 0.0, 0

        for grades in by_subject.values():
            subject_total, subject_weight = 0.0, 0
            for score, weight in grades:
                subject_total = score * weight
                subject_weight = weight

            total += subject_total / subject_weight
            count += 1

        return total / count


def main_weighted():
    book = WeightedGradebook()
    book.add_student('Isaac')

    book.report_grade('Isaac', 'Math', 90, 0.90)
    book.report_grade('Isaac', 'Math', 85, 0.10)
    book.report_grade('Isaac', 'Gym', 95, 0.20)
    book.report_grade('Isaac', 'Gym', 80, 0.20)

    print(book.average_grade('Isaac'))


class Score(object):
    """Weighted score."""

    def __init__(self, score, weight):
        self.score = score
        self.weight = weight

    def weighted_score(self):
        return self.score * self.weight


class Subject(object):
    """Keeping track of weighted scores for a subject"""

    def __init__(self):
        self._grades = []

    def add_score(self, score, weight):
        self._grades.append(Score(score, weight))

    def average_score(self):
        total = sum(e.weighted_score() for e in self._grades)
        weight = sum(e.weight for e in self._grades)
        return total / weight


class Student(object):
    """Keeping track of subjects for a student"""

    def __init__(self):
        self._subjects = defaultdict(Subject)

    def subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        """ Average grade over all subjects"""
        count = len(self._subjects)
        total = sum(e.average_score() for e in self._subjects.values())
        return total / count


class ClassGradebook(object):
    """
    Change WeightedGradebook to make the score in each subject is weighted.
    For example, final is more weighted than homework.
    """

    def __init__(self):
        self._book = defaultdict(Student)

    def student(self, name):
        return self._book[name]

    def report_grade(self, name, subject, score, weight):
        student = self._book[name]
        student._subjects[subject].add_score(score, weight)

    def average_grade(self, name):
        student = self._book[name]
        return student.average_grade()


def main_class():
    book = ClassGradebook()

    book.report_grade('Isaac', 'Math', 90, 0.90)
    book.report_grade('Isaac', 'Math', 85, 0.10)
    book.report_grade('Isaac', 'Gym', 95, 0.20)
    book.report_grade('Isaac', 'Gym', 80, 0.20)

    print(book.average_grade('Isaac'))


def main_class_2():
    """Helper classes help easier to use interface"""
    book = ClassGradebook()

    isaac = book.student('Isaac')
    math = isaac.subject('Math')
    math.add_score(90, 0.90)
    math.add_score(85, 0.10)
    gym = isaac.subject('Gym')
    gym.add_score(95, 0.20)
    gym.add_score(80, 0.20)

    print(isaac.average_grade())
    # Equivalent to the old interface
    print(book.average_grade('Isaac'))


if __name__ == '__main__':
    # main_simple()
    # main_by_subject()
    # main_weighted()
    main_class_2()
