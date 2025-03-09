//Author:YIBO LIANG
document.getElementById("login-btn").addEventListener("click", async () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:8000/auth/token", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ username, password })
    });

    const data = await response.json();
    if (response.ok) {
        localStorage.setItem("access_token", data.access_token);
        window.location.href = "cities.html";  // Redirect to city list
    } else {
        document.getElementById("output").innerText = "Login failed!";
    }
});
