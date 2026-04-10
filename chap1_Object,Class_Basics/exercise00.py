from collections import Counter
# #object = State(Attribute) + Behaviour(Method)
#
# test_list = [1,2,3]
#
# print(len(test_list))
#
# test_dict = {'a':0 ,'b' :1 , 'c' : 2}
#
# test_int = 3
#
# #class =  현실세계에서는 객체의 종류를 class라고 한다 ex) 선생님 클래스 , 의사 클래스 , 개발자 클래스
# #class =  클래스는 객체의 종류
#
# # object마다 State와 Behavior의 종류는 같습니다 그런데 그 값은 object마다 다를수 있다.
#
# test_int = 10
# test_int2 = 3

# print(test_int+test_int2)
# print(test_int-test_int2)
test_list = [1, 1, 1, 2, 3, 3]
result = {}

counter = Counter(test_list)
print(counter)

print(counter.most_common(3))
print(Counter("apple"))

for i in test_list:
    result[i] =  result.get(i,0)+1
print(result)

