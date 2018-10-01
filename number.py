tupp=("one","two","three","four","five","six","seven","eight","nine")
x = input("Enter a Three digit number:\n")

if x[0]=="1":
    print("one hundred",end=" ")
else:
    print(tupp[int(x[0])-1],end=" ")
    print("hundred",end=" ")
if x[1:3]=="10":
    print("ten")
if x[1:3]=="11":
    print("eleven")
if x[1:3]=="12":
    print("twelve")
if x[1:3]=="13":
    print("thirteen")
if x[1:3]=="15":
    print("fifteen")
if x[1:3]=="18":
    print("eighteen")
if x[1:3]=="14":
    print("fourteen")
if x[1:3]=="16":
    print("sixteen")
if x[1:3]=="19":
    print("nineteen")
elif x[1]=="2":
    print("twenty",tupp[int(x[2])-1])
elif x[1]=="3":
    print("thirty",tupp[int(x[2])-1])
elif x[1]=="4":
    print("fourty",tupp[int(x[2])-1])
elif x[1]=="5":
    print("fifty",tupp[int(x[2])-1])
elif x[1]=="6":
    print("sixty",tupp[int(x[2])-1])
elif x[1]=="8":
    print("eighty",tupp[int(x[2])-1])
elif x[1]=="7":
    print("seventy",tupp[int(x[2])-1])
elif x[1]=="9":
    print("ninety",tupp[int(x[2])-1])
elif x[2]=="0":
    print(tupp[int(x[2])-1])

