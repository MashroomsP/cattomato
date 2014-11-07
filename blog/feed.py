from django.contrib.syndication.views import Feed
from .models import Entry


class LatestPosts(Feed):
    title = "Cattomato"
    link = "/feed/"
    description = "Latest Posts of Cattomato"

    def items(self):
        return Entry.objects.published()[:5]
