class Banner {
    constructor(banner) {
        this.banner= banner;
    }

    Execute() {
        var contents = this.banner.querySelectorAll('.banner__content');
        let currentContent = 0;
        let previousContent;

        setInterval(() => {
            previousContent = currentContent
            contents[currentContent].classList.remove('active');
            currentContent = (currentContent + 1) % contents.length;
            contents[currentContent].classList.add('active');
        }, 5000);
    }
}