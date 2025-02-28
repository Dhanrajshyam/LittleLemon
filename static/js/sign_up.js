document.addEventListener("DOMContentLoaded", function () {
    const passwordField = document.getElementById("password");
    const confirmPasswordField = document.getElementById("confirm_password");
    const passwordRules = document.getElementById("password-rules");
    const passwordMatchRule = document.getElementById("password-match-rule");

    const lengthRule = document.getElementById("length");
    const capital = document.getElementById("capital");
    const small = document.getElementById("small");
    const number = document.getElementById("number");
    const special = document.getElementById("special");
    const passwordMatch = document.getElementById("password-match");

    const specialChars = /[!@#$%^&*]/;
    const uppercase = /[A-Z]/;
    const lowercase = /[a-z]/;
    const digit = /[0-9]/;

    passwordField.addEventListener("focus", function () {
        passwordRules.style.display = "block";
    });

    passwordField.addEventListener("blur", function () {
        setTimeout(() => passwordRules.style.display = "none", 200);
    });

    passwordField.addEventListener("input", function () {
        let password = passwordField.value;

        validateRule(password.length >= 8 && password.length <= 16, lengthRule);
        validateRule(uppercase.test(password), capital);
        validateRule(lowercase.test(password), small);
        validateRule(digit.test(password), number);
        validateRule(specialChars.test(password), special);
    });

    confirmPasswordField.addEventListener("focus", function () {
        passwordMatchRule.style.display = "block";
    });

    confirmPasswordField.addEventListener("blur", function () {
        setTimeout(() => passwordMatchRule.style.display = "none", 200);
    });

    confirmPasswordField.addEventListener("input", function () {
        let password = passwordField.value;
        let confirm_password = confirmPasswordField.value;

        validateRule(password === confirm_password, passwordMatch);
    });

    function validateRule(condition, element) {
        if (condition) {
            element.classList.remove("invalid");
            element.classList.add("valid");
        } else {
            element.classList.remove("valid");
            element.classList.add("invalid");
        }
    }
});
