document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const mobileForm = document.getElementById("mobileForm");
    const otpForm = document.getElementById("otpForm");

    // Login form validation
    if (loginForm) {
        loginForm.addEventListener("submit", function (e) {
            const username = document.getElementById("username").value.trim();
            const password = document.getElementById("password").value.trim();
            if (!username || !password) {
                alert("Please enter both username and password.");
                e.preventDefault();
            }
        });
    }

    // Mobile number validation
    if (mobileForm) {
        mobileForm.addEventListener("submit", function (e) {
            const mobile = document.getElementById("mobile").value.trim();
            const mobileRegex = /^[6-9]\\d{9}$/;
            if (!mobileRegex.test(mobile)) {
                alert("Enter a valid 10-digit Indian mobile number.");
                e.preventDefault();
            }
        });
    }

    // OTP validation
    if (otpForm) {
        otpForm.addEventListener("submit", function (e) {
            const otp = document.getElementById("otp").value.trim();
            if (otp.length < 4 || otp.length > 6) {
                alert("OTP must be 4 to 6 digits.");
                e.preventDefault();
            }
        });
    }
});