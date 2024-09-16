class person:
 def set(self,name,age):
     self.name=name
     self.age=age
 def output(self):
    print(self.name,self.age)
 p=person()
 skaitlis=int(input('Ivadiet cilveku skaitu:'))
 for i in range(skaits):
    name=input('Ivadiet vecumu:')
    age=int(input('Ivadiet vecumu:'))
    person.set(p,name,age)
    person.output(p)