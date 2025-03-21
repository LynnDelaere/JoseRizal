//Author:YIBO LIANG

const token = localStorage.getItem("access_token");
console.log("Token:", token);
if (!token) {
    alert("Please login first!");
    window.location.href = "index.html";
}

// -------------------- Get city information --------------------
async function fetchCityDetails() {
    // Dynamically get the latest selected_city_id each time you call
    const cityId = localStorage.getItem("selected_city_id");
    console.log("Fetching city details for cityId:", cityId);
    if (!cityId) {
        alert("❌ No city selected. Redirecting to city list.");
        window.location.href = "cities.html";
        return;
    }
    try {
        const response = await fetch(`http://127.0.0.1:8000/city/${cityId}`, {
            headers: { "Authorization": `Bearer ${token}` }
        });
        if (!response.ok) {
            throw new Error("❌ City not found!");
        }
        const city = await response.json();
        document.getElementById("city-name").innerText = city.name;
        document.getElementById("city-description").innerText = city.description;
        

        const cityImage = document.getElementById("city-image");
        if (city.image_url) {
            cityImage.src = city.image_url;
            cityImage.style.display = "block";
        } else {
            cityImage.style.display = "none";
        }

    } catch (error) {
        console.error("Error fetching city details:", error);
        alert("❌ Failed to load city details.");
    }
}

// -------------------- list of Location --------------------
async function fetchLocations() {
    // Dynamically obtain the latest selected_city_id
    const cityId = localStorage.getItem("selected_city_id");
    console.log("Fetching locations for cityId:", cityId);
    if (!cityId) {
        alert("❌ City ID is missing! Redirecting...");
        window.location.href = "cities.html";
        return;
    }
    try {
        const response = await fetch(`http://127.0.0.1:8000/city/${cityId}/locations`, {
            headers: { "Authorization": `Bearer ${token}` }
        });
        if (!response.ok) {
            throw new Error(`HTTP Error! Status: ${response.status}`);
        }
        const locations = await response.json();
        const locationList = document.getElementById("location-list");
        locationList.innerHTML = ""; 

        locations.forEach(location => {
            const li = document.createElement("li");
            li.innerText = `${location.name} (City ID: ${location.city_id})`;
            li.addEventListener("click", () => {
                localStorage.setItem("selected_location_id", location.id);
                window.location.href = "media.html"; // Jump to Media page
            });
            // delete button
            const deleteBtn = document.createElement("button");
            deleteBtn.innerText = "❌ Delete";
            deleteBtn.style.marginLeft = "10px";
            deleteBtn.addEventListener("click", (event) => {
                event.stopPropagation();
                deleteLocation(location.id);
            });
            li.appendChild(deleteBtn);
            locationList.appendChild(li);
        });
    } catch (error) {
        console.error("Error fetching locations:", error);
        alert("❌ Failed to load locations.");
    }
}

// -------------------- delete Location --------------------
async function deleteLocation(location_id) {
    if (!confirm("Are you sure you want to delete this location?")) return;
    try {
        const response = await fetch(`http://127.0.0.1:8000/delete_location/${location_id}`, {
            method: "DELETE",
            headers: { "Authorization": `Bearer ${token}` }
        });
        const data = await response.json();
        alert(data.message);
        fetchLocations(); // Reload list after deletion
    } catch (error) {
        alert("❌ Error deleting location: " + error);
    }
}


