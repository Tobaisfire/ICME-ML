import numpy as np
import pandas as pd


 # Bmagnitude #nT is Ok


def thresold(var : np.array,th : int) -> np.array:

    """
    thresold function to take Parameters of SWE H1 \
    and remove values more than thresold value.  \
    using interpolate.
  
    var -> parameters of SWE.

    th -> thresold value.
    """
    var_rm_out = []


    if len(var[var > th]) >= 1:

        var[var > th] = np.nan
        var_rm_out = pd.Series(var).interpolate().values

    else:
        var_rm_out = var
      

    return var_rm_out


def bmagnitude(cdf_var : np.array) -> tuple: 

    """
    Function to calculate Bmagnitude using \
    [BX,BY,BZ]

    cdf_var -> cdf file

    """ 


    X = thresold(cdf_var['BX'],1000)
    Y = thresold(cdf_var['BY'],1000)
    Z = thresold(cdf_var['BZ'],1000)
    bmag = np.sqrt( X**2 + Y**2 + Z**2 )
    bmag = thresold(bmag,1000)


    return X,Y,Z,bmag


#Vp calculations
def Vp_vec(cdf_var : np.array) -> np.array:   #Vp calculations

    """
    Function to calculate Vp which is velocity using \
    [VX,VY,VZ]

    cdf_var -> cdf file
    """ 

    
    vX = thresold(cdf_var['Proton_VX_moment'],1e4)
    vY = thresold(cdf_var['Proton_VY_moment'],1e4)
    vZ = thresold(cdf_var['Proton_VZ_moment'],1e4)
    vp_vec = np.sqrt( vX**2 + vY**2 + vZ**2 )
    vp_vec = thresold(vp_vec,1e4)

    return vp_vec


#Temp Calculations
def Temperature(cdf_var : np.array) -> np.array:

    """
    Calculating Temp ---> Temp = mass of proton * (Vp**2) / 3 * Boltzman constant

    """

  

    p_wpar = cdf_var['Proton_W_moment']
    m_proton = 1.67e-27     # Mass of proton in kg
    k_boltzmann = 1.38e-23  # Boltzman constant
    vth_ms = p_wpar * 1000 # to make it m/s
    T = (m_proton * (vth_ms**2)) / (3 * k_boltzmann)
    Temp = thresold(T,1e7)

    return Temp


#plasma Beta calculations
def plasma_beta(n_p : np.array,Bmag: np.array ,T: np.array) -> np.array:  

    """
    Calculating plasma_Beta --->  = (Np * Boltzman constant * Temp) / ( Bmag**2 / 2*mu (Vacuum permeability))

    """
    

    k_boltzmann = 1.380649e-23                      # Boltzmann constant 
    mu_0 = 4 * np.pi * 1e-7                         # Vacuum permeability in T m A^-1
    n_p = n_p * 1e6                                 # Proton number density in m^-3 (example value)
                                                    # Plasma temperature in Kelvin (example value)
    # Magnetic field strength in nanoTesla (example value)
    B = Bmag * 1e-9            # Conversion from nanoTesla to Tesla
    # Calculate plasma beta
    p_beta = (n_p * k_boltzmann * T) / (B**2 / (2 * mu_0))

    return p_beta



#calculating angles ->
def angels(bx:np.array,by:np.array,bz:np.array,bmag:np.array):


    angle_rad1 = np.arctan2(-by,-bx)        # arctan if need range 90
    angle_deg1 = np.degrees(angle_rad1)
    phi = angle_deg1 + 180
    angle_rad2 = np.arccos(-bz/bmag)
    angle_deg2 = np.degrees(angle_rad2)
    tetha = angle_deg2 - 90

    return tetha,phi
