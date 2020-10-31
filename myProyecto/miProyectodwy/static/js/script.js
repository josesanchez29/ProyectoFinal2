function validarRut() {
    var rut = document.getElementById("txtrut").value;
    if (rut.length != 10) {
        alert("Largo de rut incorrecto, debe tener 10 caracteres.");
        return false;
    }
    var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var car = rut.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = "K";

        }
        else {
            dv = 0;
        }
    }
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        alert("rut incorrecto");
        return false;
    }
    else {
        alert("rut correcto")
        return true;
    }
}

function validarPrecio() {
    var precio = document.getElementById("txtprecio").value;
    if (precio <= 0) {
        alert("El precio debe ser mayor a $0");
        return false;
    } else {
        alert ("precio correcto")
        return true;
    }
}

function validarFecha() {
    var fechaControl = document.getElementById("txtfecha").value;
    var fechaSistema = new Date();
    ////////////////////////////////
    var ano = fechaControl.slice(0, 4);
    var mes = fechaControl.slice(5, 7);
    var dia = fechaControl.slice(8, 10);
    ///////////////////////////////////
    var fechadelControl = new Date(ano, mes - 1, dia);
    ///////////////////////////////////////
    if (fechadelControl > fechaSistema) {
        alert("fecha de nacimiento incorrecta");
        return false;
    } else {
        alert("fecha correcta");
        var unDia = 24 * 60 * 60 * 1000;
        var diferencia = Math.round(Math.abs((fechaSistema.getTime() - fechadelControl.getTime()) / unDia));
        var anos = Math.round(diferencia / 365);
        return true;
    }
}


function grabar() {
    var rut = document.getElementById("txtrut").value;
    var nom = document.getElementById("txtnombre").value;
    var ape = document.getElementById("txtapellido").value;
    cli = new cliente();
    cli.setRut(rut);
    cli.setNombre(nombre);
    cli.setApellido(apellido);
    alert(cli.imprimir());
}


function validarTodo() {
    var resp = validarRut();
    if (resp == false) {
        return false;
    }
    var resp = validarFecha();
    if (resp == false) {
        return false;
    }

}
