file=open("File3.txt",'r')
process=0
for text in file:
    data=text.split()
    if process==0:
        process={data[0]:{"Burst_Time":data[1],"Priority":data[2]}}
    elif data[0] not in process:
        process[data[0]]={"Burst_Time":data[1],"Priority":data[2]}
value=0
print('|',value)
while len(process)>0:
    maxPriority = list(process.keys())[0]
    for i in process:
        if process.get(i).get("Priority")>process.get(maxPriority).get("Priority"):
            maxPriority=i
    for i in range(int(process.get(maxPriority).get("Burst_Time"))):
        print('-')
        value+=1
    print('|',maxPriority)
    process.pop(maxPriority)
print('Total time = ',value)