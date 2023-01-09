import pytest

class TestProstokąt:
    def test_prostokąt_1(self):
        a = [ 1, 2 ]
        b = [ 1, 3 ]
        c = [ 4, 2 ]
        d = [ 4, 3 ]
        
        assert czy_prostokąt == True
        
    def test_prostokąt_2(self):
        a = [ 1, 2 ]
        b = [ 1, 3 ]
        c = [ 4, 2 ]
        d = [ 4, 2 ]
        
        assert czy_prostokąt == False
        
    def test_prostokąt_3(self):
        a = [ 1, 2 ]
        b = [ 1, 3 ]
        c = [ 2, 2 ]
        d = [ 2, 2 ]
        
        assert czy_prostokąt == False
        
    