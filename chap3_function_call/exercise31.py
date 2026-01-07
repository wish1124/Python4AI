from chap3_function_call.utils import standardization
from utils import get_random_score,get_data_statistics,cal_mean,cal_std


n_students = 100
sources = get_random_score(n_students)
print(get_data_statistics(sources))

scoures_ms = standardization(sources)
print(get_data_statistics(scoures_ms))


