# Import required packages
import cv2
import pytesseract

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
f = open("hundred_left.csv", "w")
f = open("hundred_right.csv", "w")
for frame in range(17606,21281):
#
	print("hello")
	#frame = 4785;
	frame = str(frame).zfill(5)
#print(frame)
	filename = "F:\Cricket\ODI Frames\\ODI_"+str(frame)+".png"
#print(filename)
# Read image from which text needs to be extracted
	img = cv2.imread(filename)

#Hundred Left 57 176 102 652
#Hundred Right 1761 193 102 652

#ODI
	#Batting team = 238, 620, 77, 35
	#Innings Score = 323, 620, 85, 35
	# #Overs = 260, 657, 141, 30
	r_left = [323, 620, 85, 35]
	score_roi_left = img[int(r_left[1]):int(r_left[1]+r_left[3]),int(r_left[0]):int(r_left[0]+r_left[2])]

	gray_roi_left = cv2.cvtColor(score_roi_left, cv2.COLOR_BGR2GRAY)

	ret, thresh_roi_left = cv2.threshold(gray_roi_left, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV )

	cv2.imshow("window", thresh_roi_left)
	cv2.waitKey()

	text_left = pytesseract.image_to_string(thresh_roi_left)
	score_left = text_left.strip()
	
	# r_right = [1761, 193, 102, 652]
	# score_roi_right = img[int(r_right[1]):int(r_right[1]+r_right[3]),int(r_right[0]):int(r_right[0]+r_right[2])]

	# gray_roi_right = cv2.cvtColor(score_roi_right, cv2.COLOR_BGR2GRAY)

	# ret, thresh_roi_right = cv2.threshold(gray_roi_right, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV )

	# # #cv2.imshow("window", thresh_roi)
	# # #cv2.waitKey()

	# text_right = pytesseract.image_to_string(thresh_roi_right)
	# score_right = text_right.strip()	
	
	
	# print(frame)
	
	# f = open("hundred_left.csv", "a")
	# f.write(str(frame)+","+score_left+"\n")
	# f.close()

	# f = open("hundred_right.csv", "a")
	# f.write(str(frame)+","+score_right+"\n")
	# f.close()





