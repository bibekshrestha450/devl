# class student:
#     def __init__(self,name):
#         self.name=name
#         print('i am {name}')

#     def __del__(self):
#         print("i am student")

# obj=student('ram')
# add,str,rep,


class collage:
    def __init__(self):
        self.student = ['ram', 'sita', 'hari']

    def add(self, new):
        self.student.append(new)
        print(f"{new} added.")

    def show(self):
        print("Students in the collage:")
        for s in self.student:
            print(s)

    def delete(self, name):
        if name in self.student:
            self.student.remove(name)
            print(f"{name} deleted.")
        else:
            print(f"{name} not found.")


    

c = collage()
c.show()

c.add("gita")
c.show()

c.delete('ram')
c.show()