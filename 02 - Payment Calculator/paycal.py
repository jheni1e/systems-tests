def getpayment(hour_class, hours_total):
    payment = hour_class * hours_total
    if (payment > 5000):
        payment = payment * 0.81
    else:
        payment = payment * 0.89
    
    return payment