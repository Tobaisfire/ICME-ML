import datetime
import cdflib
import numpy as np

def gen_epochs(year, month, day, interval_seconds):
    start_date = datetime.datetime(year, month, day)
    end_date = datetime.datetime(year, month, day, 23, 59, 59)
    time_ranges = []

    current_date = start_date
    while current_date <= end_date:
        time_ranges.append([current_date.year, current_date.month, current_date.day,
                            current_date.hour, current_date.minute, current_date.second,
                            current_date.microsecond / 1000])
        current_date += datetime.timedelta(seconds=interval_seconds)

    return time_ranges


def get_dummy(day,month,year,path):
    date = datetime.date(year, month, day)
    time_ranges = gen_epochs(date.year, date.month, date.day, 92)
    print(time_ranges[0],time_ranges[len(time_ranges)//2],time_ranges[-1])
    epoch = []
    for time  in time_ranges:
        epoch.append(cdflib.cdfepoch.compute_epoch(time))

    
    z_var1_spec = {
        'Variable': 'epoch',
        'Data_Type': 45,
        'Num_Elements': 1,
        'Rec_Vary': False ,
        'Dim_Sizes':(940,),
        'Var_Type': 'zVariable',  
        'Sparse': 'no_sparse',

    }
    z_var2_spec = {
        'Variable': 'BX',
        'Data_Type': 44,
        'Num_Elements': 1,
        'Rec_Vary': False ,
        'Dim_Sizes':(940,),
        'Var_Type': 'zVariable',  
        'Sparse': 'no_sparse',
    

    }
    z_var3_spec = {
        'Variable': 'BY',
        'Data_Type': 44,
        'Num_Elements': 1,
        'Rec_Vary': False ,
        'Dim_Sizes':(940,),
        'Var_Type': 'zVariable',  
        'Sparse': 'no_sparse',

    }
    z_var4_spec = {
        'Variable': 'BZ',
        'Data_Type': 44,
        'Num_Elements': 1,
        'Rec_Vary': False ,
        'Dim_Sizes':(940,),
        'Var_Type': 'zVariable',  
        'Sparse': 'no_sparse',

    }
    z_var5_spec = {
        'Variable': 'Proton_VX_moment',
        'Data_Type': 44,
        'Num_Elements': 1,
        'Rec_Vary': False ,
        'Dim_Sizes':(940,),
        'Var_Type': 'zVariable',  
        'Sparse': 'no_sparse',
    
    }
    z_var6_spec = {
        'Variable': 'Proton_VY_moment',
        'Data_Type': 44,
        'Num_Elements': 1,
        'Rec_Vary': False ,
        'Dim_Sizes':(940,),
        'Var_Type': 'zVariable',  
        'Sparse': 'no_sparse',
    
    }
    z_var7_spec = {
        'Variable': 'Proton_VZ_moment',
        'Data_Type': 44,
        'Num_Elements': 1,
        'Rec_Vary': False ,
        'Dim_Sizes':(940,),
        'Var_Type': 'zVariable',  
        'Sparse': 'no_sparse',
    
    }
    z_var8_spec = {
        'Variable': 'Proton_Np_moment',
        'Data_Type': 44,
        'Num_Elements': 1,
        'Rec_Vary': False ,
        'Dim_Sizes':(940,),
        'Var_Type': 'zVariable',  
        'Sparse': 'no_sparse',
    
    }
    z_var9_spec = {
        'Variable': 'Proton_W_moment',
        'Data_Type': 44,
        'Num_Elements': 1,
        'Rec_Vary': False ,
        'Dim_Sizes':(940,),
        'Var_Type': 'zVariable',  
        'Sparse': 'no_sparse',
    
    }



    master_zdata =[z_var1_spec,z_var2_spec,z_var3_spec,z_var4_spec,z_var5_spec,z_var6_spec,z_var7_spec,z_var8_spec,z_var9_spec]

    master_zdata
    if len(str(month))<2:
        month = '0'+str(month)

    if len(str(day))<2:
        day = '0'+str(day)  
         
    cd = cdflib.cdfwrite.CDF(f'{path}/wi_h1_swe_{year}{month}{day}_v01.cdf')


    for data in master_zdata:
        if data['Variable'] == 'epoch':
            cd.write_var(data,var_attrs=None, var_data=epoch)
        else:
            cd.write_var(data,var_attrs=None, var_data=np.full((940,), np.nan))


    cd.close()