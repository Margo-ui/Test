class Person:
    def __init__(self, surname, name, patronymic, birthdate, gender):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate
        self.gender = gender

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_patronymic(self):
        return self.patronymic

    def set_patronymic(self, patronymic):
        self.patronymic = patronymic

    def get_birthdate(self):
        return self.birthdate

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def show(self):
        print("Name: ", self.surname, self.name, self.patronymic, "Birth date: ", self.birthdate, "Gender: ", self.gender)


class Worker(Person):
    def __init__(self, surname, name, patronymic, birthdate, gender, organization, speciality, position, salary,
                 experience):
        super().__init__(surname, name, patronymic, birthdate, gender)
        self.organization = organization
        self.speciality = speciality
        self.position = position
        self.salary = salary
        self.experience = experience

    def get_organization(self):
        return self.organization

    def set_organization(self, organization):
        self.organization = organization

    def get_speciality(self):
        return self.speciality

    def set_speciality(self, speciality):
        self.speciality = speciality

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = experience

    def show(self):
        Person.show(self)
        print("Organization: ", self.organization, "Speciality: ", self.speciality, "Position: ", self.position, "Salary: ", self.salary, "Experience: ", self.experience)

class Organization(Worker):
  def __init__(self):
    self.workers = list()
    self.newworkers = list()

  def comp(self, other):
    for worker in self.workers:
      if self.get_experience() > other.experience:
        self.newworkers.append(worker)

  def printt(self):
    for worker in self.newworkers:
      print(worker[0].get_name())
      print(worker[0].experience)

obj1 = Worker("Roger", "Smith", "Alexndrv", "11.10.2001", "Male", "ATB", "Economist", "Cashier", 5200, 2)
obj2 = Worker("Rogerr", "Smithh", "Alexndrv", "11.10.2001", "Male", "ATB", "Economist", "Cashier", 5200, 3)
obj3 = Worker("Roge", "Smit", "Alexndrv", "11.10.2001", "Male", "ATB", "Economist", "Cashier", 5200, 4)
organization = Organization()
organization.workers = (obj1, obj2, obj3)
organization.comp(2)
organization.printt()

