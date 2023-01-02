
from django.urls import path

from adminapp import views

urlpatterns = [
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('adminlogout', views.adminlogout, name="adminlogout"),
    path('adminindex',views.adminindex,name="adminindex"),
    path('addstudent',views.addstudent,name="addstudent"),
    path('displaystudent',views.displaystudent,name="displaystudent"),
    path('editstudent/<int:dataid>',views.editstudent,name="editstudent"),
    path('deletestudent/<int:dataid>',views.deletestudent,name="deletestudent"),
    path('addadmin',views.addadmin,name="addadmin"),
    path('displayadmin',views.displayadmin,name="displayadmin"),
    path('editadmin/<int:dataid>',views.editadmin,name="editadmin"),
    path('deleteadmin/<int:dataid>',views.deleteadmin,name="deleteadmin"),
    path('addcategory',views.addcategory,name="addcategory"),
    path('displaycategory',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>', views.editcategory, name="editcategory"),
    path('deletecategory/<int:dataid>', views.deletecategory, name="deletecategory"),
    path('addproduct',views.addproduct,name="addproduct"),
    path('displayproduct',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:dataid>',views.editproduct,name="editproduct"),
    path('deleteproduct/<int:dataid>',views.deleteproduct,name="deleteproduct")

]
