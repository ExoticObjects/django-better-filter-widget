from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms

class BetterFilterWidget(forms.SelectMultiple):
    class Media:
        extend = False
        css = {
            'all': ('css/better-filter-widget.css',)
        }
        js = ('js/better-filter-widget.js', )

    def render(self, name, value, attrs=None, choices=()):
        output = super(BetterFilterWidget, self).render(name, value, attrs, choices)
        output += u'''
        	<script type="text/javascript">
				(function($) {
                    $(window).ready(function(){
                        BetterFilterWidget('%s');
                    });
                })(window.$ || django.jQuery);
        	</script>
        ''' % name
        return mark_safe(output)