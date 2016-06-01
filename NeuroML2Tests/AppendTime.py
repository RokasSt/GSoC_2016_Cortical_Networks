import numpy as np

time_array=np.loadtxt("time.dat")

voltage_array=np.loadtxt("CGnRT_0_FigA8_500.dat")

if len(time_array)==len(voltage_array):

   voltage_with_time=np.zeros([len(time_array),2])

   for i in range(0,len(time_array)):
       voltage_with_time[i,0]=time_array[i]/1000
       voltage_with_time[i,1]=voltage_array[i]/1000
  
   np.savetxt("CGnRT_0_FigA8_500_wtime.dat",voltage_with_time)

       

if __name__=="__main__":

   print time_array
   print voltage_array
   print len(time_array)
   print len(voltage_array)
