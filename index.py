class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
  
    def introduce(self):
        print(f"My name is {self.name}", f"I am {self.age} years old", f"I am a {self.gender}")

Person_instance = Person(name =  'lara', age = 18, gender = 'female')

Person_instance.introduce()