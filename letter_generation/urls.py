from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from letter_generation import settings
from login.views import *
import login.views
import offer_letter.views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                            #admin url
                       url(r'^admin/', include(admin.site.urls)),
                            #offer letter generation url
                       url(r'^list/$', offer_letter.views.ListContactView.as_view(),name='employee-list', ),
                       url(r'^new/$', offer_letter.views.CreateEmployeeView.as_view(),
                           name='employee-new', ),
                       url(r'^edit/(?P<pk>\d+)/$', offer_letter.views.UpdateEmployeeView.as_view(),
                           name='employee-edit', ),
                       url(r'^delete/(?P<pk>\d+)/$', offer_letter.views.DeleteEmployeeView.as_view(),
                           name='employee-delete', ),
                       url(r'^employee_details/(?P<pk>\d+)/$', offer_letter.views.EmployeeView.as_view(),name='employee-view', ),
                       url(r"^(?P<pk>\d+)/offer_letter/$", offer_letter.views.offerletter.as_view(), name='get-offer',),

                            # Below is login module url like registration login logout etc.
                       url(r'^$', index),
                       url(r'^login/$', 'django.contrib.auth.views.login',name='login'),
                       url(r'^logout/$', logout_page),
                            # If user is not login it will redirect to login page
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       url(r'^register/$', register),
                       url(r'^register/success/$', register_success),
                       url(r'^home/$', home),
                            #password reset and email authentication url
                       url(r'^success/$','login.views.success_password',name="success"),
                       url(r'^update-password/$', 'login.views.reset', name='reset'),
                       url(r'^account/', include('django.contrib.auth.urls')),

                       #url(r'^reset/$', 'login.views.reset', name='reset'),
                       url(r'^password/reset/confirm/complete/$',
                                   login.views.password_reset_complete,
                                   name='password_reset_complete'), # must be named for reverse to work
                       url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                            'login.views.reset_confirm',
                            name='password_reset_confirm'),

                      #HR Module
                      url(r'HR/$',offer_letter.views.hr_module.as_view(),name='hr_module', ),


                      )

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)