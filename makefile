#www.cprogramming.com/tutorial/makefiles.html

nFrames = 24 

CC = python 
FILES = render_PS_anim.py
SOURCE = castle.ps



anim:
	make frames
	make gif
	make clean


frames: $(FILES)
	$(CC) $(FILES) $(SOURCE) $(nFrames)

gif:
	convert -delay 4 -loop 0 *.png ps_anim.gif

clean:
	rm *.png




