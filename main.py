import pandas as pd
import numpy as np
import os
from Student import Student

def GetExcelNamesInDir():
    FileNames = []
    dirs = os.listdir('.')                     # 获取指定路径下的文件
    for i in dirs:                             # 循环读取路径下的文件并筛选输出
        if os.path.splitext(i)[1] == ".xls":   # 筛选xls文件
            FileNames.append(i)
            print(i)                           # 输出所有的xls文件
    return FileNames

def ProcessStudentInSingleFile(filename, StudentList):
    data = pd.read_excel(filename, skiprows=2)

    # 严格模式计算
    ScoreIndex = [ i for i in range(1, 18)]
    # 非严格模式
    ScoreSumIndex = ['分值a', '分值c', '分值d', '分值e']
    
    for i in range(len(StudentList)):
        StudentList[i].AddScoreSum2List(
            data[ScoreSumIndex[0]][i], 
            data[ScoreSumIndex[1]][i], 
            data[ScoreSumIndex[2]][i], 
            data[ScoreSumIndex[3]][i]
        )

def main():
    FileNames = GetExcelNamesInDir()
    data = pd.read_excel(FileNames[0], skiprows=2)

    StudentList = []
    StudentIndex = {}
    names = data['姓  名'] 
    
    for i in range(0, len(names)):
        newStudent = Student(names[i])
        StudentIndex[names[i]] = i
        StudentList.append(newStudent)

    for i in FileNames:
        ProcessStudentInSingleFile(i, StudentList)

    ScoreA = []
    ScoreC = []
    ScoreD = []
    ScoreE = []

    for i in StudentList:
        ScoreList = i.GetFinalScore()
        ScoreA.append(ScoreList[0])
        ScoreC.append(ScoreList[1])
        ScoreD.append(ScoreList[2])
        ScoreE.append(ScoreList[3])
    StudentFinalScore = pd.DataFrame({
        '姓名': names,
        '分数a': ScoreA,
        '分数c': ScoreC,
        '分数d': ScoreD,
        '分数e': ScoreE
        })
    StudentFinalScore.to_excel('汇总结果.xlsx', index=False)

if __name__ == "__main__":
    main()