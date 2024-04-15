import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

class Plotting:

    def __init__(self):
        pass

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
        
  
        fig,ax = plt.subplots(8, 1,sharex=True, figsize=(15, 15))

        # Set x-axis ticks to show intervals of 6 hours
        hours = mdates.HourLocator(interval=8)
        h_fmt = mdates.DateFormatter('%d-%m-%Y %H:%M')  # Hour and minute format

        plt.gca().xaxis.set_major_locator(hours)
        plt.gca().xaxis.set_major_formatter(h_fmt)

        plt.xlim(time_range[0], time_range[-1])
        plt.xticks(rotation=45)     

        #plotting of BMAG
        # ax[0].set_ylim(min(b_mag),max(b_mag))
        # ax[0].set_yticks(np.arange(0, 51, 20))
        ax[0].set_ylabel(r'$B_{mag} (nT)$')
        ax[0].plot(time_range,B_magnitude,color='black')
        ax[0].grid(True)



        #Plotting for BX,BY,BZ
        ax[1].set_ylabel(r'$B_{vec} (nT)$')
        # ax[1].tick_params(axis='x',)
        ax[1].plot(time_range,Bx,label ='BX',color='blue')
        ax[1].plot(time_range,By,label ='BY',color='green')
        ax[1].plot(time_range,Bz,label ='BZ',color='red')
        ax[1].legend(loc="upper left",bbox_to_anchor=(1, 1))

        ax[1].grid(True)



        #Tetha angle
        ax[2].set_ylabel(r'$ θ $')
        ax[2].plot(time_range,teta_angle,color='black')
        ax[2].grid(True)




        #Phi angle

        ax[3].set_ylabel(r'$ φ $',color='red')
    
        ax[3].plot(time_range,phi_angle,color='red')
        
        ax[3].grid(True)



        #plotting vp -> pvec

        ax[4].set_ylabel(r'$V_{p} (km/s)$')
        ax[4].plot(time_range,Vp_pvec,color='black')
        ax[4].grid(True)



        #Plotting for Np -> Proton density

        ax[5].set_ylabel(r'$N_{p} (cm^{3})$',color='blue')
        ax[5].plot(time_range,Np_pdensity,color='blue')
        ax[5].grid(True)





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

        y_min, y_max = np.min(Temperature), np.max(Temperature)

        y_min_order = int(np.floor(np.log10(y_min)))
        y_max_order = int(np.ceil(np.log10(y_max)))

        # Set y-axis limits to span the range of orders of magnitude
        ax[6].set_ylim(10**y_min_order, 10**y_max_order)
        ax[6].plot(time_range,Temperature,color='purple')
        ax[6].set_ylabel(r'$Temp (K)$',color='purple')
        ax[6].grid(True)


        #beta plasma
        ax[7].set_yscale('log')
        ax[7].plot(time_range,Plasma_beta,color='black')
        ax[7].set_ylabel(r'$beta (β)$')
        # ax[7].set_xlabel('Time (in UT, November,2003)')


        ax[7].grid(True)

        

        





