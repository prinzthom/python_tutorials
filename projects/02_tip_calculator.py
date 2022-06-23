from tkinter import N, Y


print ("Tip Calculator")
bill = input("how much was the bill?")
tip = input("how much would you like to Tip: 10%, 12%, 15%")
tip_percent = ((float(tip))/100)
ttl_tip = (float(bill))*(float(tip_percent))
ttl_bill = (float(bill))+(float(ttl_tip))
print (f"you are tiping ${ttl_tip}")
splt_bill = input("would you like to split the bill? [y/n]")
if splt_bill == Y:
    ppl_splt = input("how many people would you like to split the bill with?")
    ttl_splt_bill = (ttl_bill)/(int(ppl_splt))
    print (f"you need to pay a total of ${ttl_bill}")
    print(f"each of you will have to pay ${ttl_splt_bill} ")
if splt_bill == N:
    print (f"you need to pay a total of {ttl_bill}")
