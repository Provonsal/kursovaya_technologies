from functools import wraps
from types import UnionType
from typing import Any, Callable, Iterable, Mapping
        

class FieldValidator:
    def __init__(self, fieldName: str, annotationType: type | UnionType | None = None) -> None:
        self._fieldName: str = fieldName
        self._annotationType: type | UnionType | None = annotationType
        
    def _create_annotations(self, cls) -> bool:
        
        all_annotations = getattr(cls, "__annotations__", None)
        
        # Если аннотаций в классе вообще не прописано то создаем их
        if all_annotations is None:
            setattr(cls, "__annotations__", {})
            return True
        return False
    
    def _set_annotation_to_class(self, cls, attrName) -> None:
        # Если в параметрах указана аннотация то смотрим
        if self._annotationType is not None:
            
            # берем все существующие аннотации
            all_annotations = getattr(cls, "__annotations__", None)

            # если аннотации уже существуют
            if all_annotations is not None:
                # и аннотация к атрибуту не прописана в классе то записываем свою
                if all_annotations.get(attrName) is None or (all_annotations.get(attrName) == self._annotationType):
                    cls.__annotations__[attrName] = self._annotationType
                # если существует аннотация к атрибуту и в параметрах тоже передана аннотация то поднимаем ошибку  
                else:
                    raise Exception("Annotation overload")
            # если аннотаций не существует то поднимаем ошибку
            else:
                raise Exception("Annotations not found")
            
        else:
            return
    
    def _get_annotation(self, cls, attrName) -> type | UnionType:
        
        # берем все существующие аннотации
        all_annotations: dict[str, type] | None = getattr(cls, "__annotations__", None)
        
        if all_annotations is not None:
            
            attr_annotation: type | None = all_annotations.get(attrName)
            
            # смотрим если нет аннотации к типу
            if attr_annotation is None:
                # и в параметрах не указана аннотация то поднимаем ошибку
                if self._annotationType is None:
                    raise Exception("Field annotation not found")
                # если указано то возвращаем указанную в параметрах аннотацию
                else:
                    return self._annotationType
            # если аннотация есть изначально то ее и возвращаем
            else:
                return attr_annotation
        else:
            raise Exception("Annotations not found")
    
    def _check_args(self, args: Iterable, kwargs: Mapping[str, Any], attr_type: type | UnionType | None):
        
        if attr_type is not None:
            for arg in args:
                assert isinstance(arg, attr_type), f"Wrong field type. Type should be {attr_type}, but got {type(arg)} instead"
                
            for value in kwargs.values():
                assert isinstance(value, attr_type), f"Wrong field type. Type should be {attr_type}, but got {type(value)} instead"
        else:
            raise Exception("Type is none")
    
    def __call__(self, func):
        
        def wrapper(cls, *args, **kwargs):
            
            self._create_annotations(cls)

            attr_type = self._get_annotation(cls, self._fieldName)
            self._set_annotation_to_class(cls, self._fieldName)

            self._check_args(args, kwargs, attr_type)
            
            return func(cls, *args)
        return wrapper