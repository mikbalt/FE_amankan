import requests
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Fungsi untuk berinteraksi dengan API backend
def call_api(url, method='GET', data=None, token=None):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    
    api_url = f"http://localhost:8000/api/{url}"  # Sesuaikan dengan URL API backend
    
    try:
        if method == 'GET':
            response = requests.get(api_url, headers=headers)
        elif method == 'POST':
            response = requests.post(api_url, data=json.dumps(data), headers=headers)
        elif method == 'PUT':
            response = requests.put(api_url, data=json.dumps(data), headers=headers)
        elif method == 'DELETE':
            response = requests.delete(api_url, headers=headers)
        
        return response.json(), response.status_code
    except Exception as e:
        return {'error': str(e)}, 500

# # View untuk halaman login
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Kirim request ke API backend untuk login
        data = {'email': username, 'password': password}
        response_data, status_code = call_api('auth/login/', method='POST', data=data)
        
        if status_code == 200 and 'access' in response_data:
            # Simpan token di session
            request.session['auth_token'] = response_data['access']
            request.session['user_info'] = {
                'username': username,
                'id': response_data.get('id'),
            }
            return redirect('home')
        else:
            error_message = response_data.get('error', 'Login gagal. Periksa username dan password Anda.')
            return render(request, 'dashboard/login.html', {'error_message': error_message})
    
    return render(request, 'dashboard/login.html')

# View untuk halaman home/dashboard
def home_view(request):
    # Cek apakah user sudah login
    if 'auth_token' not in request.session:
        return redirect('login')
    
    # Contoh pengambilan data dari API backend
    token = request.session['auth_token']
    user_info = request.session['user_info']
    
    # Ambil data untuk dashboard dari API
    # data, status_code = call_api('dashboard/data/', token=token)
    
    # Untuk contoh, kita gunakan data dummy saja
    context = {
        'user': user_info,
        # 'dashboard_data': data if status_code == 200 else {}
    }
    
    return render(request, 'dashboard/home.html', context)

# View untuk logout
def logout_view(request):
    # Hapus token dari session
    if 'auth_token' in request.session:
        del request.session['auth_token']
    if 'user_info' in request.session:
        del request.session['user_info']
    
    return redirect('login')