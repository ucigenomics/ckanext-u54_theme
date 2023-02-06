------------------------
ckanext-u54_theme
------------------------

Requirements
============

This extension is compatible with CKAN 2.9 and higher.


Config Settings
===============

The following configuration variables must be set:

* `ckanext.u54_theme.plugin.u54_url` 
* `ckanext.u54_theme.plugin.u54_portal_url` 
* `ckanext.u54_theme.plugin.u54_ckan_app_id` (CKAN app UUID in u54 portal)


Development Installation
========================

To install ckanext-u54_theme for development, activate your CKAN
virtualenv and do:

    git clone https://github.com/rarsenal/ckanext-u54_theme.git
    cd ckanext-u54_theme
    python setup.py develop
    pip install -r dev-requirements.txt
