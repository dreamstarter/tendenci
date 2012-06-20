from rss.feedsmanager import SubFeed
from site_settings.utils import get_setting
from perms.utils import PUBLIC_FILTER
from sitemaps import TendenciSitemap

from chamberlin_projects.models import Project

class LatestEntriesFeed(SubFeed):
    title =  '%s Latest Projects' % get_setting('site','global','sitedisplayname')
    link =  "/chamberlin_projects/"
    description =  "Latest Projects by %s" % get_setting('site','global','sitedisplayname')

    def items(self):
        items = Project.objects.filter(**PUBLIC_FILTER).order_by('-create_dt')[:20]
        return items

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.project_description

    def item_pubdate(self, item):
        return item.create_dt

    def item_link(self, item):
        return item.get_absolute_url()

class ProjectSitemap(TendenciSitemap):
    """ Sitemap information for chamberlin_projects """
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        items = Project.objects.filter(**PUBLIC_FILTER).order_by('-create_dt')
        return items

    def lastmod(self, obj):
        return obj.create_dt
