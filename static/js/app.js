$(document).ready(function() {
    $("#select_species").select2();
});

$(document).on("click", ".open-details-dialog", function (e) {
    e.preventDefault();
    var details = $(this).data('detalhes');
    var $popup = $("#popup");
    $('#register-details').text(details);
    $popup.modal("show");
});

function mostrar_detalhe (detalhe) {
	alert(detalhe)
}