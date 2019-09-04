from tkinter import*

cnt=[0,0,0,0]
window=Tk()
blist=[]
name=['미국:','영국:','프랑스:','일본:']

def cnt_add(i):
    button=blist[i]
    cnt[i]+=1
    button["text"]=name[i]+str(cnt[i])


Label(window, text="가장 여행하고 싶은 나라는?").pack()
for s in range(4):
    b=Button(window,text=name[s]+str(cnt[s]),command=lambda k=s: cnt_add(k))
    b.pack()
    blist.append(b)
window.mainloop()