// Copyright (c) 2025, Navneet and contributors
// For license information, please see license.txt



document.addEventListener('DOMContentLoaded', function() {
        fetch('http://van.life:8000/api/v2/method/rentals.api.count_total_drivers')
        .then(response => response.json())
        .then(data => {
            console.log('Fetched data', data);
        })
        .catch(error => {
            console.log("Error", error);
        });
	
});
