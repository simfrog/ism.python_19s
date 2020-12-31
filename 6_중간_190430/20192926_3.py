nowtime=input("현재시각:")
worktime=int(input("작업시간(분):"))
dtime=int(nowtime[0])*60+int(nowtime[2]+nowtime[3])+worktime
d=dtime//60
d1=dtime%60
print("작업종료시각:%d:%d"%(d,d1))
