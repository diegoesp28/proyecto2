
$(document).ready(function() {
	$("#formulario").validate({
	  rules: {
		nombre : {
		  required: true,
		  minlength: 3
		},
		numero: {
		  required: true,
		  minlength: 1
		},
		edad: {
		  required: true,
		  minlength: 3
		},
		id_tipo_animal: {
		  required: true
		},
		id_genero: {
			required:true
		},
		img_mascota: {
			required:true
		}
	  },
	  messages : {
		nombre: {
		  minlength: "el nombre requiere 3 caracteres",
		  required: "nesesitas un nombre"
		},
		numero: {
		  required: "identificador ",
		  minlength: "identificador almenos un caracterer"
		},
		edad: {
		  required: "re quiere un aproximado"
		},
		id_tipo_animal: {
		  required: "requiere un animal",
		  
		},
		id_genero: {
			required: "requiere un genero"
		},
		img_mascota: {
			required: "requiere un genero"
		}
	  }
	});
  });

  

