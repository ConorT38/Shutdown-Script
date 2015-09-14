from subprocess import Popen

f = open("x800a.bat", 'w')

f.write("shutdown.exe /h")

f.close()

#Open the batch file
p = Popen("x800a.bat")

#run the batch file
stdout, stderr = p.communicate()



