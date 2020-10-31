function validarNombre(){
   var nombre = document.getElementById("txtnombre").value;
   if(nombre.trim().length >= 3 && nombre.trim().length <=8){
      return true;
    } 
  if(nombre.trim().length < 3){
  alert("el nombre debe contener entre 3 y 80 caracteres y no debe estar vacio");
  return false;
  }
}

function validarApellido(){
    var apellido = document.getElementById("txtapellido").value;
    if(apellido.trim().length >= 3 && apellido.trim().length <=8){
        return true;
    } 
    if(apellido.trim().length < 3){
        alert("el apellido debe contener entre 3 y 80 caracteres y no debe estar vacio");
        return false;
    }


}


function validarUsuario(){
    var usuario = document.getElementById("txtnombreusuario").value;
    if(usuario.trim().length >= 8){
        return true;
    } 
    if(usuario.trim().length < 8){
        alert("usuario debe contener como minimo 8 caracteres");
        return false;
    }


}




function ValidarFormulario(){
    var resp = true;

    if(validarNombre() == false){
    resp = false;
    }

        
    if(validarApellido() == false){
    resp = false;
    }

    if(validarUsuario() == false){
    resp = false;
    }
    return resp;
}




function validarNombreinsumo(){
    var nombre = document.getElementById("txtnombre").value;
    if(nombre.trim().length >= 3 && nombre.trim().length <=120){
       return true;
     } 
   if(nombre.trim().length < 3){
   alert("el nombre del insumo debe contener entre 3 y 80 caracteres y no debe estar vacio");
   return false;
   }
 }


function Validarinsumo(){
    var resp = true;
    if(validarNombreinsumo() == false){
    resp = false;
    }

    return resp;
}
