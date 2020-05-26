import os
import multiprocessing

no_of_cpu = multiprocessing.cpu_count()

def find_cube(num):
	print(os.getpid())
	print("cube: %d" %(num*num*num))

def find_sqr(num):
	print(os.getpid())
	print("square: %d" %(num*num))

p1 = multiprocessing.Process(target = find_cube, args = (12,))
p2 = multiprocessing.Process(target = find_sqr, args = (13,))
p3 = multiprocessing.Process(target = find_cube, args = (11,))
p4 = multiprocessing.Process(target = find_sqr, args = (16,))
p5 = multiprocessing.Process(target = find_cube, args = (15,))
p6 = multiprocessing.Process(target = find_sqr, args = (19,))
p7 = multiprocessing.Process(target = find_cube, args = (10,))
p8 = multiprocessing.Process(target = find_sqr, args = (14,))

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
p8.start()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()
p6.join()
p7.join()
p8.join()

print("Task Complete")