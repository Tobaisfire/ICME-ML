import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

class Plotting:

    def __init__(self,title):
        self.title = title
    

    def ipplot(self,
               time_range : np.array ,
               B_magnitude :np.array,
               Bx:np.array,
               By:np.array,
               Bz:np.array,
               teta_angle:np.array,
               phi_angle:np.array,
               Vp_pvec:np.array,
               Np_pdensity:np.array,
               Temperature:np.array,
               Plasma_beta:np.array
               ):
        
  
        fig,ax = plt.subplots(8, 1,sharex=True, figsize=(15, 25))

        # Set x-axis ticks to show intervals of 6 hours
        hours = mdates.HourLocator(interval=8)
        h_fmt = mdates.DateFormatter('%d-%m-%Y %H:%M')  # Hour and minute format

        plt.gca().xaxis.set_major_locator(hours)
        plt.gca().xaxis.set_major_formatter(h_fmt)

        plt.xlim(time_range[0], time_range[-1])
        plt.xticks(rotation=45)  
          
        ax[0].set_title(self.title) 

        #plotting of BMAG
        ax[0].set_ylim(0,51)
        # ax[0].set_yticks(np.arange(0, 51, 20))
        ax[0].set_ylabel(r'$B_{mag} (nT)$')
        ax[0].plot(time_range,B_magnitude,color='black')
        ax[0].grid(True, axis='y')
    


        #Plotting for BX,BY,BZ
        ax[1].set_ylim(-30,31)
        ax[1].set_ylabel(r'$B_{vec} (nT)$')
        # ax[1].tick_params(axis='x',)
        ax[1].plot(time_range,Bx,label ='BX',color='blue')
        ax[1].plot(time_range,By,label ='BY',color='green')
        ax[1].plot(time_range,Bz,label ='BZ',color='red')
        ax[1].legend(loc="upper left",bbox_to_anchor=(1, 1))

        ax[1].grid(True, axis='y')
        



        #Tetha angle

        ax[2].set_ylim(-90, 90)
        ax[2].set_yticks(range(-90, 91, 20))
        # ax[2].yaxis.set_major_locator(MultipleLocator(10))
        # ax[2].yaxis.set_major_formatter(FormatStrFormatter('%d'))

        ax[2].set_ylabel(r'$ θ $')
        
        ax[2].plot(time_range,teta_angle,color='black')
        ax[2].grid(True, axis='y')
        



        #Phi angle
        ax[3].set_ylim(0, 360)
        ax[3].set_yticks(range(0, 361, 60))
        ax[3].set_ylabel(r'$ φ $',color='red')
   
        ax[3].plot(time_range,phi_angle,color='red')
        
        ax[3].grid(True, axis='y')
   


        #plotting vp -> pvec
        ax[4].set_ylim(200,1000)
        ax[4].set_ylabel(r'$V_{p} (km/s)$')
        ax[4].plot(time_range,Vp_pvec,color='black')
        ax[4].grid(True, axis='y')
   


        #Plotting for Np -> Proton density
        ax[5].set_ylim(0,70)
        ax[5].set_ylabel(r'$N_{p} (cm^{3})$',color='blue')
        ax[5].plot(time_range,Np_pdensity,color='blue')
        ax[5].grid(True, axis='y')
       




        #Plotting for Temp

        # ax[4].set_yscale('log')
        # def scientific_formatter(x, pos):
        #     if x <= 0:  # Handle zero or negative values
        #         return '0'
        #     else:
        #         return f'$10^{{{int(np.log10(x))}}}$'

        # # Set the y-axis tick formatter
        # ax[4].yaxis.set_major_formatter(FuncFormatter(scientific_formatter))

        ax[6].set_yscale('log')

        y_min_order = 4
        y_max_order = 6

        # Set y-axis limits to span the range of orders of magnitude
      
        ax[6].set_ylim(10**y_min_order, 10**y_max_order)
        ax[6].plot(time_range,Temperature,color='purple')
        ax[6].set_ylabel(r'$Temp (K)$',color='purple')
        ax[6].grid(True, axis='y')
      

        #beta plasma
        ax[7].set_ylim(10**-2,10**2)
        ax[7].set_yscale('log')
        ax[7].axhline(y=1, color='r',linestyle='--')
        ax[7].plot(time_range,Plasma_beta,color='black')
        ax[7].set_ylabel(r'$beta (β)$')
        # ax[7].set_xlabel('Time (in UT, November,2003)')

        
        ax[7].grid(True, axis='y')

    

        






