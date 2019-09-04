import os.path

if os.path.isfile("todo.txt"):
    print('동일한 이름의 파일이 이미 존재합니다.')
else:
    outfile=open('todo.txt','w')
    outfile.write('파이썬 프로그래밍\n')
    outfile.write('자료구조\n')
    outfile.write('네트워크 프로그래밍\n')