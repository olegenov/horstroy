class Info {
    constructor(card, infoWindow) {
        this.card = card;
        this.infoWindow = infoWindow;
        this.OpenWindow = this.OpenWindow.bind(this);
        this.CloseWindow = this.CloseWindow.bind(this);
    }

    addEvent() {
        this.card.addEventListener('click', this.OpenWindow)
        this.infoWindow.querySelector('#WindowClose').addEventListener('click', this.CloseWindow)
    }

    OpenWindow() {
        this.infoWindow.classList.add('active')
        document.body.style.overflow = 'hidden';
    }
    
    CloseWindow() {
        this.infoWindow.classList.remove('active')
        document.body.style.overflow = 'auto';
    }
}