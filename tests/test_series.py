from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci_5():
    expected=5
    actual= fibonacci(5) 
    assert expected == actual

def test_fibonacci_2():
    expected=1
    actual= fibonacci(2) 
    assert expected == actual

def test_fibonacci_3():
    expected=2
    actual= fibonacci(3) 
    assert expected == actual

def test_fibonacci_7():
    expected=13
    actual= fibonacci(7) 
    assert expected == actual

def test_lucas_0():
    expected=2
    actual= lucas(0) 
    assert expected == actual
    


def test_lucas_3():
    expected=4
    actual= lucas(3) 
    assert expected == actual
    

def test_lucas_7():
    expected=29
    actual= lucas(7)
    assert expected == actual
    

def test_sum_series():
    expected=8
    actual= sum_series(3, 4, 2)
    assert expected == actual
    


def test_sum_series():
    expected=6
    actual= sum_series(3, 4, 1)
    assert expected == actual

    
    