




class Person:


    def __init__(self, first_name, last_name):

        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.full_name = f'{self.first_name} {self.last_name}'
        self.energy = 10
        self.money = 10
        self.wisdom = 10

    def work_job(self):
        print(f'{self.full_name} works a day at their job.')
        self.energy -= 1
        self.money += 5

    def sleep(self):
        self.energy = 10

    def __str__(self):
        return f'Name:\t{self.full_name}\nEnergy:\t{self.energy}\nMoney:\t{self.money}\nWisdom:\t{self.wisdom}\n'

    


class Student(Person):

    def __init__(self, first_name, last_name, subject):
        Person.__init__(self, first_name, last_name)
        self.subject = subject

    def learn(self, teacher):
        print(f'{teacher.full_name} is trying to teach {self.full_name}.')
        if not isinstance(teacher, Teacher):
            print(f'This teacher isnt a teacher at all!')
        elif teacher.subject != self.subject:
            print(f'This teacher doesnt teach the students subject!')
        else:
            teacher.work_job()
            print(f'Wow, {self.subject} is very interesting!')
            self.wisdom +=1
            self.energy -=1




class Teacher(Person):

    def __init__(self, first_name, last_name, subject):
        Person.__init__(self, first_name, last_name)
        self.subject = subject




if __name__ == '__main__':

    s1 = Student('alice', 'aaa', 'python')

    t1 = Teacher('patrick', 'adams', 'python')


    print(s1)

    s1.work_job()

    print(s1)

    s1.learn(t1)







