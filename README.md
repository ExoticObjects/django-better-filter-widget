django-better-filter-widget
===========================

A better filter widget for foreign key relationships that also works on mobile devices.

<img src="http://i.imgur.com/jzKen5h.gif" width="542"/>

# About
Django's horizontal and vertical filter widget is ugly, confusing to new users and completely broken on mobile devices. **django-better-filter-widget** is not magic and does not do real-time lookups like **django-selectable**. It's simply a nicer UI for filtering a list of things that, most importantly, actual works on mobile devices.


# Installation

Note: This project is brand spanking new as still being tested. It was developed using django 1.6. It was tested in modern desktop and mobile browsers.

**Install with pip**

`pip install django-better-filter-widget`

**settings.py**

Add 'better_filter_widget' to INSTALLED_APPS in your settings.py

** admin.py **

Specify the Better Filter as your widget:

	class MyModelForm(forms.ModelForm):
	    
	    class Meta(object):
	        model = MyModel
	        widgets = {
	            'my_field': BetterFilterWidget(),
	        }
	       

	class MyModelAdmin(admin.ModelAdmin):

	    form = MyModelForm

	admin.site.register(MyModel, MyModelAdmin)
    
