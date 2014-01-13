try:
    import json
except ImportError:
    import simplejson as json

from zope.component import queryUtility
from zope.publisher.browser import BrowserView

from plone.registry.interfaces import IRegistry

from Products.CMFCore.utils import getToolByName

class TemplateList(BrowserView):
    
    def __call__(self):
        
        self.request.response.setHeader('Content-Type', 'text/javascript')
        
        registry = queryUtility(IRegistry)
        templates = []
        
        if registry is not None:
            templateDirectories = registry.get('collective.tinymcetemplates.templateLocations', None)
            if templateDirectories:
                
                portal_catalog = getToolByName(self.context, 'portal_catalog')
                portal_url = getToolByName(self.context, 'portal_url')
                
                portal_path = '/'.join(portal_url.getPortalObject().getPhysicalPath())
                paths = []
                for p in templateDirectories:
                    if p.startswith('/'):
                        p = p[1:]
                    paths.append("%s/%s" % (portal_path, p,))
                
                for r in portal_catalog(path=paths, portal_type="Document"):
                    item = r.getObject()
                    templates.append([r.Title, item.getText() if hasattr(item, 'getText') else item.text.output, r.Description])
        
        return u"var tinyMCETemplateList = %s;" % json.dumps(templates)
