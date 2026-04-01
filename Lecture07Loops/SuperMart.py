
numberOfItems=int(input("Enter Your Number Of Items\n"))
finalBill=0
for i in range(1,numberOfItems+1):
    print("Item No",i)
    itemsPrice=int(input("Enter Your Item Price \n"))
    finalBill=finalBill+itemsPrice
    
print("Your Total Bill is",finalBill )


if finalBill <=10000:
    discount =finalBill*0.2
    afterDiscBill=finalBill-discount
    print("After Discount Your Bill Is ", afterDiscBill)
elif finalBill <=20000:
    discount =finalBill*0.5
    afterDiscBill=finalBill-discount
    print("After Discount Your Bill Is ", afterDiscBill)
else:
    discount =finalBill*0.75
    afterDiscBill=finalBill-discount
    print("After Discount Your Bill Is ", afterDiscBill)
