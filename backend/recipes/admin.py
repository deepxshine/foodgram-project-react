from django.contrib import admin
from recipes.models import (Tag, Recipe, Ingredient, IngredientInRecipe,
                            ShoppingCart, Subscribe, FavoriteRecipe, TagRecipe)


class IngredientsInRecipe(admin.TabularInline):
    model = IngredientInRecipe
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'author', 'get_tags',)
    list_filter = ('author', 'name', 'tags')
    search_fields = ('name',)
    inlines = IngredientsInRecipe,

    # def get_favorites(self, obj):
    #     return obj.favorites.count()
    #
    # # get_favorites.short_description = (
    # #     'Количество лайков'
    # # )

    def get_tags(self, obj):
        return '\n'.join(obj.tags.values_list('name', flat=True))

    get_tags.short_description = 'Теги'


@admin.register(Ingredient)
class Ingredient(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscribe)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'author')
    search_fields = ('user', 'author')
    list_filter = ('user', 'author')


@admin.register(FavoriteRecipe)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')


@admin.register(TagRecipe)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tag', 'recipe')