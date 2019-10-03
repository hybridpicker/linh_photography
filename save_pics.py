import glob, os
from portfolio.models import Photo
import shutil

def save_pics():

    directories = []
    
    c = 1
    for dir in directories:
        os.chdir(dir)
        i = 1
        for file in sorted(glob.glob("*")):
            new_file = Photo.objects.create(title=str(file),
                                            images="portfolio/images/" + file,
                                            category_id=int(c),
                                            ordering=int(i))
            new_file.save()
            i += 1
            print(new_file)
        c +=1
