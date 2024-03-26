import os
import argparse
#path = input('请输入文件路径(结尾加上/)：')

# 获取该目录下所有文件，存入列表中

if __name__=="__main__":
    parser=argparse.ArgumentParser(
    description="Run this renamefile for oldfile to add num_id")
    parser.add_argument('-n','--sum',type=int,default=0,help='give a sum num for previous files')
    parser.add_argument('-p', '--path', type=str, default='./', help='give a path for previous files')
    args=parser.parse_args()
    sum=args.sum+1
    path =args.path
    fileList = os.listdir(path)

    for file in fileList:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + os.sep + file  # os.sep添加系统分隔符
        # 设置新文件名
        s=file.split('-')[0]
        s1='{:09d}'.format(int(s[-3:])+sum)
        newname = path + os.sep + file.replace(s,s1)

        os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
        print(oldname, '======>', newname)

