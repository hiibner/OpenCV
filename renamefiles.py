import os
#Dateiendung ändern
counter = 0
for filename in os.listdir('C:/Users/Hyu/Downloads/Monogramme'):
    new_filename = filename.split('.')[0]
    os.rename('C:/Users/Hyu/Downloads/Monogramme/' + filename, 'C:/Users/Hyu/Downloads/Monogramme/'+new_filename+'.jpg')
