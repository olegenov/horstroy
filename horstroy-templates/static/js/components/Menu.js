class Menu {
    constructor(menuButton, menuContainer) {
        this.menuButton = menuButton;
        this.menuContainer = menuContainer;
        this.OpenMenu = this.OpenMenu.bind(this);
        this.CloseMenu = this.CloseMenu.bind(this);
    }

    addEvent() {
        this.menuButton.addEventListener('click', this.OpenMenu)
        this.menuContainer.querySelector('#MenuClose').addEventListener('click', this.CloseMenu)
    }

    OpenMenu() {
        this.menuContainer.classList.add('active')
        var items = document.querySelectorAll('.menu__item')
    
        for (i = 0; i < items.length; i++) {
            (function(i) {
                window.setTimeout(function () {
                    var item = items[i];
                    item.classList.add('appear')
                }, (i+1)*200);
            }(i));
        }
    }
    
    CloseMenu() {
        this.menuContainer.classList.remove('active')
        window.setTimeout(function () {
            var items = document.querySelectorAll('.menu__item')
            for (let item of items) {
                item.classList.remove('appear')
            }
        }, 1000);
    }
}