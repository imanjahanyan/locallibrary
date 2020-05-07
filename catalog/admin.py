from django.contrib import admin
from . import models

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Information', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


class BooksInstanceInline(admin.TabularInline):
    model = models.BookInstance


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name',     'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(models.Genre)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


# class GenreInline(admin.TabularInline):
#     model = models.Genre


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]



