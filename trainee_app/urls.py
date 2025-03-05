from django.urls import path
from .views import trainee_list

urlpatterns = [
    path('traineelist/', trainee_list, name='trainee_list'),
]


from .views import add_trainee

urlpatterns += [
    path('add/', add_trainee, name='add_trainee'),
]

from django.urls import path
from .views import trainee_list

urlpatterns = [
    path('traineelist/', trainee_list, name='trainee_list'),
]


from .views import add_trainee

urlpatterns += [
    path('add/', add_trainee, name='add_trainee'),
]

from .views import update_trainee

urlpatterns += [
    path('update/<int:trainee_id>/', update_trainee, name='update_trainee'),
]

from .views import delete_trainee

urlpatterns += [
    path('delete/<int:trainee_id>/', delete_trainee, name='delete_trainee'),
]
