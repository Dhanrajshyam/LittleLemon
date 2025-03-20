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

    // booking form submission
    const booking_form = document.getElementById("booking_form");
    
    booking_form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission
        
        const formData = new FormData(booking_form);
        const data = Object.fromEntries(formData.entries());

        fetch("/api/booking", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                alert("Booking successful! Your reservation is confirmed.");
                form.reset(); // Clear the form after successful submission
            } else {
                alert("Booking failed: " + (result.error || "Please try again."));
            }
        })
        .catch(error => {
            alert("Error submitting booking. Please check your internet connection and try again.");
            console.error("Booking Error:", error);
        });
    });

    // Get available slots for the selected booking date
    const dateInput = document.getElementById("date");
    const slotsSelect = document.getElementById("slots");
    // Fetch available slots when the booking date changes
    dateInput.addEventListener("change", function () {
        const selectedDate = dateInput.value;
        if (!selectedDate) return;

        fetch(`/api/booking/available_slots?date=${selectedDate}`)
            .then(response => response.json())
            .then(data => {
                slotsSelect.innerHTML = ""; // Clear previous options
                if (data.slots && data.slots.length > 0) {
                    data.slots.forEach(slot => {
                        const option = document.createElement("option");
                        option.value = slot;
                        option.textContent = `Slot ${slot}`;
                        slotsSelect.appendChild(option);
                    });
                } else {
                    const option = document.createElement("option");
                    option.textContent = "No slots available";
                    option.disabled = true;
                    slotsSelect.appendChild(option);
                }
            })
            .catch(error => {
                console.error("Error fetching available slots:", error);
            });
    });
    
});

