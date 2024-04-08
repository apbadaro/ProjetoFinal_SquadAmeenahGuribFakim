
//? CÓDIGO PARA MENU HAMBURGUER:

// Capturar o Clic da Página:
var menuIcon = document.querySelector('.menu-icon');

var ul = document.querySelector('.ul');

// TESTE DE CLICK
// menuIcon.addEventListener('click', ()=>{
//     alert("Clicou no ícone do Menu")
// })

menuIcon.addEventListener('click', ()=>{
    if (ul.classList.contains('ativo')) {
        ul.classList.remove('ativo');
        // Para fechar um X no Amburguer:
        // document.querySelector('.menu-icon img').src = '/static/img/menu-branco.png';
        document.querySelector('.menu-icon img').src = '../static/img/menu-branco.png';

    }

    else {
        ul.classList.add('ativo');
        // Senão usa a imagem do amburguer fechado
        // document.querySelector('.menu-icon img').src = '/static/img/menu-close-branco.png';
        document.querySelector('.menu-icon img').src = '../static/img/menu-close-branco.png';
        // menu-close-branco
    }
});

