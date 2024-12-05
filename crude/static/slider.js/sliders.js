const slides = document.querySelectorAll('.slide');
let index = 0;

function showSlides() {
    slides.forEach((slide, i) => {
        slide.style.display = i === index ? 'block' : 'none';
    });
    index = (index + 1) % slides.length;
}

setInterval(showSlides, 5000);
showSlides();
