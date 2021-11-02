import numpy as np

# function
def define_filt(fx, filt_freq, type_filt):
    
    """
    This is a doc string - implement lp or hp filter
    
    Input Args:
        fx (array, float): list of frequencies, takend from np.fft.rfftfreq
        filt_freq (int): cutoff freq for lp or hp filter
        type_filt (str): lp = low pass, hp = high pass
        
    Returns:
        brick: brick wall filter ... 
    """
    
    cutoff_pnt = np.argmin(np.abs(fx - filt_freq))
    brick = np.zeros(len(fx))
    
    if type_filt == 'lp':
        brick[0:cutoff_pnt] = 1
    elif type_filt == 'hp':
        brick[cutoff_pnt:] = 1
    else:
        print('wrong filter')
        return 0
    
    return brick
        
    
def apply_filt(sig,filt):
    
    """
    docstring - apply the defined filter to the ffted signal
    
    """
    
    fft_sig = np.fft.rfft(sig)
    inverse_sig = np.fft.irfft(fft_sig * filt)
    return inverse_sig
