import os



files = os.listdir(".\gaga")
path =".\\gaga\\"

newPath = ".\\gaga\\"
i = 0
for fName in files:

    fName = path + fName
    
    fileName =path +  "CMayup" + str(i) + ".png"
    os.rename(fName,fileName)
    i += 1 

    
