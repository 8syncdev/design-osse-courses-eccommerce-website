from django.shortcuts import redirect

def error_404_view(request, exception):
    # print('Error 404')
    return redirect('/admin/login/')