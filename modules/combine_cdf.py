import cdflib
import numpy as np



def merge_cdf(cdf1,cdf2,cdf3):
    t1 = cdf1.varget('epoch')
    t2 = cdf2.varget('epoch')
    t3 = cdf3.varget('epoch')

    #BX,BY,BZ

    BX1 = cdf1.varget('BX')
    BX2 = cdf2.varget('BX')
    BX3 = cdf3.varget('BX')

    BY1 = cdf1.varget('BY')
    BY2 = cdf2.varget('BY')
    BY3 = cdf3.varget('BY')


    BZ1 = cdf1.varget('BZ')
    BZ2 = cdf2.varget('BZ')
    BZ3 = cdf3.varget('BZ')


    #Proton_Vp_moment Proton_VX_moment
    VX1 = cdf1.varget('Proton_VX_moment')
    VX2 = cdf2.varget('Proton_VX_moment')
    VX3 = cdf3.varget('Proton_VX_moment')

    VY1 = cdf1.varget('Proton_VY_moment')
    VY2 = cdf2.varget('Proton_VY_moment')
    VY3 = cdf3.varget('Proton_VY_moment')

    VZ1 = cdf1.varget('Proton_VZ_moment')
    VZ2 = cdf2.varget('Proton_VZ_moment')
    VZ3 = cdf3.varget('Proton_VZ_moment')


    #Proton_Np_moment
    NP1 = cdf1.varget('Proton_Np_moment')
    NP2 = cdf2.varget('Proton_Np_moment')
    NP3 = cdf3.varget('Proton_Np_moment')


    #Proton_W_moment
    pw1 = cdf1.varget('Proton_W_moment')
    pw2 = cdf2.varget('Proton_W_moment')
    pw3 = cdf3.varget('Proton_W_moment')

    #combining
    m_bx = np.concatenate((BX1, BX2, BX3))
    m_by = np.concatenate((BY1,BY2,BY3))
    m_bz = np.concatenate((BZ1,BZ2,BZ3))

    m_vpx = np.concatenate((VX1,VX2,VX3))
    m_vpy = np.concatenate((VY1,VY2,VY3))
    m_vpz = np.concatenate((VZ1,VZ2,VZ3))

    m_np = np.concatenate((NP1,NP2,NP3))

    m_pw = np.concatenate((pw1,pw2,pw3))

    m_t = np.concatenate((t1,t2,t3))




    dataset = {"Epoch":m_t,
               "BX":m_bx,
               "BY":m_by,
               "BZ":m_bz,
               "Proton_VX_moment":m_vpx,
               "Proton_VY_moment":m_vpy,
               "Proton_VZ_moment":m_vpz,
               "Proton_Np_moment":m_np,
               "Proton_W_moment":m_pw
               }
    
    return dataset