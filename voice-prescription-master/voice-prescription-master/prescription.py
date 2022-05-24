import cv2
import os
from datetime import date
from PIL import Image
today = date.today().strftime("%d/%m/%Y")

black = (1,1,1)
white = (255,255,255)


global addname,addage,addgender,addserial,addsignature,addsymptom,adddiagnosis,addadvice,templete,quantity,medname,af_bf,tim,medpos,qtypos,af_bfpos,timpos
addname = ""
addage = ""
addgender= ""
addserial = ""
addsignature = ""
addsymptom = ""
adddiagnosis = ""
addadvice = ""
templete = ""
medname = []
quantity = []
af_bf = []
tim = []
medpos =[]
qtypos =[]
af_bfpos = []
timpos = []

for i in range(20):
    num = 505+ ((i-1) * 35)
    medpos.append((61,num))
    qtypos.append((350,num))
    af_bfpos.append((430,num))
    timpos.append((500,num))
    medname.append("")
    quantity.append("")
    af_bf.append("")
    tim.append("")

def generate():
    global addname,addage,addgender,addserial,addsignature,addsymptom,adddiagnosis,addadvice,templete,quantity,medname,af_bf,tim,medpos,qtypos,af_bfpos,timpos
    templete = cv2.imread(os.getcwd() + '/templete/prescription-templete.jpg' )
    write(str(addname),(196,290))
    write(str(addage),(514,290),size=0.45)
    write(str(addgender),(134,323))
    write(str(addserial),(310,323),size=0.45)
    write(str(addsignature),(376,782))
    write(str(addsymptom),(160,356))
    write(str(adddiagnosis),(160,389))
    write(str(addadvice),(138,716))
    write(str(today),(485,323),size=0.45)

    for j in range(20):
        write(str(medname[j]),medpos[j] )
        write(str(quantity[j]),qtypos[j],size=0.45)
        write(str(af_bf[j]),af_bfpos[j] )
        write(str(tim[j]),timpos[j])
        j = j+1
def write(text,origin, color=black,size=0.6):
    global templete
    cv2.putText(templete, text , origin ,  cv2.FONT_HERSHEY_DUPLEX, size, color , 1, cv2.LINE_AA)

def name(x):
    global addname
    addname = x
    generate()

def age(x):
    global addage
    addage = x
    generate()

def gender(x):
    global addgender
    addgender = x
    generate()

def serial(x):
    global addserial
    addserial = x
    generate()

def medicine(number,med,qty=1,ab=0,t=1):
    global medname,quantity,af_bf,tim
    if(number < 20):
        
        if(ab == 0):
            food = "BF"
        else:
            food = "AF"
        
        if(t == 1):
            time = ""
        elif(t == 2):
            time = ""
        elif(t == 3):
            time = ""
        elif(t == 4):
            time = ""
        del medname[number]
        medname.insert(number,med) 

        del quantity[number]
        quantity.insert(number,qty)

        del af_bf[number]
        af_bf.insert(number,food)

        del tim[number]
        tim.insert(number,time)
        

def signature(x):
    global addsignature
    addsignature = x
    generate()

def symptoms(x):
    global addsymptom
    addsymptom = x
    generate()

def diagnosis(x):
    global adddiagnosis
    adddiagnosis = x
    generate()

def advice(x):
    global addadvice
    addadvice = x
    generate()

def save():
    global addserial
    im_pil = Image.fromarray(cv2.cvtColor(templete,cv2.COLOR_BGR2RGB))
    im_pil.save("prescription" + str(addserial) + ".pdf","PDF",resolution = 100)


