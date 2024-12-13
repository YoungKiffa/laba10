import cProfile
import pstats

def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

# Профилируем функцию для различных значений n
def run_profiling():
    cProfile.run('fibonacci_memoization(35)')

# Запускаем профилирование
run_profiling()

# Сохраняем результаты в файл для последующего анализа
profiler = cProfile.Profile()
profiler.enable()
fibonacci_memoization(40)
profiler.disable()

# Анализируем результаты
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.print_stats()

