import datetime as dt

class Robot():
    """Standart model of robot."""

    def __init__(self, id):
        self.id: int = id

class WateringRobot(Robot):
    """Robot model for watering binary tree."""

    def __init__(self, id, volume):
        super().__init__(id)
        self.volume: float = volume

    def watering(self, tree, water_amount):
        if water_amount < 1:
            print(f'Необходимо налить ещё {1 - water_amount} л. воды.')
        if tree.water_amount + water_amount > 2:
            raise BaseException('Слишком много воды для полива.')
        tree.water_amount += water_amount

class CuttingRobot(Robot):
    """Robot model for cutting binary tree."""

    def __init__(self, id, amount_per_week = 0):
        super().__init__(id)
        self.amount_per_week: int = 0

    def cutting(self, tree, branches):
        if branches < 4:
            print(f'Необходимо отрезать ещё {4 - branches} ветки.')
        if tree.branch_amount < branches:
            raise BaseException('У дерева нет столько веток.')
        tree.branch_amount -= branches


class BinaryTree():
    """Model of binary tree."""

    def __init__(self, id, branch_amount, water_amount):
        self.id: int = id
        self.branch_amount: int = branch_amount
        self.water_amount: float = water_amount


class Record():
    """Model of record in the journal."""

    def __init__(self, time, action, robot):
        self.time = time
        self.action = action
        self.robot = robot


class Journal():
    """Standart model of working with binary tree."""

    def __init__(self, tree, history = [], amount_of_water = 0, cut_branches = 0):
        self.history: list = []
        self.tree: BinaryTree = tree
        self.amount_of_water: float = 0
        self.cut_branches: int = 0
        self.last_watering: dt.datetime = dt.datetime(1970, 1, 1, 0, 0, 0)
        self.last_cutting: dt.datetime = dt.datetime(1970, 1, 1, 0, 0, 0)

    def check_history(self, first_action_time, second_action_time):
        if first_action_time > second_action_time:
            raise BaseException('Нарушен хронологический порядок.')
        return True

    def add_action_to_journal(self, time, action, robot, branches = 0, water = 0):
        if self.history == [] or self.check_history(self.history[-1].time, time):
            if action == 'cutting':
                if (time - self.last_cutting).days < 7:
                    if self.cut_branches + branches > 8:
                        raise BaseException('На этой неделе нельзя больше обрезать ветви.')
                else:
                    self.cut_branches = 0
                self.cut_branches += branches
                robot.cutting(self.tree, branches)
                self.last_cutting = time
            elif action == 'watering':
                if (time - self.last_watering).days >= 1:
                    self.amount_of_water = 0
                    self.tree.water_amount = 0
                self.amount_of_water += water
                robot.watering(self.tree, water)
                self.last_watering = time
            else:
                raise BaseException('Нет такого действия.')
            self.history.append(Record(time, action, robot))


tree = BinaryTree(1, 12, 0) # дерево с id 1: 12 ветвей, 0 литров воды в горшке
cutting_robot = CuttingRobot(1) # робот с id 1
watering_robot = WateringRobot(1, 10) # робот с id 1 и объёмом 10 литров

journal = Journal(tree)

journal.add_action_to_journal(dt.datetime(2023, 5, 2, 12, 1, 0), 'cutting', cutting_robot, branches=2)
print('action 1 ok')

journal.add_action_to_journal(dt.datetime(2023, 5, 3, 12, 10, 0), 'watering', watering_robot, water=1.5)
print('action 2 ok')

journal.add_action_to_journal(dt.datetime(2023, 5, 3, 12, 15, 0), 'cutting', cutting_robot, branches=6)
print('action 3 ok')

journal.add_action_to_journal(dt.datetime(2023, 5, 4, 12, 16, 0), 'watering', watering_robot, water=0.5)
print('action 4 ok')

journal.add_action_to_journal(dt.datetime(2023, 5, 7, 12, 17, 0), 'watering', watering_robot, water=2)
print('action 5 ok')

journal.add_action_to_journal(dt.datetime(2023, 5, 11, 12, 17, 0), 'cutting', cutting_robot, branches=3)
print('action 6 ok')

print('Количество ветвей в дереве на сейчас: ', tree.branch_amount)
print('Количество воды в горшке с деревом на сейчас: ', tree.water_amount)