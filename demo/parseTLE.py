#!/usr/bin/python




def adder(stringsep):
	string=""
	for x in stringsep:
		string = string+x+" "
	return (string)

def updateTLE():
	#requestsObject = requests.get("http://celestrak.com/NORAD/elements/cubesat.txt")
	#tle = requestsObject.text
	#check celstrak data with some regex  to make sure it's the pattern we are expecting??

	tle = "EYESAT-1 (AO-27) 1 22825U 93061C 16349.12125796 -.00000001 00000-0 17078-4 0 9993 2 22825 98.7858 306.7055 0008926 145.9026 214.2730 14.29979804210953 CUTE-1 (CO-55) 1 27844U 03031E 16349.02274461 .00000066 00000-0 49751-4 0 9993 2 27844 98.6914 354.7200 0010123 157.5879 202.5743 14.22001456698005 CUBESAT XI-IV (CO-57) 1 27848U 03031J 16348.55036456 .00000054 00000-0 44496-4 0 9992 2 27848 98.7010 354.4315 0009844 167.3814 192.7612 14.21621118697823 CUBESAT XI 5 1 28895U 05043F 16348.66645112 .00000177 00000-0 42816-4 0 9997 2 28895 97.8437 153.7463 0017132 15.2617 344.9099 14.63312857593350 CUTE-1.7+APD II (CO-65) 1 32785U 08021C 16349.22704152 .00000264 00000-0 34594-4 0 9993 2 32785 97.5846 15.7815 0014512 64.3578 295.9136 14.87752809467394 COMPASS-1 1 32787U 08021E 16349.17367177 .00000635 00000-0 67320-4 0 9996 2 32787 97.5824 23.4161 0013543 41.3908 318.8335 14.92349536467905 AAUSAT-II 1 32788U 08021F 16348.67698724 .00000580 00000-0 60127-4 0 9993 2 32788 97.5825 25.4446 0012862 37.2011 323.0097 14.93594326467988"
	
	#splitTLE = tle.split(" ")

	#split by space
	splitspaceTLE = ['EYESAT-1', '(AO-27)', '', '', '', '', '', '', '', '\r\n1', '22825U', '93061C', '', '', '16349.12125796', '-.00000001', '', '00000-0', '', '17078-4', '0', '', '9993\r\n2', '22825', '', '98.7858', '306.7055', '0008926', '145.9026', '214.2730', '14.29979804210953\r\nCUTE-1', '(CO-55)', '', '', '', '', '', '', '', '', '', '\r\n1', '27844U', '03031E', '', '', '16349.02274461', '', '.00000066', '', '00000-0', '', '49751-4', '0', '', '9993\r\n2', '27844', '', '98.6914', '354.7200', '0010123', '157.5879', '202.5743', '14.22001456698005\r\nCUBESAT', 'XI-IV', '(CO-57)', '', '', '\r\n1', '27848U', '03031J', '', '', '16349.74685895', '', '.00000047', '', '00000-0', '', '41546-4', '0', '', '9996\r\n2', '27848', '', '98.7009', '355.6110', '0009909', '164.0510', '196.0981', '14.21621353697991\r\n']
	#split by \r\n
	splitrnTLE = ['EYESAT-1 (AO-27)        ', '1 22825U 93061C   16349.12125796 -.00000001  00000-0  17078-4 0  9993', '2 22825  98.7858 306.7055 0008926 145.9026 214.2730 14.29979804210953', 'CUTE-1 (CO-55)          ', '1 27844U 03031E   16349.02274461  .00000066  00000-0  49751-4 0  9993', '2 27844  98.6914 354.7200 0010123 157.5879 202.5743 14.22001456698005', 'CUBESAT XI-IV (CO-57)   ', '1 27848U 03031J   16349.74685895  .00000047  00000-0  41546-4 0  9996', '2 27848  98.7009 355.6110 0009909 164.0510 196.0981 14.21621353697991', 'CUBESAT XI 5            ', '1 28895U 05043F   16349.69213614  .00000172  00000-0  41979-4 0  9993', '2 28895  97.8437 154.7222 0017055  12.0624 348.0984 14.63313390593509', 'CUTE-1.7+APD II (CO-65) ', '1 32785U 08021C   16349.22704152  .00000264  00000-0  34594-4 0  9993', '2 32785  97.5846  15.7815 0014512  64.3578 295.9136 14.87752809467394', 'COMPASS-1               ', '1 32787U 08021E   16349.17367177  .00000635  00000-0  67320-4 0  9996', '2 32787  97.5824  23.4161 0013543  41.3908 318.8335 14.92349536467905', 'AAUSAT-II               ', '1 32788U 08021F   16349.68189769  .00000428  00000-0  45736-4 0  9999', '2 32788  97.5823  26.4141 0012808  33.9167 326.2870 14.93595647468133']

	newsplits = []
	for x in splitrnTLE:
		#temp = 
		newsplits.append(x.split(" "))
	
	#print (newsplits)

	for element in newsplits:
		for x in element:
			print(x)
			if (x == '') or (x==" "):
				print ("true")
				element.remove(x)

	print (newsplits)



	# ghjhg
	# splitslash = []

	# for x in splitspaceTLE:
	# 	if '\r\n' in x:
	# 		splitspaceTLE.append(x.split('\r\n'))
	# 		print ("true")

	# print (splitslash)
	# print (splitspaceTLE)

	# while len(splitTLE) != 0:
	# 	namesep = []
	# 	while splitTLE[0]!="1":
	# 		namesep.append(splitTLE.pop(0))
			
	# 	name = adder(namesep)

	# 	line1sep = splitTLE[:9]
	# 	del splitTLE[:9]
	# 	line1 = adder(line1sep)

	# 	line2sep = splitTLE[:8]
	# 	del splitTLE[:8]
	# 	line2 = adder(line2sep)

	# 	print(line2)
	# 	#newTLE = TLE(name=name,line1=line1,line2=line2)
	# 	#newTLE.save()


updateTLE()