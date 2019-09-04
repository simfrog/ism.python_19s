infomation=dict()

while True:
    id=input('(save) ID:')
    if id=='':
        break
    pw=input('(save) PW:')
    infomation[id]=pw

while True:
    sid=input('ID:')
    print(infomation.get(sid,'없습니다.'))