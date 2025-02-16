const apiKey = "038e45e1170c1161db236f50c6162dba"; 

async function getWeather() {
    const city = document.getElementById("city-input").value; 
    if (!city) {
        alert("Please enter a city name");
        return;
    }
    
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("City not found");
        
        const data = await response.json();
        displayWeather(data);
    } catch (error) {
        alert(error.message);
    }
}

function displayWeather(data) {
    const cityName = data.name;
    const temperature = Math.round(data.main.temp) + "°C";
    const weatherCondition = data.weather[0].main;

    document.getElementById("cityName").textContent = cityName;
    document.getElementById("temperature").textContent = temperature;
    document.getElementById("condition").textContent = weatherCondition;

    const weatherIcon = document.getElementById("weatherIcon");
    const iconCode = data.weather[0].icon;
    weatherIcon.src = `https://openweathermap.org/img/wn/${iconCode}@2x.png`;

    document.getElementById("weather-info").style.display = "block";
}
