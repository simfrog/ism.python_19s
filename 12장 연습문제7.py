while True:
    try:
        fname=input("입력  파일 이름:")
        infile=open(fname,"r")
        break
    except IOError:
        print("파일"+fname+"이 없습니다. 다시 입력하시오")
print("파일이 성공적으로 열렸습니다.")

