from numpy import save

def DT5742_read(path, file_name, rlength, records, avg_length):
    n1 = np.zeros((records, rlength))
    wdir = os.path.join(path,file_name)
    with open(wdir, 'rb') as f:
        ct = 0 
        while(1):
            b = np.fromfile(f, dtype=np.int32, count=6)
    #        print('file header=',b)
            b1 = np.fromfile(f, dtype=np.float32, count=1024)
            n1[ct] = b1[15:1015] - np.mean(b1[15:1015]) 
    #        print('file header=',b)
            ct = ct + 1
            if ct > records-1:
                f.close()
                break 
    return n1

path = r'\Users\mmishra\OneDrive - North Carolina State University\drs4_multiplexerr\8to1mult\dt5742'
folders = ['50MHz', '55MHz', '60MHz', '65MHz', '70MHz', '75MHz', '80MHz', '85MHz']
files = ['wave_0.dat', 'wave_2.dat']
