from django.apps import AppConfig


class UserOperationConfig(AppConfig):
    name = 'user_operation'
    verbose_name = "用户操作管理"

    def ready(self):
        import user_operation.signals
