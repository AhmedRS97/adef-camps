from .account import urlpatterns as accounts_urls
from .session import urlpatterns as sessions_urls
from .track import urlpatterns as tracks_urls
from .space import urlpatterns as spaces_urls
from .timeslot import urlpatterns as timeslots_urls
from .camp import urlpatterns as camps_urls
from .group import urlpatterns as groups_urls


urlpatterns = list()

urlpatterns += accounts_urls
urlpatterns += sessions_urls
urlpatterns += tracks_urls
urlpatterns += spaces_urls
urlpatterns += timeslots_urls
urlpatterns += camps_urls
urlpatterns += groups_urls
