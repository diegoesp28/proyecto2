$(document).ready(function() {
	$("#formulario").validate({
	  rules: {
		nombre : {
		  required: true,
		  minlength: 3
		},
		ciudad: {
		  required: true,
		  minlength: 3
		},
		correo: {
		  required: true,
		  email: true
		},
		comentario: {
		  required: true,
		  minlength: 20
		}
	  },
	  messages : {
		nombre: {
		  minlength: "el nombre requiere 3 caracteres"
		},
		ciudad: {
		  required: "requiere 3 caracteres",
		},
		correo: {
		  correo: "tiene que ser en formato correo: abc@domain.tld"
		},
		comentario: {
		  required: "tiene que tener minimo 20 caracteres",
		  
		}
	  }
	});
  });