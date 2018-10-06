import serial
import time
tflag=1
rflag=1
p='ppsc.txt'
obc=serial.Serial('COM20',9600)
time.sleep(2)
zda_flag=0
gga_flag=0
gll_flag=0
rmc_flag=0
gsa_flag=0
gsv_flag=0
vtg_flag=0
rsm_flag=1
all_flag=0
conf_count=0
conf=[0,1,2,3,4,5,6,7,8,9,10,11]
start=time.time()
while True:
    while True :
        ntime=time.time()
        if obc.in_waiting:
            conf_edit=obc.readline(1)
            conf_num=int.from_bytes(conf_edit,'big')
            conf[conf_count]=conf_num
            print('conf[',conf_count,']',hex(conf[conf_count]))
            conf_count=conf_count+1
            if (conf[conf_count - 2]==0x3f and conf[conf_count - 1]==0x3f):
                conf[0]=0x3f
                conf[1]=0x3f
                conf_count=2
                print('\n\nconf_count=2\n\n')
            elif (conf[conf_count - 2]==0x0d and conf[conf_count - 1]==0x0a):
                conf_count=0
                
                print('\n\nconf_count=0\n\n')
            elif( conf_count>11):
                conf_count=0
                print('\n\nconf_count=00\n\n')
        if (ntime-start)>=1:
            break
    start=time.time()
    ppsf=open(p)
    ppsd=ppsf.read()
    ppsf.close()
    #asc=ppsd.encode('ascii')
    #if asc==b'ready':
    if ppsd==u'ready':
        ppsf=open(p,'w')
        ppsf.write(u'start')
        ppsf.close()
        print('start pps')
        #read rsm file
        rsmf=open('gps_rsm.txt')
        rsmd=rsmf.read()
        rsmd1=rsmd.encode('ascii')
        rsmf.close()
        #read gga file
        ggaf=open('gps_gga.txt')
        ggad=ggaf.read()
        ggad1=ggad.encode('ascii')
        ggaf.close()
        #read gll file
        gllf=open('gps_gll.txt')
        glld=gllf.read()
        glld1=glld.encode('ascii')
        gllf.close()
        #read zda
        zdaf=open('gps_zda.txt')
        zdad=zdaf.read()
        zdad1=zdad.encode('ascii')
        zdaf.close()
        #read rmc
        rmcf=open('gps_rmc.txt')
        rmcd=rmcf.read()
        rmcd1=rmcd.encode('ascii')
        rmcf.close()
        #read gsa file
        gsaf=open('gps_gsa.txt')
        gsad=gsaf.read()
        gsad1=gsad.encode('ascii')
        gsaf.close()
        #read gsv file
        gsvf=open('gps_gsv.txt')
        gsvd=gsvf.read()
        gsvd1=gsvd.encode('ascii')
        gsvf.close()
        #read vtg file
        vtgf=open('gps_vtg.txt')
        vtgd=vtgf.read()
        vtgd1=vtgd.encode('ascii')
        vtgf.close()
        
        if(conf[0]==0x3f and conf[1]==0x3f and conf[2]==0x0A and conf[3]==0x0C and conf[4]==0xA2 and conf[5]==0xB0  and conf[8]==0x0D and conf[9]==0x0A):
            print('\n\ncommand testing part 1\n\n')
            if(conf[6]==0x01):
                print('\n\ncommand=3\n\n')
                start=time.time()
                conf=[0,1,2,3,4,5,6,7,8,9,10,11]
                while True :
                    ntime=time.time()
                    if(ntime-start)>=3:
                        start=time.time()
                        break
            elif(conf[6]==0x00):
                print('\n\ncommand=2\n\n')
                zda_flag=0
                gga_flag=0
                gll_flag=0
                rmc_flag=0
                gsa_flag=0
                gsv_flag=0
                vtg_flag=0
                rsm_flag=1
                all_flag=0
                conf=[0,1,2,3,4,5,6,7,8,9,10,11]
        
        if(conf[0]==0x3f and conf[1]==0x3f and conf[2]==0x0A and conf[3]==0x0C and conf[4]==0xA2 and conf[5]==0xEA  and conf[10]==0x0D and conf[11]==0x0A):
            print('\n\ncommand testing part 2\n\n')
            if(conf[6]==0xCF):
                print('\n\ncommand=5\n\n')
                if(conf[7]==0x00):
                    print('\n\ncommand=50\n\n')
                    if(conf[8]==0x00):
                        zda_flag=0
                    elif(conf[8]==0x01):
                        zda_flag=1 
                elif(conf[7]==0x01):
                    print('\n\ncommand=51\n\n')
                    if(conf[8]==0x00):    
                        gga_flag=0
                    elif(conf[8]==0x01):
                        gga_flag=1
                elif(conf[7]==0x02):
                     if(conf[8]==0x00):
                        gll_flag=0
                     elif(conf[8]==0x01):
                        gll_flag=1
                elif(conf[7]==0x03):
                     if(conf[8]==0x00):
                        rmc_flag=0
                     elif(conf[8]==0x01):
                        rmc_flag=1
                elif(conf[7]==0x04):
                     if(conf[8]==0x00):
                        gsa_flag=0
                     elif(conf[8]==0x01):
                        gsa_flag=1
                elif(conf[7]==0x05):
                     if(conf[8]==0x00):
                        gsv_flag=0
                     elif(conf[8]==0x01):
                        gsv_flag=1
                elif(conf[7]==0x06):
                     if(conf[8]==0x00):
                        vtg_flag=0
                     elif(conf[8]==0x01):
                        vtg_flag=1
                elif(conf[7]==0x07):
                     if(conf[8]==0x00):
                        rsm_flag=0
                     elif(conf[8]==0x01):
                        rsm_flag=1
                elif(conf[7]==0x08):
                    print('\n\ncommand=58\n\n')
                    if(conf[8]==0x00):
                        zda_flag=0
                        gga_flag=0
                        gll_flag=0
                        rmc_flag=0
                        gsa_flag=0
                        gsv_flag=0
                        vtg_flag=0
                        rsm_flag=0
                    elif(conf[8]==0x01):
                        zda_flag=1
                        gga_flag=1
                        gll_flag=1
                        rmc_flag=1
                        gsa_flag=1
                        gsv_flag=1
                        vtg_flag=1
                        rsm_flag=1
                conf=[0,1,2,3,4,5,6,7,8,9,10,11]
        print('send data')
        print(time.time())
        while (time.time()-start)<=0.28 :
            gar=1
        
        print('sending data')
        if rsm_flag==1:
            No=obc.write(rsmd1)
            print('rsm',rsmd)
        if zda_flag==1:
            No=obc.write(zdad1)
            print('zda',zdad)
        if gga_flag==1:
            No=obc.write(ggad1)
            print('gga',ggad)
        if gll_flag==1:
            No=obc.write(glld1)
            print('gll',glld)
        if rmc_flag==1:
            No=obc.write(rmcd1)
            print('rmc',rmcd)
        if gsa_flag==1:
            No=obc.write(gsad1)
            print('gsa',gsad)
        if gsv_flag==1:
            No=obc.write(gsvd1)
            print('gsv',gsvd)
        if vtg_flag==1:
            No=obc.write(vtgd1)
            print('vtg',vtgd)
          
    else:
        print('pps not ready')
