//------------clima

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
        jQuery('#geo').html('<button type="button" onclick="getLocation()" class="btn btn-success ">'+data.location.name+ ', ' +data.location.country+': '+data.current.temp_c+'°c </button>');
    });
}

jQuery(document).ready(function(){
    getLocation();
});



