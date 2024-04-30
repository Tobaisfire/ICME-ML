import numpy as np


def repair_nan(time_range):
    start_index = 0
    current_date = time_range[0].astype('datetime64[D]')
    date_ranges = {}

    # Iterate over the datetime array to find the start and end indices of each date
    for i, dt in enumerate(time_range):
        if dt.astype('datetime64[D]') != current_date:
            end_index = i - 1
            date_ranges[current_date.astype('str')] = {'start_index': start_index, 'end_index': end_index}
            start_index = i
            current_date = dt.astype('datetime64[D]')

    # Add the start and end indices of the last date to the dictionary
    end_index = len(time_range) - 1
    date_ranges[current_date.astype('str')] = {'start_index': start_index, 'end_index': end_index}
    
    return date_ranges


def repair_nan_dummyinfo(cdf,time_range):
    nana_dic = repair_nan(time_range)
    k=''
    for key,data in nana_dic.items():
        if np.isnan(cdf['BX'][data['start_index']]):
            print(key,data)
            k = str(key)

    st,ed =nana_dic[k]['start_index'],nana_dic[k]['end_index']
    nan_values = np.full(len(cdf['BX'][st:ed+1]), np.nan)
    return st,ed,nan_values


def repair_full(cdf,time_range,BX,BY,BZ,b_mag,p_density,vp,temp,p_beta,tehta_angle,phi_angle):
    st,ed,nan_values = repair_nan_dummyinfo(cdf,time_range)

    BX[st:ed+1],BY[st:ed+1],BZ[st:ed+1],b_mag[st:ed+1]=nan_values,nan_values,nan_values,nan_values
    p_density[st:ed+1]=nan_values
    vp[st:ed+1]=nan_values
    temp[st:ed+1]=nan_values
    p_beta[st:ed+1]=nan_values
    tehta_angle[st:ed+1],phi_angle[st:ed+1]=nan_values,nan_values

    return BX,BY,BZ,b_mag,p_density,vp,temp,p_beta,tehta_angle,phi_angle