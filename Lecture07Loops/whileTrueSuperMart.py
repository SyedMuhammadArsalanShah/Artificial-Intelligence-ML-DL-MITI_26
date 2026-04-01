counter=1
finalBill=0
while True:
    
    print("Item No ",counter)
    price=int(input("Enter Your Item Price Here\n"))
    finalBill=finalBill+price
    counter=counter+1
    if price == 00:
        break
    

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