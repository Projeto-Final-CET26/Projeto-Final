// Pedidos AJAX (jQuery) para o CRUD da API de livros.

var API = "http://192.168.11.165:8000/books";

function listarLivros() {
    $.ajax({
        url: API,
        method: "GET",
        success: function (resposta) {
            $("#resultado").text(JSON.stringify(resposta, null, 2));
        },
        error: function (erro) {
            $("#resultado").text("Erro: " + erro.status + " " + erro.responseText);
        }
    });
}

function obterLivro() {
    $.ajax({
        url: API + "/" + $("#id").val(),
        method: "GET",
        success: function (resposta) {
            $("#resultado").text(JSON.stringify(resposta, null, 2));
        },
        error: function (erro) {
            $("#resultado").text("Erro: " + erro.status + " " + erro.responseText);
        }
    });
}

function enviarLivro() {
    var ano = $("#ano").val();

    $.ajax({
        url: API,
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            title: $("#titulo").val(),
            author: $("#autor").val(),
            year: ano ? Number(ano) : null
        }),
        success: function (resposta) {
            $("#resultado").text(JSON.stringify(resposta, null, 2));
        },
        error: function (erro) {
            $("#resultado").text("Erro: " + erro.status + " " + erro.responseText);
        }
    });
}

function actualizarLivro() {
    var ano = $("#ano").val();

    $.ajax({
        url: API + "/" + $("#id").val(),
        method: "PUT",
        contentType: "application/json",
        data: JSON.stringify({
            title: $("#titulo").val(),
            author: $("#autor").val(),
            year: ano ? Number(ano) : null
        }),
        success: function (resposta) {
            $("#resultado").text(JSON.stringify(resposta, null, 2));
        },
        error: function (erro) {
            $("#resultado").text("Erro: " + erro.status + " " + erro.responseText);
        }
    });
}

function apagarLivro() {
    $.ajax({
        url: API + "/" + $("#id").val(),
        method: "DELETE",
        success: function () {
            $("#resultado").text("Livro apagado.");
        },
        error: function (erro) {
            $("#resultado").text("Erro: " + erro.status + " " + erro.responseText);
        }
    });
}
