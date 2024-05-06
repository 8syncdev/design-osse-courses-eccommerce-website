from django.contrib import admin
from .models import (
    User,
    Category,
    Comment,
    Course,
    Detaillesson,
    Enrollment,
    Exercise,
    Extent,
    Invoice,
    Invoicedetails,
    Lesson,
    Payment,
    Shoppingcart,
    ShoppingcartDetails,
    Submission,
    WalletCrypto,
    Crypto,
    Discount,
    Role,
    Userrole,
    Status,
    CourseStatus,
)

from unfold.admin import ModelAdmin as ModelAdminUI
from unfold.contrib.import_export.admin import ExportActionModelAdmin



# class ExampleAdmin(ModelAdminUI, ExportActionModelAdmin, ImportExportModelAdmin):
#     import_form_class = ImportForm
#     export_form_class = ExportForm

# Đăng ký các model với trang quản trị
@admin.register(User)
class UserAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['username', 'email', 'full_name', 'phone', 'created_at', 'updated_at']

@admin.register(Category)
class CategoryAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['category_name', 'created_at', 'updated_at']

@admin.register(Comment)
class CommentAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['user', 'course', 'content', 'created_at', 'updated_at']

@admin.register(Course)
class CourseAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['title', 'description', 'price', 'instructor', 'created_at', 'updated_at']

@admin.register(Detaillesson)
class DetaillessonAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['name', 'lesson', 'extent', 'created_at', 'updated_at']

@admin.register(Enrollment)
class EnrollmentAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['user', 'course', 'created_at', 'updated_at']

@admin.register(Exercise)
class ExerciseAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['title', 'description', 'detail_lesson', 'created_at', 'updated_at']

@admin.register(Extent)
class ExtentAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


@admin.register(Invoice)
class InvoiceAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['tolal_price', 'shopping_cart', 'created_at', 'updated_at']

@admin.register(Invoicedetails)
class InvoicedetailsAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['invoice', 'shopping_cart_details', 'created_at', 'updated_at']

@admin.register(Lesson)
class LessonAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['title', 'description', 'course', 'created_at', 'updated_at']

@admin.register(Payment)
class PaymentAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['status', 'shopping_cart', 'wallet_crypto', 'created_at', 'updated_at']


@admin.register(Shoppingcart)
class ShoppingcartAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']

@admin.register(ShoppingcartDetails)
class ShoppingcartDetailsAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['shopping_cart', 'course', 'created_at', 'updated_at']

@admin.register(Submission)
class SubmissionAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['code', 'exercise', 'user', 'created_at', 'updated_at']

@admin.register(WalletCrypto)
class WalletCryptoAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['user', 'crypto', 'amount', 'created_at', 'updated_at']
    
@admin.register(Crypto)
class CryptoAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['crypto_name', 'created_at', 'updated_at']

@admin.register(Discount)
class DiscountAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['discount_percentage', 'code_name', 'created_at', 'updated_at']

@admin.register(Role)
class RoleAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['role_name', 'created_at', 'updated_at']

@admin.register(Userrole)
class UserroleAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['user', 'role', 'created_at', 'updated_at']

@admin.register(Status)
class StatusAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(CourseStatus)
class CourseStatusAdmin(ModelAdminUI, ExportActionModelAdmin):
    list_display = ['course', 'status', 'created_at', 'updated_at']




