# my_list = [-5056798,2,3,4,5,56,67,78,8,9,90,2,4,23,565,756,6324,6,679,876,34,32]
# iterator = iter(my_list)
# print(iterator)
# try:
#     while True:
#         print(next(iterator))
# except StopIteration:
#     print("всьо харе список закінчився")

class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i

count = Counter(5)
for elem in count:
    print(elem)