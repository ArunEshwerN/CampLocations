document.addEventListener('DOMContentLoaded', () => {
    // Smooth Scrolling for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Lazy Loading Images
    document.querySelectorAll('img[data-src]').forEach(img => {
        img.setAttribute('src', img.getAttribute('data-src'));
        img.onload = () => img.removeAttribute('data-src');
    });
});
