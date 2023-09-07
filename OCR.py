# Import required packages
import cv2
import pytesseract

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
f = open("scorecard.csv", "w")
for frame in range(1, 29033):
#
	frame = str(frame).zfill(5)
	#print(frame)
	filename = "F:\Cricket\ODI Frames\\ODI_"+str(frame)+".png"
	#print(filename)
# Read image from which text needs to be extracted
	img = cv2.imread(filename)

	# #Batting team = 238, 620, 77, 35
	# #Innings Score = 323, 620, 85, 35
	# #Overs = 260, 657, 141, 30
	r = [323, 620, 85, 35]
	score_roi = img[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]

	gray_roi = cv2.cvtColor(score_roi, cv2.COLOR_BGR2GRAY)

	ret, thresh_roi = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV )

	# #cv2.imshow("window", thresh_roi)
	# #cv2.waitKey()

	text = pytesseract.image_to_string(thresh_roi)
	score = text.strip()
	f = open("scorecard.csv", "a")
	print(str(frame)+","+score)
	f.write(str(frame)+","+score+"\n")
	f.close()





