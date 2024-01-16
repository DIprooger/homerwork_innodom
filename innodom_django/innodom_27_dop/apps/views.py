from django.shortcuts import render


def home_page(request):
    return render(
        request=request,
        template_name='base.html'
    )


def contact_page(request):
    return render(
        request=request,
        template_name='child.html'
    )


def main(request):
    return render(
        request=request,
        template_name='main.html'
    )


def page1(request):
    return render(
        request=request,
        template_name='page1.html'
    )


def page2(request):
    return render(
        request=request,
        template_name='page2.html'
    )
