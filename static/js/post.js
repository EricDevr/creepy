function votar(id_post, voto_c) {
    $.ajax({
        url: "http://127.0.0.1:8000/post/voto/"+id_post+"/"+voto_c+"/",
        data: {

        },
        success: success_res
    });
}
function success_res(response) {
    $("#" + response['voto']).html(response['cant'])
}