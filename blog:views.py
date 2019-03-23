from django.shortcuts import render

# Create your views here.
# Wendy Griffin
def post_list(request):
    return render(request, 'blog/post_list.html', {})
