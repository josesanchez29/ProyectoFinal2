from django.test import TestCase
import unittest
from .models import Insumos

# Create your tests here.

class TestBaseDatos(unittest.TestCase):

    def test_guardar_insumo(self):
        valor = 0
        try:
            insumo = Insumos(
               nombre="perfume",
               descripcion="200ml",
               precio=4000,
               stock=1
            )
            insumo.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)
     

    def test_Eliminar_insumo(self):
        valor = 0
        try:
            insumo = Insumos(
               nombre="alargador",
            )
            insumo.delete()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)




if __name__ == "__main__":
    unittest.main()        
