from django.conf import settings

def global_variables(request):
    image_url = settings.STATIC_URL + "media/acessories-generatoes.jpeg"  # Replace with your image path
    absolute_image_url = request.build_absolute_uri(image_url)
    return {
        'ABSOLUTE_IMAGE_URL': absolute_image_url,
    }