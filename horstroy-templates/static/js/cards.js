function ShowCards(entry) {
    let i = 1;
    entry.forEach(change => {
        if (change.isIntersecting) {
            (function(i) {
                window.setTimeout(function () {
                    change.target.classList.add('show');
                }, (i+1)*200);
            }(i));
            i += 1;
        }
    });
}

let options = { threshold: [0.3] };
let observer = new IntersectionObserver(ShowCards, options);
let elements = document.querySelectorAll('.card');
for (var i = 0; i < elements.length; i++) {
    let element = elements[i]
    observer.observe(element)
}
