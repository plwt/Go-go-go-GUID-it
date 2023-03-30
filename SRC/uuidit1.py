import uuid
import subprocess

paths = {"openfile" = "/opt/Lets-UUID-it/SRC/UUID.txt"}

def uuidit():
    
    # Create UUID
    random_uuid = uuid.uuid4()

    # Create text file for UUID
    textfile=open('/opt/Lets-UUID-it/SRC/UUID.txt', 'w', encoding='utf-8')
    textfile.write('UUID =  \n')
    textfile.write('\n')
    
    # Enter UUID into text file and save file
    for element in random_uuid:
        textfile.write(element)
    textfile.write('\n')
    textfile.write('\n')

    textfile.close()
    
    subprocess.Popen(paths["fileopen"])

#run UUID generator 
uuidit()







   
    



    
    















   

