//la validacion antterior quedo como formato de rut devido a que el nuevo no modifica sino que acepta formato
function validaRut(campo){
	if ( campo.length == 0 ){ return false; }
	

	campo = campo.replace('-','')
	campo = campo.replace(/\./g,'')

	var suma = 0;
	var caracteres = "1234567890kK";
	var contador = 0;    
	for (var i=0; i < campo.length; i++){
		u = campo.substring(i, i + 1);
		if (caracteres.indexOf(u) != -1)
		contador ++;
	}
	if ( contador==0 ) { return false }
	
	var rut = campo.substring(0,campo.length-1)
	var drut = campo.substring( campo.length-1 )
	var dvr = '0';
	var mul = 2;
	
	for (i= rut.length -1 ; i >= 0; i--) {
		suma = suma + rut.charAt(i) * mul
                if (mul == 7) 	mul = 2
		        else	mul++
	}
	res = suma % 11
	if (res==1)		dvr = 'k'
                else if (res==0) dvr = '0'
	else {
		dvi = 11-res
		dvr = dvi + ""
	}
	if ( dvr != drut.toLowerCase() ) { return false; }
	else { return true; }
}


$.validator.addMethod("rut", function(value, element) { 
        return this.optional(element) || validaRut(value); 
}, "Revise el RUT");


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
			required:true,
			rut: true
			
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
			rut:'inserte un rut valido'
			
			
		}
	  }
	});
  });

  

