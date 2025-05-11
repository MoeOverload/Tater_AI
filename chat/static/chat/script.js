



document.addEventListener('DOMContentLoaded', () => {
    // Scroll logic
    const anchor = document.getElementById("bottom-anchor");
    anchor?.scrollIntoView({ behavior: "smooth" });

    // Toggle logic
    const sectionToggles = document.querySelectorAll('.section-toggle');
    sectionToggles.forEach(toggle => {
        toggle.addEventListener('click', (event) => {
            const btn = event.currentTarget;
            const sectionContent = btn.nextElementSibling;
            const expanded = btn.getAttribute('aria-expanded') === 'true';
            sectionContent.hidden = expanded;
            btn.setAttribute('aria-expanded', String(!expanded));
        });
    });
    
});
