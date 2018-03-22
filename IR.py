IR = "river.jpg"
IB = "river.jpg"
NIVDTest = "river.jpg"


def openImage(pic, winnum):
	IR = pmOpenImage(winnum,pic)
	wd = getWidth(winnum)
	ht = getHeight(winnum)

def getWidth(n):
	width = pmGetImageWidth(n)
	return width
def getHeight(n):
	height = pmGetImageHeight(n)
	return height


#because of our camera, the red channel is mostly just ir
#so we will use that to compute our ir image
def NIR(pic,winnum):
	wd = getWidth(winnum)
	ht = getHeight(winnum)
	print wd
	print ht

	print "this is rgb for 200 100"
	print pmGetPixel(winnum,200,100)

	for w in range(wd):
		for h in range(ht):
			rgb = pmGetPixel(winnum,w,h)
			red = rgb[0]
			rgb = pmSetPixel(winnum,w,h, red, red, red)

def NIB(pic ,winnum):
	wd = getWidth(winnum)
	ht = getHeight(winnum)

	for w in range(wd):
		for h in range(ht):
			rgb = pmGetPixel(winnum,w,h)
			blue = rgb[2]
			rgb = pmSetPixel(winnum,w,h, blue, blue, blue)


def NIVD(pic, winnum):
	wd = getWidth(winnum)
	ht = getHeight(winnum)

	for w in range(wd):
		for h in range(ht):
			rgb = pmGetPixel(winnum,w,h)
			compared = compare(rgb[0], rgb[1], rgb[2])
			rgb = pmSetPixel(winnum,w,h, compared[0], compared[1], compared[2] )

def compare(red, green, blue):
	bsubr = blue-red
	gsubr = green-red
	if(red>blue):
		green += bsubr
		blue = 0
		red = 0
	
	elif(blue<red):
		red /=4
		blue += (gsubr+red)
		green = 0
		

	return(red, green, blue)
pmOpenImage(0,"river.jpg")
#pmOpenImage(1, "riverbluehst.jpg")
openImage(IR, 1)
openImage(IB, 2)
openImage(NIVDTest, 3)
NIR(IR,1)
NIB(IB,2)
NIVD(NIVDTest,3)

#pmOpenImage(5, "nir_river.jpg")
#pmOpenImage(4, "blue_river.jpg")




