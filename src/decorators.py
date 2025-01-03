
import functools


def log(filename=None):
    """Декоратор который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор принимает на вход необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль)"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_message = f"Function {func.__name__} started with args: {args}, kwargs: {kwargs}\\n"
            try:
                result = func(*args, **kwargs)
                log_message += f"Function {func.__name__} finished with result: {result}\\n"
            except Exception as e:
                log_message += (f"Function {func.__name__} raised {type(e).__name__} with args: {args}, kwargs:"
                                f"{kwargs}\\n")
                raise
            finally:
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message)
            return result
        return wrapper
    return decorator
