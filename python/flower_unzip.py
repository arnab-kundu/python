import os, sys, tarfile

# README - How to run 
# 1. Keep this file and flower_photos.tgz file in same folder.
# 2. Open ternimal in same location.
# 3. Run python flower_unzip.py flower_photos
# Or. Run python flower_unzip.py <your_.tgz_or_.tar_filename_without_extension>

def extract(tar_url, extract_path='.'):
    print(tar_url)
    tar = tarfile.open(tar_url, 'r')
    for item in tar:
        tar.extract(item, extract_path)
        if item.name.find(".tgz") != -1 or item.name.find(".tar") != -1:
            extract(item.name, "./" + item.name[:item.name.rfind('/')])
try:

    extract(sys.argv[1] + '.tgz')
    print('Done.')
except:
    name = os.path.basename(sys.argv[0])
    print(name[:name.rfind('.')], '<filename>')
