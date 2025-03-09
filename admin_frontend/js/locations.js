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
    // Get the selected city ID from local storage
    const cityId = localStorage.getItem("selected_city_id");
    if (!cityId) {
        alert("❌ No city selected! Redirecting to city list.");
        window.location.href = "cities.html";
        return;
    }
    
    // Retrieve form values
    const name = document.getElementById("locationName").value;
    const description = document.getElementById("locationDescription").value;
    const latitude = document.getElementById("latitude").value;
    const longitude = document.getElementById("longitude").value;
    
    // Basic form validation
    if (!name || !description || !latitude || !longitude) {
        alert("Please fill out all required fields.");
        return;
    }
    
    // Prepare location_data object
    const locationData = {
        latitude: parseFloat(latitude),
        longitude: parseFloat(longitude)
    };
    
    try {
        const response = await fetch("http://127.0.0.1:8000/add_location/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify({
                city_id: cityId,
                name: name,
                description: description,
                location_data: locationData
            })
        });
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || "Failed to add location");
        }
        const data = await response.json();
        alert(data.message);
        window.location.href = "locations.html"; // Redirect back to locations page after adding
    } catch (error) {
        console.error("Error adding location:", error);
        alert("❌ Error adding location: " + error.message);
    }
}


// -------------------- Called when the page loads --------------------
const selectedCityId = localStorage.getItem("selected_city_id");
if (selectedCityId) {
    fetchCityDetails();  // Loading city information
    fetchLocations();    // Load locations for this city
} else {
    alert("❌ No city selected. Redirecting to city list.");
    window.location.href = "cities.html";
}

