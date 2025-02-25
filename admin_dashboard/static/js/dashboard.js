// JavaScript untuk fungsi Dashboard

document.addEventListener('DOMContentLoaded', function() {
    // Toggle sidebar di mobile
    const sidebarToggle = document.querySelector('#sidebarToggle');
    
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            document.querySelector('#sidebar').classList.toggle('collapse');
        });
    }
    
    // Contoh kode untuk menampilkan data dari API
    function fetchDataFromAPI() {
        // Fetch data dari backend API
        // Kode ini perlu disesuaikan dengan endpoint API yang sebenarnya
        fetch('https://api-backend-url/data')
            .then(response => response.json())
            .then(data => {
                console.log('Data dari API:', data);
                // Tampilkan data di dashboard
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }
    
    // Panggil fungsi fetch data jika diperlukan
    // fetchDataFromAPI();
});