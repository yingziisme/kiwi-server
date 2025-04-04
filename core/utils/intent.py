import os
import sys
from config.logger import setup_logging
import importlib

logger = setup_logging()

_providers = {}


def create_instance(class_name, *args, **kwargs):
    if class_name in _providers:
        return _providers[class_name]

    # 创建intent实例
    if os.path.exists(os.path.join('core', 'providers', 'intent', class_name, f'{class_name}.py')):
        lib_name = f'core.providers.intent.{class_name}.{class_name}'
        if lib_name not in sys.modules:
            sys.modules[lib_name] = importlib.import_module(f'{lib_name}')
        _providers[class_name] = sys.modules[lib_name].IntentProvider(*args, **kwargs)
        return _providers[class_name]

    raise ValueError(f"不支持的intent类型: {class_name}，请检查该配置的type是否设置正确")