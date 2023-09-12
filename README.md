### Foodgram – Продуктовый помощник

Проект для людителей высокой и не очень кухни. Здесь вы можете опубликовать рецепт из бабушкиной поваренной книги или
найти новый рецепт. Понравившиеся рецепты вы можете добавить в избранное и подпсаться на этого кулинара, а если решите
приготовить это блюдо, вы можете добавить все ингредиенты в корзину, а потом скачать список покупок на ваше устройство.

## Данные суперюзера

a@a.ru
a
http://158.160.8.160

## Для запуска проекта
Выполните командды:
```bash
cd ../infra
docker-compose up -d --build
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
```


## Для авторизованных пользователей:

Доступна главная страница.
Доступна страница другого пользователя.
Доступна страница отдельного рецепта.
Доступна страница «Мои подписки».
Можно подписаться и отписаться на странице рецепта.
Можно подписаться и отписаться на странице автора.
При подписке рецепты автора добавляются на страницу «Мои подписки» и удаляются оттуда при отказе от подписки.
Доступна страница «Избранное».
На странице рецепта есть возможность добавить рецепт в список избранного и удалить его оттуда.
На любой странице со списком рецептов есть возможность добавить рецепт в список избранного и удалить его оттуда.
Доступна страница «Список покупок».
На странице рецепта есть возможность добавить рецепт в список покупок и удалить его оттуда.
На любой странице со списком рецептов есть возможность добавить рецепт в список покупок и удалить его оттуда.
Есть возможность выгрузить файл (.txt) с перечнем и количеством необходимых ингредиентов для рецептов из
«Списка покупок».
Ингредиенты в выгружаемом списке не повторяются, корректно подсчитывается общее количество для каждого ингредиента.
Доступна страница «Создать рецепт».
Есть возможность опубликовать свой рецепт.
Есть возможность отредактировать и сохранить изменения в своём рецепте.
Есть возможность удалить свой рецепт.
Доступна и работает форма изменения пароля.
Доступна возможность выйти из системы (разлогиниться).

## Для неавторизованных пользователей

Доступна главная страница.
Доступна страница отдельного рецепта.
Доступна страница любого пользователя.
Доступна и работает форма авторизации.
Доступна и работает система восстановления пароля.
Доступна и работает форма регистрации.

##администратор и админ-зона

Все модели выведены в админ-зону.
Для модели пользователей включена фильтрация по имени и email.
Для модели рецептов включена фильтрация по названию, автору и тегам.
На админ-странице рецепта отображается общее число добавлений этого рецепта в избранное.
Для модели ингредиентов включена фильтрация по названию.
