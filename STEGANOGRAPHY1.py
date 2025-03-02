import cv2
import os
import string
a=cv2.imread("D:/CYBER SECURITY INTERNSHIP AICTE/INTERNSHIP/ENCRYPTION/PICTURE1.jpg")
b=a
c=input("Enter the secret message to be encrypted and hidden within the image: \n")
d=input("Enter the password to protect the message hidden within the image: \n")
e=[""]*len(c)
for g in range(len(c)):
    e[g]=str(bin(ord(c[g])))
i=j=k=0
for g in range(len(c)):
    for h in range(8):
        if(e[g]==0):
            if((b[i][j][k])%2!=0):
                b[i][j][k]=b[i][j][k]-1
        if(e[g]==1):
            if((b[i][j][k])%2==0):
                b[i][j][k]=b[i][j][k]-1
i=j=k=0
cv2.imwrite("NEWPICTURE1.jpg",b)
os.system("Start NEWPICTURE1.jpg")
f=[""]*len(c)
l=""
for g in range(len(c)):
    for h in range(8):
        if((b[i][j][k]%2)==0):
            f[g]+="0"
        if((b[i][j][k]%2)!=0):
            f[g]+="1"
    l+=chr((int((f[g]),2)))
    h=1
m=input("Enter the password to protect the message hidden within the image: \n")
if(m==d):
    print("The secret message to be hidden within the image: \n",c)
else:
    print("The password is incorrect. The message hidden within the image cannot be decrypted and displayed.")
