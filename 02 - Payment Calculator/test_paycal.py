from paycal import getpayment

def test_payment():
    assert getpayment(100, 60) == 4860
    assert getpayment(50, 80) == 3560