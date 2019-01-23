# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class Worker:

    def __init__(self, s):
        name, surname, salary, position, norm = s.split()
        self.fullname = name + ' ' + surname
        self.salary = float(salary)
        self.position = position
        self.norm = float(norm)

    def calc_salary(self):
        hours = work_hours.get(self.fullname, None)
        if hours is None:
            return None
        if hours >= self.norm:
            real_salary = self.salary * (1  +
                          2 * (hours / self.norm  - 1))
        else:
            real_salary = self.salary * (hours / self.norm)
        return round(real_salary, 2)

if __name__ == '__main__':

    # read data
    with open('data/workers', 'r') as f:
        s_list = f.readlines()

    with open('data/hours_of', 'r') as f:
        h_list = f.readlines()

    # prepare structures
    def parse(x):
        name, surname, hours = x.split()
        return name + ' ' + surname, float(hours)

    workers = list(map(Worker, s_list[1:]))
    work_hours = {i: j for i, j in 
                    map(parse, h_list[1:])}
            

    # calculate real salaries
    real_salaries = {worker.fullname: worker.calc_salary() 
            for worker in workers}

    print('REAL SALARIES: ')
    print(real_salaries)

