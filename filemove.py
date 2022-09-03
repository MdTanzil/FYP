import os
import shutil
sourcepath=r'C:\Users\mdtan\Desktop\TraindatasetforSSD'
sourcefiles = os.listdir(sourcepath)
destinationpath = r'C:\Users\mdtan\Desktop\Final Dataset\annots'
for file in sourcefiles:
    if file.endswith('.xml'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))