document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('hamburger').onclick = function() {
        document.getElementById('navLinks').classList.toggle('active');
    };
});