
number=['0','1','2','3','4','5','6','7','8','9']

smallchar=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

bigchar=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

commonchar=['+','-','*','/','<','>','?','=']

uncommonchar=['~','`','!','@','#','$','%','^','&','(',')','|','[',']','{','}',';',':','',',','.']




def creatList(* strList):
    s=[]
    for arr in strList:
        s+=arr
    return s

def createPsw(leng,chars,fopen,strpsw):
    for s in chars:
        if leng>0:
            createPsw(leng-1,chars,fopen,strpsw+s)
        else:
            fopen.write(strpsw+s+'\n')


with open('dic_len8_10_num_char.txt','w') as fopen:
    arr=creatList(number)
    createPsw(6,arr,fopen,'')

       

            

    
    
    
        



