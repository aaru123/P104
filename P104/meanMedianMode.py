from collections import Counter
import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader=csv.reader(f)
    file_data = list(reader)

#remove the title
file_data.pop(0)

#sort the height data 
newdata = []

for i in range(len(file_data)) :
   newNum = file_data[i][2]
   newdata.append(float(newNum))

# mean 
length = len(newdata)
sum = 0
for x in newdata:
    sum += x
mean = sum/length

#median
newdata.sort()
length = len(newdata)

if length % 2 == 0 :
    
    median1 =  float(newdata[length//2])
   
    median2 =  float(newdata[length//2-1])
   
    median = (median1 + median2) /2
else:
     median = newdata[length//2]
     

#mode
data = Counter(newdata)
modedata = {
    '75-85':0,
    '85-95':0,
    '95-105':0,
    '105-115':0,
    '115-125':0,
    '125-135':0,
    '135-145':0,
    '145-155':0,
    '155-165':0,
    '165-175':0,
}

for weight, occurrence in data.items():
    if 75< float(weight)<85:
        modedata['75-85'] += occurrence
    elif 85< float(weight)<95:
        modedata['85-95'] += occurrence
    elif 95< float(weight)<105:
        modedata['95-105'] += occurrence
    elif 105< float(weight)<115:
        modedata['105-115'] += occurrence
    elif 115< float(weight)<125:
        modedata['115-125'] += occurrence
    elif 125< float(weight)<135:
        modedata['125-135'] += occurrence
    elif 135< float(weight)<145:
        modedata['135-145'] += occurrence
    elif 145< float(weight)<155:
        modedata['145-155'] += occurrence
    elif 155< float(weight)<165:
        modedata['155-165'] += occurrence
    elif 165< float(weight)<175:
        modedata['165-175'] += occurrence
        
 
modeRange, modeOccurrence = 0,0
for range, occurrence in modedata.items():
    if occurrence > modeOccurrence:
        modeRange, modeOccurrence = [int(range.split('-')[0]), int(range.split('-')[1])],occurrence

mode = float((modeRange[0] + modeRange[1])/2)


print('mode is',mode)
print ('median is',median,'pounds')
print('mean (average) is' , mean, 'pounds')
