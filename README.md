django-better-filter-widget
===========================

A better filter widget for foreign key relationships that also works on mobile devices. This was initially developed as a drop-in replacement for  admin forms. It will work in a normal form but you'll have to include some css/js dependencies. I'll write about how to do that soon.

<img src="http://i.imgur.com/jzKen5h.gif" width="542"/>

# About
Django's [horizontal and vertical filter widget](http://i.imgur.com/RBgrm.png) is ugly, confusing to new users and completely broken on mobile devices. **django-better-filter-widget** is not magic and does not do real-time lookups like **django-selectable**. It's simply a nicer UI for filtering a list of things that, most importantly, actual works on mobile devices.


# Installation

Note: This project is brand spanking new and is still being tested. It was developed using django 1.6. It was tested in modern desktop and mobile browsers.

**Install with pip**

`pip install django-better-filter-widget`

**settings.py**

Add 'better_filter_widget' to INSTALLED_APPS in your settings.py

**admin.py**

Specify BetterFilterWidget as the widget for your field:

	from django import forms
	from django.contrib import admin
	from better_filter_widget import BetterFilterWidget

	class MyModelForm(forms.ModelForm):
	    
	    class Meta(object):
	        model = MyModel
	        widgets = {
	            'my_field': BetterFilterWidget(),
	        }
	       

	class MyModelAdmin(admin.ModelAdmin):

	    form = MyModelForm

	admin.site.register(MyModel, MyModelAdmin)
    

# License

The MIT License (MIT)

Copyright (c) 2014 Exotic Objects

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

