$(document).ready(function(){
    $("#registrar").click(function(){
        var nombre = $("#user").val();
        var correo = $("#id_email").val();
        var confirmarCorreo = $("#confirmar_correo").val();
        var pass =$("#contrasena").val();
        var conPass = $("#confirmarContrasena").val();
        var passRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$/;
        var isValid = true;

        function validarCorreo(correo){
            var emailRegex = /^[a-zA-Z0-9._%+-]+@(gmail|hotmail)\.(com|cl)$/;
            return emailRegex.test(correo)

        }
        function validarFormulario() {
            var correo = $('#id_email').val(); // Obtener el valor del campo de correo electrónico
            if (!validarCorreo(correo) && correo == null && correo == "") {
                // Si el correo no es válido, mostrar un mensaje de error
                $('#errorCorreo').text('Correo electrónico inválido');
                e.preventDefault();

                return false;
            }
            return true;
        }
    
        // Manejar la validación cuando se envía el formulario
        $('#miFormulario').submit(function() {
            return validarFormulario();
        });

        
        
        if (!emailRegex.test(correo)) {
            $("#errorCorreo").fadeIn();
            isValid = false;
        } else {
            $("#errorCorreo").fadeOut();
        }

        if (confirmarCorreo !== correo) {
            $("#errorConfirmarCorreo").fadeIn();
            isValid = false;
        } else {
            $("#errorConfirmarCorreo").fadeOut();
        }

        if (nombre.length > 20 || nombre.length < 5 || nombre === "") {
            $("#errorUser").fadeIn();
            isValid = false;
        } else {
            $("#errorUser").fadeOut();
        }

        if (!passRegex.test(pass)) {
            $("#errorPass").fadeIn();
            isValid = false;
        } else {
            $("#errorPass").fadeOut();
        }

        if (pass !== conPass) {
            $("#errorConfirmarPass").fadeIn();
            isValid = false;
        } else {
            $("#errorConfirmarPass").fadeOut();
        }

        if (!isValid) {
            $('')
            e.preventDefault();
        }
    });



})