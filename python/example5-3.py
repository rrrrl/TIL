from os import listdir, makedirs
from os.path import isdir
from shutil import copyfile


'''
listdir : 파일 목록 조회
makedirs : 폴더 생성
isdir : 폴더가 이미존재하는지 확인
copyfile : 파일 복사
'''

orig_dir = "/Users/jeonghaeyeon/example/"
out_dir = "/Users/jeonghaeyeon/example2/"

file_list = listdir(orig_dir)
print(file_list)

# 파일명 : TEST_년-월-일_시-분-초.pdf

    
for f_name in file_list:
    f_date = f_name[5:-4]
    print(f_date)
    f_date = f_date.split('_')
    f_date = f_date[0]
    f_date = f_date.split('-')

    year = f_date[0]
    month = f_date[1]
    day = f_date[2]

    target_dir = out_dir + year + "/" + month + "/" + day
    if not isdir(target_dir):
        makedirs(target_dir)

    copyfile(orig_dir + f_name, target_dir + "/" + f_name)
    print(orig_dir + f_name + " => " + target_dir + "/" + f_name)
