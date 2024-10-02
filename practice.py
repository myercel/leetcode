# example selection sort
def sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        tmp = lst[i]
        lst[i] = lst[min]
        lst[min] = tmp
    
# example binary search
def search(lst, num):
    # lst must be sorted!
    l = 0
    r = len(lst)-1

    while l <= r:
        mid = (r + l) // 2
        if lst[mid] == num:
            return mid  #found the index of target
        if lst[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
        
    return -1 # indicating the value was not found in lst

class City:
    def __init__(self, name):
        self.cityName = name
        self.numRecords = 0
        self.sumSalaries = 0
        self.avgSalary = 0

    def updateSalary(self, salary):
        self.sumSalaries += salary
        self.numRecords += 1
    
    def calculateAvg(self):
        self.avgSalary = self.sumSalaries // self.numRecords

def main():
    
    ### SORTING AND SEARCHING ###
    # lst = [4, 3, 6, 7, 1, 9, 2]

    # print(lst)
    # sort(lst)
    # print(lst)

    # index = search(lst, 7)
    # print(index)
    # assert index == 5

    ### AVG SALARY PRACTICE
    lst = [["a", 30], ["b", 25], ["a", 15], ["c", 50], ["b", 5]]
    cities = {}

    for c, s in lst:
        if c not in cities:
            cities[c] = City(c)
        
        cities[c].updateSalary(s)
        cities[c].calculateAvg()
    
    for c in cities:
        print(c, cities[c].avgSalary)

main()