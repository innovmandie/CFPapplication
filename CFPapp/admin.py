from django.contrib import admin
from .models import PostA1_C1, PostA1_C2, PostA1_C3, PostA2_C1, PostA2_C2, PostA2_C3, PostB1_C1, PostB1_C2, PostB1_C3, Utilisateur_infos
from .models import Post


#admin.site.register(Utilisateur)
admin.site.register(Post)
admin.site.register(Utilisateur_infos)
admin.site.register(PostA1_C1)
admin.site.register(PostA1_C2)
admin.site.register(PostA1_C3)
admin.site.register(PostA2_C1)
admin.site.register(PostA2_C2)
admin.site.register(PostA2_C3)
admin.site.register(PostB1_C1)
admin.site.register(PostB1_C2)
admin.site.register(PostB1_C3)