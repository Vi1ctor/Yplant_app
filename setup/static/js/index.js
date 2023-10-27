$(document).ready(function() {
    // Obtém a URL atual
    var currentUrl = window.location.href;

    // Itera sobre as abas da barra de navegação
    $(".navbar-nav .nav-link").each(function() {
        // Obtém o link de destino da aba
        var tabUrl = $(this).attr("href");

        // Verifica se a URL atual corresponde à URL da aba
        if (currentUrl.indexOf(tabUrl) !== -1) {
            // Aplica a classe "active" à aba correspondente
            $(this).parent().addClass("active");
        }
    });
});


