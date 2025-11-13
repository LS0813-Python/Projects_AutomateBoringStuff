def tablePrinter(lstDouble) :
    maxLen = 0
    nCount = len(lstDouble[0])
    for itemList in lstDouble :
        if nCount != len(itemList) :
            nCount = 0
            break
        for item in itemList :
            if maxLen < len(item) :
                maxLen = len(item)

    maxLen +=  1
    for i in range(nCount) :
        strLine = ''
        for j in range(len(lstDouble)) :
            strLine = strLine + lstDouble[j][i].rjust(maxLen)
        print(strLine)

strInput = input()
num = 0
totalList = []
while strInput != '':
    strList = strInput.split()
    totalList.append(strList)
    num = num + 1
    strInput = input()

tablePrinter(totalList)