class Worker:
    def __init__(self, name, surname, position, **kwargs):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = kwargs


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        try:
            total_wage = sum(self._income.values())
        except TypeError:
            print("This method supports only numbers")
        else:
            return total_wage


qa_manager = Position("Anna", "Potter", "QA Manager", wage=25000, bonus=30000)
print(qa_manager.get_full_name())
print(qa_manager.get_total_income())

developer = Position("Olivia", "Johnson", "Junior developer", wage=40000, bonus=3456.55)
print(developer.get_full_name())
print(developer.get_total_income())

developer_1 = Position("Tom", "Brown", "Senior developer", wage="60000", bonus=4567)
print(developer_1.get_full_name())
print(developer_1.get_total_income())