// -------------------- Add Location --------------------
async function addLocation() {
<<<<<<< HEAD
    // Get the selected city ID from local storage
=======
    // 获取本地存储的选定城市 ID
>>>>>>> 70572b9 (Add database, backend, and admin_frontend folders)
    const cityId = localStorage.getItem("selected_city_id");
    if (!cityId) {
        alert("❌ No city selected! Redirecting to city list.");
        window.location.href = "cities.html";
        return;
    }
<<<<<<< HEAD
    
    // Retrieve form values
=======

    // 获取表单数据
>>>>>>> 70572b9 (Add database, backend, and admin_frontend folders)
    const name = document.getElementById("locationName").value;
    const description = document.getElementById("locationDescription").value;
    const latitude = document.getElementById("latitude").value;
    const longitude = document.getElementById("longitude").value;
<<<<<<< HEAD
    
    // Basic form validation
    if (!name || !description || !latitude || !longitude) {
        alert("Please fill out all required fields.");
        return;
    }
    
    // Prepare location_data object
=======

    // 确保用户已经在地图上选择了一个位置
    if (!latitude || !longitude) {
        alert("❌ Please select a location on the map!");
        return;
    }

    // 构造 JSON 数据
>>>>>>> 70572b9 (Add database, backend, and admin_frontend folders)
    const locationData = {
        latitude: parseFloat(latitude),
        longitude: parseFloat(longitude)
    };
<<<<<<< HEAD
    
=======

    const data = {
        city_id: parseInt(cityId),  // 确保 city_id 是整数
        name: name,
        description: description,
        location_data: locationData
    };

>>>>>>> 70572b9 (Add database, backend, and admin_frontend folders)
    try {
        const response = await fetch("http://127.0.0.1:8000/add_location/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
<<<<<<< HEAD
            body: JSON.stringify({
                city_id: cityId,
                name: name,
                description: description,
                location_data: locationData
            })
        });
=======
            body: JSON.stringify(data)
        });

>>>>>>> 70572b9 (Add database, backend, and admin_frontend folders)
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || "Failed to add location");
        }
<<<<<<< HEAD
        const data = await response.json();
        alert(data.message);
        window.location.href = "locations.html"; // Redirect back to locations page after adding
=======

        const result = await response.json();
        alert(result.message);
        window.location.href = "locations.html"; // 跳转到地点列表页面
>>>>>>> 70572b9 (Add database, backend, and admin_frontend folders)
    } catch (error) {
        console.error("Error adding location:", error);
        alert("❌ Error adding location: " + error.message);
    }
}

<<<<<<< HEAD
=======
let map;
let marker;

function initMap() {
    const defaultCenter = { lat: 51.0543, lng: 3.7174 }; // 根特, 比利时

    map = new google.maps.Map(document.getElementById("map"), {
        center: defaultCenter,
        zoom: 12
    });

    // 监听用户点击地图，设置标记并填充坐标
    map.addListener("click", (event) => {
        placeMarker(event.latLng);
    });
}

function placeMarker(location) {
    if (marker) {
        marker.setPosition(location);
    } else {
        marker = new google.maps.Marker({
            position: location,
            map: map,
        });
    }

    // 将选定的坐标填充到输入框（隐藏字段）
    document.getElementById("latitude").value = location.lat();
    document.getElementById("longitude").value = location.lng();

    // 更新显示区域（如果需要显示当前选中坐标）
    document.getElementById("selectedCoords").innerText =
        "Selected Coordinates: (" + location.lat().toFixed(6) + ", " + location.lng().toFixed(6) + ")";
}

document.addEventListener("DOMContentLoaded", function() {
    const selectBtn = document.getElementById("selectOnMapBtn");
    if (selectBtn) {
      selectBtn.addEventListener("click", function () {
        const mapDiv = document.getElementById("map");
        // 切换地图显示状态
        if (mapDiv.style.display === "none" || mapDiv.style.display === "") {
          mapDiv.style.display = "block";
          // 如果地图还没有初始化，则调用 initMap()；否则，触发 resize 事件确保地图正确显示
          if (!map) {
            initMap();
          } else {
            google.maps.event.trigger(map, "resize");
          }
        } else {
          mapDiv.style.display = "none";
        }
      });
    } else {
      console.error("Element with id 'selectOnMapBtn' not found.");
    }
  });

>>>>>>> 70572b9 (Add database, backend, and admin_frontend folders)

// -------------------- Called when the page loads --------------------
const selectedCityId = localStorage.getItem("selected_city_id");
if (selectedCityId) {
    fetchCityDetails();  // Loading city information
    fetchLocations();    // Load locations for this city
} else {
    alert("❌ No city selected. Redirecting to city list.");
    window.location.href = "cities.html";
}

