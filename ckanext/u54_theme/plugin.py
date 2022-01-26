import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
pconfig = toolkit.config
from ckan.common import config
from ckan.lib.app_globals import set_app_global
from ckan.lib.plugins import DefaultTranslation
import ckan.logic as logic
import ckan.lib.helpers as h
from datetime import datetime


class U54ThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        set_app_global('ckan.u54_portal_url',
                   pconfig.get('%s.u54_portal_url' % __name__))

        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'theme')

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'u54_theme_get_last_datasets': lambda: logic.get_action('package_search')({}, {"rows": 8})['results'],
            'u54_theme_get_resource_number': u54_theme_get_resource_number,
            'u54_theme_get_showcase_number': u54_theme_get_showcase_number,
            'u54_theme_get_popular_datasets': lambda: logic.get_action('package_search')({}, {"rows": 4, 'sort': 'views_total desc'})['results'],
            'u54_theme_display_date': u54_theme_display_date,
            'u54_theme_get_map': u54_theme_get_map,
            'u54_theme_get_groups': lambda: logic.get_action('group_list')({}, {"all_fields": True}),
            'u54_theme_spatial_installed': lambda: config.get('ckanext.u54_theme.spatial_installed', 'False'),
            'u54_theme_osmnames_key': lambda: config.get('ckanext.u54_theme.osmnames_key', '')
        }


def u54_theme_display_date(strDate):
    return datetime.strptime(strDate, "%Y-%m-%dT%H:%M:%S.%f").strftime('%d/%m/%Y')


def u54_theme_get_resource_number():
    return logic.get_action('resource_search')({}, {'query': {'name:': ''}})['count']


def u54_theme_get_showcase_number():
    return len(logic.get_action('ckanext_showcase_list')({}, {}))


def u54_theme_get_map(view_id, resource_id, package_id):
    resource_view = None
    try:
        resource_view = logic.get_action('resource_view_show')({}, {'id': view_id})
    except ():
        return 'View not found'

    resource = logic.get_action('resource_show')({}, {'id': resource_id})
    package = logic.get_action('package_show')({}, {'id': package_id})

    return h.rendered_resource_view(resource_view, resource, package, True)
