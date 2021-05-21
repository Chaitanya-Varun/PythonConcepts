#For measuring time once 
# import time
# start = time.time()
# end =time.time()
# net_time = start-time;

#for getting accurate measurement for a particular snippet of code
import timeit
# print(timeit.timeit('1+3', number=500000))
print(timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = list(i for i in input_list if div_by_two(i))''',number=50000))
print(timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = [i for i in input_list if div_by_two(i)]''',number=50000))