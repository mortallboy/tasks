'''Домашная работа'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('udemy_courses.csv')
fig, ax = plt.subplots(3,2)

free = df[df['price'] == 0]
non_free = df[df['price'] != 0]

task1_free_y = free.count()
task1_non_free_y = non_free.count()
task1_x = ['Количество']

task2_free_y = [free['num_subscribers'].max(),
                free['num_subscribers'].mean(),
                free['num_subscribers'].min()]
task2_non_free_y = [non_free['num_subscribers'].max(),
                    non_free['num_subscribers'].mean(),
                    non_free['num_subscribers'].min()]

task3_free_y = [free['num_reviews'].max(),
                free['num_reviews'].mean(),
                free['num_reviews'].min()]
task3_non_free_y = [non_free['num_reviews'].max(),
                    non_free['num_reviews'].mean(),
                    non_free['num_reviews'].min()]

task23_x = ['Макс.', 'Средн.', "Мин."]

ax[0][0].set_title('Бесплатные')
ax[0][1].set_title('Платные')

ax[0][0].bar(task1_x,task1_free_y)
ax[0][1].bar(task1_x,task1_non_free_y)
ax[1][0].bar(task23_x,task2_free_y,)
ax[1][1].bar(task23_x,task2_non_free_y)
ax[2][0].bar(task23_x,task3_free_y)
ax[2][1].bar(task23_x,task3_non_free_y)

ax[1][0].set_yscale('log')
ax[1][1].set_yscale('log')
ax[2][0].set_yscale('log')
ax[2][1].set_yscale('log')

plt.tight_layout()
plt.show()
