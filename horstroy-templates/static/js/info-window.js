const cards = document.querySelectorAll('.card')

cards.forEach(card => {
    const window = document.querySelector(`.info-window[id="${card.id}"]`);
    const info = new Info(card, window);

    info.addEvent()
});
