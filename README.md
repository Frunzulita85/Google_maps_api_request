# 🌍 Google Maps Places API – Python Project

A simple Python project that uses **Google Maps Places API** to search for locations (restaurants, shops, hotels, etc.) using HTTP requests.

---

## 📌 Features

* Search places by text query
* Get nearby places by coordinates
* Fetch place details (name, rating, address, etc.)
* Easy to extend for Flask / FastAPI / web apps

---

## 🛠 Requirements

* Python 3.8+
* Google Maps API Key with **Places API enabled**

---

## 🔑 Getting a Google Maps API Key

1. Go to **Google Cloud Console** → [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. Create a new **Project**
3. Enable:

   * Places API
   * Maps JavaScript API (optional, for frontend)
4. Go to **APIs & Services → Credentials → Create API Key**
5. Restrict the key to your IP or domain (recommended)

---


## 📊 Example Output

```bash
Restaurant A - 4.6
Restaurant B - 4.3
Restaurant C - 4.7
```



## 📚 Official Documentation

[https://developers.google.com/maps/documentation/places/web-service](https://developers.google.com/maps/documentation/places/web-service)



MIT License
