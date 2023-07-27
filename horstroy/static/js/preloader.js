window.onload = function () {
    window.setTimeout(function () {
        element = document.querySelector('.preloader')
        element.classList.add('loaded_hiding');
        window.setTimeout(function () {
            element.classList.add('loaded');
            element.classList.remove('loaded_hiding');
        }, 1000);
    }, 2000);
}