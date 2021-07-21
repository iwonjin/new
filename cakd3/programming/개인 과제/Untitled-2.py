def read_memberinfo():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    memberinfo = pd.read_csv('성도정보.csv', encoding='ANSI' )
    return memberinfo

def read_attendinfo():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt    
    attendinfo = pd.read_csv('출석정보.csv', encoding='ANSI' )
    return attendinfo
######################################################################
#######################################################################3
########################################################################


r1 = read_memberinfo()
print (r1)

r2 = read_attendinfo()
print (r2)


