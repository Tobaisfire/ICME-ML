import numpy as np
import pandas as pd


 # Bmagnitude #nT is Ok
def bmagnitude(cdf_var : np.array) -> tuple:  
    X = cdf_var['BX']
    Y = cdf_var['BY']
    Z = cdf_var['BZ']

    bmag = np.sqrt( X**2 + Y**2 + Z**2 )
    if len(bmag[bmag >= 1000]) >= 1:
        bmag[bmag >= 1000] = np.nan
        bmag = pd.Series(bmag).interpolate().values


    return X,Y,Z,bmag



#Vp calculations
def Vp_vec(cdf_var : np.array) -> np.array:   #Vp calculations
    vX = cdf_var['Proton_VX_moment']
    vY = cdf_var['Proton_VY_moment']
    vZ = cdf_var['Proton_VZ_moment']

    vp_vec = np.sqrt( vX**2 + vY**2 + vZ**2 )
    
    if len(vp_vec[vp_vec >= 1000]) >= 1:
        vp_vec[vp_vec >= 1000] = np.nan
        vp_vec = pd.Series(vp_vec).interpolate().values


    return vp_vec



#Temp Calculations
def Temperature(cdf_var : np.array) -> np.array:   
    p_wpar = cdf_var['Proton_W_moment']

    # p_wpar[p_wpar >= 99999] = np.nan
    # p_wpar_new = pd.Series(p_wpar).interpolate().values

    m_proton = 1.67e-27     # Mass of proton in kg
    k_boltzmann = 1.38e-23  # Boltzman constant
    vth_ms = p_wpar * 1000 # to make it m/s

    T = (m_proton * (vth_ms**2)) / (3 * k_boltzmann)

    return T



#plasma Beta calculations
def plasma_beta(n_p : np.array,Bmag: np.array ,T: np.array) -> np.array:  

    k_boltzmann = 1.380649e-23                      # Boltzmann constant 
    mu_0 = 4 * np.pi * 1e-7                         # Vacuum permeability in T m A^-1
    n_p = n_p * 1e6                                 # Proton number density in m^-3 (example value)
                                                    # Plasma temperature in Kelvin (example value)

    # Magnetic field strength in nanoTesla (example value)

    if len(Bmag[Bmag >= 1000]) >= 1:
        Bmag[Bmag >= 1000] = np.nan
        Bmag = pd.Series(Bmag).interpolate().values

    B = Bmag * 1e-9            # Conversion from nanoTesla to Tesla

    # Calculate plasma beta
    p_beta = (n_p * k_boltzmann * T) / (B**2 / (2 * mu_0))

    return p_beta



#calculating angles ->
def angels(bx:np.array,by:np.array,bz:np.array,bmag:np.array):

    if len(bmag[bmag >= 1000]) >= 1:
        bmag[bmag >= 1000] = np.nan
        bmag = pd.Series(bmag).interpolate().values

    angle_rad1 = np.arctan2(-by,-bx)        # arctan if need range 90
    angle_deg1 = np.degrees(angle_rad1)
    phi = angle_deg1 + 180

    angle_rad2 = np.arccos(-bz/bmag)
    angle_deg2 = np.degrees(angle_rad2)
    tetha = angle_deg2 - 90

    return tetha,phi
