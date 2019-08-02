import unittest
#import mymodule
from fibo import fibonacci
#from main import *

class TestMyModule(unittest.TestCase):

 def test_fibo(self):
   fibo = fibonacci() 
   esperado = 0
   actual = fibo.siguiente()
   self.assertEqual(esperado, actual)
  

if __name__ == "__main__":
   unittest.main()