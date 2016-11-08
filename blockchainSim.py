import xlrd
import math
PACKET_SIZE = 791
LANE_NUM = 6
SIG_SIZE = 256

workbook = xlrd.open_workbook('inputFiles.xlsx')
sheet = workbook.sheet_by_index(0)

data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
#print data[1][0]
print "|t_put\t|cars/sect\t|numMinters\t|cars/Minter\t|mintDataRate\t|smartContractDataRate"
for x in range (1,r+1):
	spacing = data[x][0]
	transTime = data[x][1]
	TxR = data[x][2]
	secSize = data[x][3]
	#print spacing, transTime, TxR, secSize
	#mbps
	t_put = ((TxR/spacing*12) * 1/(transTime/1000) * PACKET_SIZE * 8)/1000000
	carsPerSection = secSize*1000/spacing * LANE_NUM
	#round up
	numMinters = math.ceil(carsPerSection/(TxR/spacing*12)) 
    
	#divide that number of minters up among all cars in section
	carsPerMinter = carsPerSection/numMinters
	minterDataInRate = (carsPerMinter * 1/(transTime/1000) * PACKET_SIZE * 8)/1000000
	scReqDataRate = (SIG_SIZE * carsPerMinter/(transTime/1000))/1000

	print "|%.3f\t" % t_put, "|%.1f\t\t" % carsPerSection, "|%.1f\t\t" % numMinters, "|%.2f\t\t" % carsPerMinter, "|%.3f\t\t" % minterDataInRate, "|%.3f" % scReqDataRate
