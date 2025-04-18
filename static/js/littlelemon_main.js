document.addEventListener("DOMContentLoaded", function () {
    // Elements
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector(".navbar-collapse");
    const navLinks = document.querySelectorAll(".nav-link");
    const bookingForm = document.getElementById("booking_form");
    const durationButtons = document.querySelectorAll(".duration-btn");
    const bookingDateInput = document.getElementById("booking_date");
    const branchSelect = document.getElementById("branch");
    const startTimeDisplay = document.getElementById("start_time_display");
    const endTimeDisplay = document.getElementById("end_time_display");
    const endTimeHidden = document.getElementById("end_time");
    const bookingContainer = document.getElementById("booking-container");
    const pagination = document.getElementById("pagination");
    const searchInput = document.getElementById("search_booking");

    // Set min date
    bookingDateInput.min = new Date().toISOString().split("T")[0];

    // Navbar toggle logic
    navbarToggler?.addEventListener("click", () => navbarCollapse.classList.toggle("show"));
    document.addEventListener("click", function (event) {
        if (!navbarCollapse.contains(event.target) && !navbarToggler.contains(event.target)) {
            navbarCollapse.classList.remove("show");
        }
    });
    navLinks.forEach(link => link.addEventListener("click", () => navbarCollapse.classList.remove("show")));

    // Utilities
    const pad = num => String(num).padStart(2, '0');
    const format12hr = date => {
        let hours = date.getHours();
        const minutes = pad(date.getMinutes());
        const ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12 || 12;
        return `${hours}:${minutes} ${ampm}`;
    };
    const formatTime = timeStr => {
        const [h, m] = timeStr.split(':').map(Number);
        const date = new Date();
        date.setHours(h, m);
        return format12hr(date);
    };
    const getCSRFToken = () => document.cookie.match('(^|;)\\s*csrftoken\\s*=\\s*([^;]+)')?.pop() || '';
    const getMonthName = num => new Date(2000, num, 1).toLocaleString('default', { month: 'short' });

    // Time picker state
    let selectedStartTime = null;
    let selectedDuration = 30;
    const defaultWorkingHours = { opening_time: "10:00", closing_time: "22:00" };
    let openingTime = defaultWorkingHours.opening_time;
    let closingTime = defaultWorkingHours.closing_time;
    const branch = branchSelect?.value || "Vellore";

    function calculateMaxStartTime(closingTimeStr, durationMins) {
        const [hh, mm] = closingTimeStr.split(":").map(Number);
        const closingDate = new Date();
        closingDate.setHours(hh);
        closingDate.setMinutes(mm - durationMins);
        return `${pad(closingDate.getHours())}:${pad(closingDate.getMinutes())}`;
    }

    // Initialize Flatpickr
    const startTimePicker = flatpickr(startTimeDisplay, {
        enableTime: true,
        noCalendar: true,
        dateFormat: "h:i K",
        time_24hr: false,
        minuteIncrement: 30,
        minTime: openingTime,
        maxTime: calculateMaxStartTime(closingTime, selectedDuration),
        clickOpens: true,
        allowInput: false,
        onChange: function (selectedDates) {
            if (selectedDates.length > 0) {
                selectedStartTime = selectedDates[0];
                document.getElementById("start_time").value = `${pad(selectedStartTime.getHours())}:${pad(selectedStartTime.getMinutes())}`;
                updateEndTime();
            }
        }
    });

    function updateTimePickerLimits() {
        startTimePicker.set("minTime", openingTime);
        startTimePicker.set("maxTime", calculateMaxStartTime(closingTime, selectedDuration));
    }

    function updateEndTime() {
        if (!selectedStartTime || !selectedDuration) return;
        const end = new Date(selectedStartTime.getTime() + selectedDuration * 60000);
        endTimeDisplay.value = format12hr(end);
        endTimeHidden.value = `${pad(end.getHours())}:${pad(end.getMinutes())}`;
    }

    durationButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            selectedDuration = parseInt(btn.dataset.duration);
            durationButtons.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            updateEndTime();
            updateTimePickerLimits();
        });
    });

    async function fetchWorkingHours() {
        try {
            const response = await fetch(`/api/booking/working_hours?branch=${branch}`);
            if (!response.ok) throw new Error("API Error");
            const data = await response.json();
            openingTime = data.opening_time || defaultWorkingHours.opening_time;
            closingTime = data.closing_time || defaultWorkingHours.closing_time;
        } catch (err) {
            console.warn("Failed to fetch working hours. Using default.", err);
            openingTime = defaultWorkingHours.opening_time;
            closingTime = defaultWorkingHours.closing_time;
        } finally {
            updateTimePickerLimits();
        }
    }

    // Trigger fetch on page load and branch change
    fetchWorkingHours();
    branchSelect?.addEventListener("change", () => {
        openingTime = defaultWorkingHours.opening_time;
        closingTime = defaultWorkingHours.closing_time;
        fetchWorkingHours();
    });

    // Handle booking form submission
    bookingForm?.addEventListener("submit", async function (e) {
        e.preventDefault();
        const formData = new FormData(bookingForm);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch("/api/booking", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                body: JSON.stringify(data),
            });

            if (response.status === 401) {
                alert("Please login to make a booking.");
                window.location.href = `/login?next=${encodeURIComponent(location.pathname)}`;
                return;
            }

            const result = await response.json();
            if (result.status?.toLowerCase() === "booked") {
                alert(`Booking successful!\nName: ${result.name}\nDate: ${result.booking_date}\nFrom ${result.start_time} to ${result.end_time}`);
                bookingForm.reset();
                endTimeDisplay.value = "";
                durationButtons.forEach(b => b.classList.remove("active"));
                fetchBookings();
            } else {
                alert("Booking failed: " + (result.error || "Please try again."));
            }
        } catch (err) {
            console.error("Booking error:", err);
            alert("Something went wrong. Please try again.");
        }
    });

    // Booking list with search and pagination
    let currentPage = 1;
    const pageSize = 5;
    let allBookings = [];

    async function fetchBookings(page = 1) {
        try {
            const res = await fetch("/api/booking");
            if (!res.ok) throw new Error("Failed to fetch bookings.");
            const data = await res.json();
            allBookings = data.results || [];
            currentPage = page;
            renderBookings();
        } catch (err) {
            console.error("Fetch bookings failed:", err);
            bookingContainer.innerHTML = `<p class="text-danger">Error loading bookings. Please sign in and Try Again</p>`;
        }
    }

    function renderBookings() {
        const keyword = searchInput.value.trim().toLowerCase();
        allBookings.sort((a, b) => new Date(b.booking_date) - new Date(a.booking_date));
        const filtered = allBookings.filter(b =>
            b.name?.toLowerCase().includes(keyword) ||
            b.email?.toLowerCase().includes(keyword) ||
            b.phone?.includes(keyword)
        );

        const totalPages = Math.ceil(filtered.length / pageSize);
        const start = (currentPage - 1) * pageSize;
        const paginated = filtered.slice(start, start + pageSize);

        bookingContainer.innerHTML = paginated.length === 0
            ? `<p>No bookings found.</p>`
            : paginated.map(b => {
                if (!b.booking_date?.includes("-")) return "";
                const [yyyy, mm, dd] = b.booking_date.split("-");
                const statusClass = b.status.toLowerCase();
                const formattedDate = `${dd}-${getMonthName(parseInt(mm) - 1)}-${yyyy}`;
                return `
                    <div class="ticket-card ${statusClass}">
                        <div class="ticket-date">
                            <h1>${dd}</h1>
                            <span>${getMonthName(parseInt(mm) - 1)}</span>
                        </div>
                        <div class="ticket-details">
                            <h2>${b.name}</h2>
                            <p><i class="fa fa-calendar"></i> ${formattedDate}</p>
                            <p><i class="fa fa-clock-o"></i> ${formatTime(b.start_time)} - ${formatTime(b.end_time)}</p>
                            <p><i class="fa fa-heart-o"></i> ${b.no_of_guests} Guests</p>
                            <p><i class="fa fa-phone"></i> +91-${b.phone}</p>
                            <button class="ticket-button">${statusClass.charAt(0).toUpperCase() + statusClass.slice(1)}</button>
                        </div>
                    </div>
                `;
            }).join("");

        renderPagination(totalPages);
    }

    function renderPagination(totalPages) {
        pagination.innerHTML = "";
        if (totalPages <= 1) return;

        for (let i = 1; i <= totalPages; i++) {
            const li = document.createElement("li");
            li.className = `page-item ${i === currentPage ? "active" : ""}`;
            li.innerHTML = `<a class="page-link" href="#">${i}</a>`;
            li.addEventListener("click", e => {
                e.preventDefault();
                currentPage = i;
                renderBookings();
            });
            pagination.appendChild(li);
        }
    }

    let searchTimeout = null;
    searchInput?.addEventListener("input", () => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => fetchBookings(1), 300);
    });

    fetchBookings();
});
