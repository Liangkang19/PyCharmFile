#f1 = open('BEYOND海阔天空.mp3')
#for each_line in f1:
#    print(each_line,end = '')
#f1.close()

fx = open('C:\\Users\\57307\\Desktop\\DPON\\BEYOND海阔天空.mp3')
fy = open('C:\\Users\\57307\\Desktop\\DPON\\BEYOND海阔天空.txt','x')
fy.write(fx.read())
fy.close()
fx.close()
