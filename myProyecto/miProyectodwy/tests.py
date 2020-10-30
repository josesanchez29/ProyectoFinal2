from django.test import TestCase
import unittest
from .models import Insumos
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your tests here.
class TestInsumos(unittest.TestCase):

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

#####################################################################################

class TestUsuario(unittest.TestCase):
   
    def test_login(self):
       usu = authenticate( username='auto', password='auto')
       if usu is not None and usu.is_active:
            assert True
       else:
           assert False

    def test_registro_usuario(self):
        valor = 0
        try:
            usu = User(
               first_name ="carlos",
               last_name="fuenzalida",
               email="ckarlitos.98.fuenzalida@gmail.com",
               username="Karlitos2341",
               password="111111111",
               
            )
            usu.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)


if __name__ == "__main__":
    unittest.main()        
