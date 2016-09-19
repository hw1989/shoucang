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
psw=''
def createPsw(len,chars,fopen):
    global psw
    for s in chars:
        psw+=s
        if len>0:
            createPsw(len-1,chars,fopen)
        else:
            fopen.write(psw+'\n')
            psw=''


with open('dic_len8_10_num_char.txt','w',encoding='gbk') as fopen:
    arr=creatList(number)
    createPsw(6,arr,fopen)

       

            

    
    
    
        



