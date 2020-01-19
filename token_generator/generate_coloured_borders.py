#!/usr/bin/env python
import os
import subprocess
FILES="Source"
COLORS={'white':'180,180,180', 'red':'180,0,0', 'green':'0,180,0', 'blue':'0,0,180', 'yellow':'180,180,0', 'cyan':'0,180,180','magenta':'180,0,180'}
#COLORS={'white':'180,180,180'}
dir_path = os.path.dirname(os.path.realpath(__file__))
MASKPATH = os.path.join(dir_path,"meta","mask.png")


DESTPATH = os.path.join(dir_path,"output")+os.sep
print()

for subdir, dirs, files in os.walk(os.path.join(dir_path,FILES)):
	for file in files:
		filename=str(file)
		fullname=os.path.join(subdir,file)
		if not filename.endswith(('.png','.jpg')):
			print("skipping "+filename)
			continue
		

		for key in COLORS.items():
			print("processing "+filename+" "+key[0])
			COMMANDS=["magick",
					 fullname+"[450x450]",
					 "-repage", "500x500",
					 "-background", "black",
					 "-gravity", "center",
					 "-extent","500x500",
					 MASKPATH,
					 "-alpha","Off",
					 "-compose",
					 "CopyOpacity", "-composite",
					 "-fill", "none",
					 "-stroke", "rgb("+key[1]+")",
					 "-strokewidth","15",
					 "-draw","circle 250,250,250,20",
					 "-stroke","rgb(50,50,50)",
					 "-strokewidth","5",
					 "-draw","circle 250,250,250,10",
					 '-resize','210x210',
					 'png8:'+DESTPATH+"t_"+os.path.splitext(filename)[0]+"-border-"+key[0]+".png"]
			COMMAND=''
			for c in COMMANDS:
				COMMAND+=" \""+c+"\""
			ret=os.popen(COMMAND)

