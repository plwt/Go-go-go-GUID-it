import uuid

def guidit():
    
    # Create GUID
    random_uuid = uuid.uuid4()

    # Create text file for GUID
    textfile=open('/opt/GoGoGoGUIDIt/src/GUID.txt', 'w', encoding='utf-8')
    textfile.write('GUID =  \n')
    textfile.write('\n')
    
    # Enter GUID into text file and save file
    for element in random_uuid:
        textfile.write(element)
    textfile.write('\n')
    textfile.write('\n')

    textfile.close()

#run GUID generator 
guidit()
  

    




 













    



  
  






    










