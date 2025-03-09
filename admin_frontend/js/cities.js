// Author: YIBO LIANG

document.addEventListener("DOMContentLoaded", function () {
    // 如果页面中存在城市列表，则调用 fetchCities()
    if (document.getElementById("city-list")) {
        fetchCities();
    }
    // 如果页面中存在添加城市的表单，则注册表单提交事件
    if (document.getElementById("add-city-form")) {
        document.getElementById("add-city-form").addEventListener("submit", addCity);
    }
});

// 显示所有城市的功能
async function fetchCities() {
    const token = localStorage.getItem("access_token");
    console.log("Token:", token);

    try {
        const response = await fetch("http://127.0.0.1:8000/cities", {
            headers: { "Authorization": `Bearer ${token}` }
        });

        if (!response.ok) {
            throw new Error("Failed to fetch cities");
        }

        const cities = await response.json();
        const cityList = document.getElementById("city-list");
        cityList.innerHTML = "";

        cities.forEach(city => {
            const li = document.createElement("li");
            
            // 如果有图片，则在城市名称前显示
            if (city.image_url) {
                const img = document.createElement("img");
                img.src = city.image_url;
                img.alt = city.name;
                img.style.width = "100px";
                img.style.marginRight = "10px";
                li.appendChild(img);
            }

            const cityText = document.createElement("span");
            cityText.innerText = city.name;
            cityText.style.cursor = "pointer";
            cityText.addEventListener("click", () => {
                // 每次点击城市时，存储最新的城市 ID
                localStorage.setItem("selected_city_id", city.id);
                console.log("Selected city ID set to:", localStorage.getItem("selected_city_id"));
                window.location.href = "locations.html";
            });
            li.appendChild(cityText);

            cityList.appendChild(li);
        });

    } catch (error) {
        console.error("Error fetching cities:", error);
        alert("❌ Failed to load cities.");
    }
}

// 添加城市（支持图片上传）的功能
async function addCity(event) {
    event.preventDefault(); // 阻止表单默认提交

    const token = localStorage.getItem("access_token");
    if (!token) {
        alert("Please login first!");
        window.location.href = "index.html";
        return;
    }

    // 使用 FormData 来提交 multipart/form-data 数据（文本和文件）
    const formData = new FormData();
    formData.append("name", document.getElementById("cityName").value);
    formData.append("description", document.getElementById("cityDescription").value);

    // 获取文件上传的 input（可选）
    const fileInput = document.getElementById("cityImage");
    if (fileInput && fileInput.files.length > 0) {
        formData.append("file", fileInput.files[0]);
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/add_city/", {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${token}` // 认证信息
            },
            body: formData // 直接传输 FormData，浏览器会自动设置 Content-Type
        });

        const data = await response.json();
        document.getElementById("output").innerText = data.message;
        if (data.image_url) {
            console.log("Uploaded image URL:", data.image_url);
        }
        alert("✅ City added successfully!");
        window.location.href = "cities.html"; // 添加成功后跳转回城市列表

    } catch (error) {
        console.error("Error adding city:", error);
        alert("❌ Error adding city: " + error);
    }
}
