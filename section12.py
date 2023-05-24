class Friends:
    def __init__(self, connections: list):
        self.connections = connections

    def add(self, connection):
        if connection in self.connections:
            print(False)
        else:
            self.connections.add(frozenset(connection))
            print(True)

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(frozenset(connection))
            print(True)
        else:
            print(False)

    def names(self):
        print(set().union(*self.connections))

    def connected(self, connection):
        result = set()
        for connection in self.connections:
            if relation in connection:
                result.add(*(connection - set(relation)))
        print(result)



class Student:
    def __init__(self, name: str, group: str, grade: dict):
        self._name = name
        self._group = group
        self._grade = grade

    def all_average(subject):
        count = 0
        score = 0
        for i in Student.grade_all:
            all_subject_avarage = i.get(subject)
        for j in all_subject_avarage:
            score += j
            count += 1
    test = score / count
    return f"Средний балл по {subject} равен: {test:.1f}"

    def all_average(group):
        count = 0
        score = 0
        for i in Student.grade_all:
            all_group_avarage = i.get(group)
        for j in all_group_avarage:
            score += j
            count += 1
    test = score / count
    return f"Средний балл по {group} равен: {test:.1f}"
 



