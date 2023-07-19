class Menu {
    constructor(menuButton, menuContainer) {
        this.menuButton = menuButton;
        this.menuContainer = menuContainer;
    }

    addEvent() {
        menuButton.addEventListener('click', this.OpenMenu)
        menuContainer.querySelector('#MenuClose').addEventListener('click', this.CloseMenu)
    }

    OpenMenu() {
        menuContainer.classList.add('active')
        var items = document.querySelectorAll('.menu__item')
    
        for (i = 1; i < items.length; i++) {
            (function(i) {
                window.setTimeout(function () {
                    var item = items[i];
                    item.classList.add('appear')
                }, (i+1)*200);
            }(i));
        }
    }
    
    CloseMenu() {
        menuContainer.classList.remove('active')
        window.setTimeout(function () {
            var items = document.querySelectorAll('.menu__item')
            for (let item of items) {
                item.classList.remove('appear')
            }
        }, 1000);
    }
}