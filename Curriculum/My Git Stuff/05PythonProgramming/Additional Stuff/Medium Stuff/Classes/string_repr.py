# import datetime

# today = datetime.datetime.now()
# # for the user
# print(str(today))
# # output: 2019-11-12 12:42:53.634735

# # for the developer, repr shows more info about the object 
# print(repr(today))
# # output: datetime.datetime(2019, 11, 12, 12, 42, 53, 634735)

class someClass:
    ex1 = 0
    ex2 = 0

    def f(self, val):
            ex1 = val
            self.ex2 = val
def main():
    someInstance = someClass()
    print("Instance ex1 and 2")
    print(someInstance.ex1)
    print(someInstance.ex2)

    someInstance.f(100)
    print("Instance ex1 and 2 after")
    print(someInstance.ex1)
    print(someInstance.ex2)

    print("And the original")
    print(someClass.ex1)
    print(someClass.ex2)

main()