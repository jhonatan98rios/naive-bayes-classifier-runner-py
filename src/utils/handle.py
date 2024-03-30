from typing import Tuple, Any, Callable

def handle(func: Callable[..., Any], *args, **kwargs) -> Tuple[Exception, Any]:
    try:
        result = func(*args, **kwargs)
        return (None, result)  # Retorna None para o erro e o resultado da função
    except Exception as e:
        return (e, None)  # Retorna a exceção e None para o resultado
