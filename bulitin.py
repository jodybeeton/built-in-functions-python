#My short and sweet solutions
#Exercise 1
#declare a list of filtering
grades = [20, 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]
grades = list(filter(lambda x : x >=70, grades))
print(grades)

#Exercise 2
#converting ages into dog years
dog_ages = [12, 8, 4, 1, 2, 6, 4, 4, 5]
dog_ages =  list(map(lambda x : x * 7, dog_ages))
print(dog_ages)

#Exercise 3
#converting transactions into a single total

transactions = [51.0, 49.99, 80.99, 67.99, 120.52, 23.49]
transactions = [round(x) for x in transactions]
print(transactions)
