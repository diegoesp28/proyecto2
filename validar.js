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
		},
		documento: {
			minlength:9,
			maxlength:10
		}
	  },
	  messages : {
		nombre: {
		  minlength: "el nombre requiere 3 caracteres",
		  required: "nesesitas un nombre"
		},
		ciudad: {
		  required: "ciudad con 3 caracteres",
		  minlength: "ciudad con 3 caracteres"
		},
		correo: {
		  correo: "tiene que ser en formato correo: abc@domain.tld",
		  required: "re quiere un correo"
		},
		comentario: {
		  required: "requiere un comentario",
		  minlength: "requiere minimo 20 caracteres"
		  
		},
		documento: {
			required: "requiere un rut o pasaporte",
			minlength:"faltan caracteres",
			maxlength:"sobra caracteres"
		}
	  }
	});
  });