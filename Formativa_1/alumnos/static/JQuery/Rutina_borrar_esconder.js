var flag = true;
function esconder(){
if (flag){
  document.getElementById("contrasena").type = "password";

  document.getElementById("eye").src = "img/icons8-ojo-cerrado-16.png";
  flag = false;
}
else{
  document.getElementById("contrasena").type = "text";
  document.getElementById("eye").src = "img/icons8-visible-16.png";

  flag = true;
}
}

function empty(){
  document.getElementById("contrasena").value ="";
}

var bandera = true;
function esconderConfCont(){
if (bandera){
  document.getElementById("confirmarContrasena").type = "password";
  document.getElementById("eyeConfCont").src = "img/icons8-ojo-cerrado-16.png";
  bandera = false;
}
else{
  document.getElementById("confirmarContrasena").type = "text";
  document.getElementById("eyeConfCont").src = "img/icons8-visible-16.png";
  bandera = true;
}
}
function emptyConfCont(){
  document.getElementById("confirmarContrasena").value = "";
}

