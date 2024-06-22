var flag = true;

function esconder(){
  const passwrod = document.getElementById("id_password1");
 if (passwrod === "password"){
  passwrod.type = "text";
 }
 else
 {
  passwrod.type ="password";
 }
}

