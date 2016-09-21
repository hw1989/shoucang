#数字集合
number=['0','1','2','3','4','5','6','7','8','9']
#小写字母集合
smallchar=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#大写字母集合
bigchar=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#常见字符集合
commonchar=['+','-','*','/','<','>','?','=']
#非常见字符集合
uncommonchar=['~','`','!','@','#','$','%','^','&','(',')','|','[',']','{','}',';',':','',',','.']

#allchar=[number,smallchar,bigchar,commonchar,uncommonchar]

#对密码组合拼接
def creatList(* strList):
    s=[]
    for arr in strList:
        s+=arr
    return s
#创建密码
maxSize=0
filename=0
strCode=''
def createPsw(leng,chars,strpsw):
    global maxSize
    global filename
    global strCode
    for s in chars:
        if leng>1:
            createPsw(leng-1,chars,strpsw+s)
        else:
            maxSize+=1
            #每10000000条一个文件
            if maxSize==20000000:
                filename+=1
                maxSize=0
            strCode+=(strpsw+s+'\n')
            #每chars的一个长度写一次，防止频繁写
            if maxSize%len(chars)==0:
                with open('dic_'+str(filename)+'.txt','a',encoding='gbk') as fopen:
                    fopen.write(strCode)
                strCode=''
arr=creatList(number,smallchar)
createPsw(6,arr,'')

       

            

    
    
    
        



