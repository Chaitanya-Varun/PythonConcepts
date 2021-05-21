import multiprocessing
from multiprocessing import Pool
import time
# def spawn(num):
# 	print('Spawned!{}'.format(num))

# if __name__ == '__main__':
# 	s1 = time.time()
# 	for i in range(500):
# 		p = multiprocessing.Process(target=spawn,args=(i,))
# 		p.start()
# 		#p.join()
# 	e1 = time.time()
# 	s2 = time.time()
# 	for i in range(500):
# 		p = multiprocessing.Process(target=spawn,args=(i,))
# 		p.start()
# 		p.join()
# 	e2 = time.time()

# print(e1-s1,e2-s2)

def  job(num):
	return(2*num)

if __name__=='__main__':
	p = Pool(processes=20)
	data = p.map(job,range(20))
	p.close()
	print(data)

#use map to retrive data from the proceses