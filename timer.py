import time
#print(dir(time))
seconds = input("Enter time in seconds")

def countdown(seconds):
  while seconds > 0 : 
    minutes = int(seconds/60)
    sec = int(seconds % 60)
    print(f"{minutes} : {sec}") 
    time.sleep(1)
    seconds -=1
  print("time up!")
countdown(int(seconds))
