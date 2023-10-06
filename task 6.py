#Ans. 1
lst = [30, 75, 9, 97, 50, -4, 70, 59]
print(max(lst))
lst.remove(min(lst))
lst.sort(reverse=True)
print(lst[-1:-5:-1])
#Ans. 2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python", 1]]
count = str(main_lst).count("python")
print(count)
#Ans. 3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
print(my_lst[0].capitalize()+" "+
my_lst[1].capitalize()+" "+
my_lst[2].capitalize()+" "+
my_lst[3].capitalize()+" "+
my_lst[4].capitalize())
#Ans. 4
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
copied_lst = my_lst[:]
print(copied_lst)
#Ans. 5
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2], my_lst[4] = my_lst[4], my_lst[2]
print(my_lst)
#Ans. 6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
result = sum(nums)
print(result)
#Ans. 7
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
new_tuple = tuple1 + (9,)
print(new_tuple)
#Ans. 8
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
result_tuple = tuple1 + (9,) + tuple2
print(result_tuple)

