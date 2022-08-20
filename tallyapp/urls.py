from .import views
from django.urls import path,include

urlpatterns = [
    # path('',views.base,name="base"),
    path('create',views.create,name="create"),
    path('companycreate',views.companycreate,name="companycreate"),
    path('gst_details/<int:pk>',views.gst_details,name="gst_details"),
    path('add_gstdetails/<int:pk>',views.add_gstdetails,name="add_gstdetails"),
    path('tds_deductor/<int:pk>',views.tds_deductor,name="tds_deductor"),
    path('person_details/<int:pk>',views.person_details,name="person_details"),
    path('add_person/<int:pk>',views.add_person,name="add_person"),
    path('add_tds/<int:pk>',views.add_tds,name="add_tds"),
    path('features/<int:pk>',views.features,name="features"),
     path('edit_features/<int:pk>',views.edit_features,name="edit_features"),
    path('',views.dashboard,name="dashboard"),
    path('company_list',views.company_list,name="company_list"),
    path('select_company',views.select_company,name="select_company"),
    path('dash_board/<int:pk>',views.dash_board,name="dash_board"),
    path('alter_company',views.alter_company,name="alter_company"),
    path('edit_page/<int:pk>',views.edit_page,name="edit_page"),
    path('edit_companydetails/<int:pk>',views.edit_companydetails,name="edit_companydetails"),
    path('change_company',views.change_company,name="change_company"),
    path('shut_company',views.shut_company,name="shut_company"),
    
    path('shut/<int:pk>',views.shut,name="shut"),
    path('date_change',views.date_change,name="date_change"),
    path('print_config',views.print_config,name="print_config"),
    path('add_country',views.add_country,name="add_country"),
    path('download',views.download,name="download"),
    path('addstates',views.addstates,name="addstates"),
    path('state_country',views.state_country,name="state_country"),
    path('load_cities',views.load_cities,name="load_cities"),
    path('edit_gst_details/<int:pk>',views.edit_gst_details,name="edit_gst_details"),
    path('add_newgstdetails/<int:pk>',views.add_newgstdetails,name="add_newgstdetails"),
    path('edit_tds_deductor/<int:pk>',views.edit_tds_deductor,name="edit_tds_deductor"),
    path('add_newtdsdetails/<int:pk>',views.add_newtdsdetails,name="add_newtdsdetails"),
    path('edit_person_details/<int:pk>',views.edit_person_details,name="edit_person_details"),
    path('add_newpersondetails/<int:pk>',views.add_newpersondetails,name="add_newpersondetails")
   
]
