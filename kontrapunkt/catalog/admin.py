from django.contrib import admin


from .models import Country
admin.site.register(Country)

from .models import Composer
admin.site.register(Composer)

from .models import CompositionCategory
admin.site.register(CompositionCategory)

from .models import Composition
admin.site.register(Composition)

from .models import Collection
admin.site.register(Collection)

from .models import Piece
admin.site.register(Piece)

from .models import PieceInstance
admin.site.register(PieceInstance)


# # Define the admin class
# class ComposerAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] # Affets detail view
#     
# # Register the admin class with the associated model
# admin.site.register(Composer, ComposerAdmin)
