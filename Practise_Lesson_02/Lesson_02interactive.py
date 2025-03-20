# как-то получить щт пользователя оценку
rate_as_str = input("Оцените работу оператора от 1 до 5:")
rate = int(rate_as_str) # int

# протестировать, что оценка от 1 до 5

if(rate < 1):
    rate = 1

if(rate > 5):
     rate = 5

# в зависимости от оценки, предложить дать обратную связь
feetdback = ''

if rate ==1:
    feetdback = input("расскажите, что нам улучшить:")
elif rate == 2:
    feedback = input("расскажите, что вас смутило:")
elif rate == 3:
    feedback = input("расскажите, как нам стать лучше:")
elif rate == 4:
    feedback = input("расскажите, почему не 5:")
else:
    feedback = input("расскажите, за что похвалить оператора:")
print(feetdback)