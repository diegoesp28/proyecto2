function getLocation(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        JQuery('#geo').html('la localizacion no  se puede conseguir.');
    }
}

function showPosition(position){
    var latitud = position.coords.latitude;
    var longitud = position.coords.longitude;
    var linkAPI = 'http://api.weatherapi.com/v1/current.json?key=261a3397a09c419cb67155250211405&q=';
    var url = linkAPI +latitud +','+longitud;
    jQuery.getJSON(url , 
    function(data){
        jQuery('#geo').html('<p style="font-family: sans-serif;"> Clima:'+data.location.name+ ', ' +data.location.country+': '+data.current.temp_c+'°c </p>');
    });
}

jQuery(document).ready(function(){
    getLocation();
});


//validar rut

function validarRut(rut){
    //quitando puntos en la variable
    var valor = rut.value.replace('.','');
    //quitando comas
    valor = valor.replace('-','');
    //quitando guion
    valor = valor.replace(',','');

    //sacando los cuerpos y divito verificador

    cuerpo = valor.slice(0,-1);
    dv = valor.slice(-1).topUpperCase();

    //formatear run
    rut.value = cuerpo + '-'+ dv

    //si no cumple con el minimo ej. (n.nnn.nnn)

    if(cuerpo.length < 7){rut.setCustomValidity("Rut Incompleto");return false;}

    //calcular digito verificador
    suma = 0;
    multiplo = 2;


    //para cada digito del cuerpo

    for (i=1;i<=cuerpo.length;i++){
        index = multiplo * valor.charAt(cuerpo.length - i);

        //sumar al contador general
        suma= suma + index;

        // consolidar multiplo dentro del rango [2,7]
        if(multiplo <7){multiplo = multiplo+1;}else {multiplo = 2;}
    }

    dvEsperado = 11 - (suma % 11);
    
    // Casos Especiales (0 y K)
    dv = (dv == 'K')?10:dv;
    dv = (dv == 0)?11:dv;
    
    // Validar que el Cuerpo coincide con su Dígito Verificador
    if(dvEsperado != dv) { rut.setCustomValidity("RUT Inválido"); return false; }
    
    // Si todo sale bien, eliminar errores (decretar que es válido)
    rut.setCustomValidity('');
}