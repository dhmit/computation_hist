from django.shortcuts import redirect


def redirect_view(request):
    response = redirect('/dj_comp_hist/')
    return response
