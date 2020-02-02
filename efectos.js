//METODO GET
var id_get = $("#id_get").val();
$('.api_get').click( function() {
    $.ajax({
      
             url : "http://localhost:8000/api/carros/",
             type: 'GET',
             dataType: "json",
             success : function (data) {
                      $('#nombre').text( data[0].nombre);
                      $('#precio').text( data[0].precio);
                      $('#año').text( data[0].año);
                    }
                 });
             });

//METODO DELETE
var id_delete = $("#id_eliminar").val();
$('.api_delete').click(function(){
    $.ajax({
        url: "http://localhost:8000/api/carros/"+id_delete+"/",
        data: {},
        type: 'DELETE',
        contentType: 'application/json',
        success: function(result) {
            console.log('DELETE atendido correctamente');
        },
    });
});

//METODO POST
$(".api_post").click(function(){          

    var data = {};
    data.nombre = $("#nombre_post").val();
    data.precio = $("#precio_post").val();
    data.año = $("#año_post").val();

    $.ajax({
        url: "http://localhost:8000/api/carros/",
        type: "POST",
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        beforeSend: function (xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
    },
    success: function (arg) {
        location.reload()
    },
        success: function(data){
            alert(data);
        },
        failure: function(errMsg) {
            alert(errMsg);
        }
    });
});




