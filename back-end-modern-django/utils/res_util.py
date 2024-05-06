from typing import *
from dev_core.settings.settings import (
    DEBUG
)


class ResUtil:
    @staticmethod
    def res_success(name_res: str, data:any):
        return {
            'detail': name_res,
            'data': data,
            'code': 'res_success'
        }
    
    @staticmethod
    def res_fail(name_res: str, data: Optional[any] = None):
        return {
            'detail': name_res if DEBUG else "Don't show the error message in production mode",
            'data': data if DEBUG else "Don't show the error message in production mode",
            'code': 'res_fail'
        }