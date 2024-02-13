import time
def something_print(num):
   start_time = time.time()
   for i in range(num):
      print(i)
   end_time = time.time()
   time_difference = (str(end_time - start_time))
   print(time_difference)
      
something_print(100)
