from zope.component import getMultiAdapter
from Products.Five.browser import BrowserView

from plone.memoize.ram import cache

JS_TEMPLATE = '''
$(document).ready(function () {
    jarn.i18n.loadCatalog('eea.tags', '%(lang)s');
    _ = jarn.i18n.MessageFactory('eea.tags')
});
'''

def cache_key(fun, self, language):
    return language

class I18NJavascript(BrowserView):

    def __call__(self, *args, **kwargs):
        pps = getMultiAdapter((self.context, self.request), 
                              name='plone_portal_state')

        language = pps.language()
        return self.cooked_javascript(language)

    @cache(cache_key)
    def cooked_javascript(self, language):
        return JS_TEMPLATE % {'lang': language}