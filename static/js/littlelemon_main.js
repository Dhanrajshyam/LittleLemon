document.addEventListener("DOMContentLoaded", function () {
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector(".navbar-collapse");
    const navLinks = document.querySelectorAll(".nav-link");

    // Toggle the menu when clicking the navbar toggler
    navbarToggler.addEventListener("click", function () {
        navbarCollapse.classList.toggle("show");
    });

    // Close the menu when clicking outside of it
    document.addEventListener("click", function (event) {
        if (!navbarCollapse.contains(event.target) && !navbarToggler.contains(event.target)) {
            navbarCollapse.classList.remove("show");
        }
    });

    // Close the menu when clicking on a navigation link
    navLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            navbarCollapse.classList.remove("show");
        });
    });
    
});

