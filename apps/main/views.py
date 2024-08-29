from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from .models import AboutUs
from .froms import ContactUsForm
from ..post.models import Post
# Create your views here.

class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['posts'] = Post.objects.order_by('-created_at')[:3]
         return context


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['about_us'] = AboutUs.objects.all()
         return context

class ContactUsView(CreateView):  #CreateView
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = '/'

    # def form_valid(self, form):
    #     form.send_email()
    #     return super().form_valid(form)


# class SearchView(ListView):
#     template_name = 'pages/post_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         query = self.request.GET.get('q')
#         if query:
#             context['posts'] = Post.objects.filter(title__icontains=query)
#         else:
#             context['posts'] = Post.objects.none()
#         return context




























