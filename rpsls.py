#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��Ա��İ�������
���ڣ�2022.5.11
"""

import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

def name_to_number(name):
    if name=='ʯͷ':
        name=0
        return name
    elif name=='ʷ����':
        name=1
        return name
    elif name=='ֽ':
        name=2
        return name
    elif name=='����':
        name=3
        return name
    elif name=='����':
        name=4
        return name


def number_to_name(number):

    if number==0:
        number='ʯͷ'
        return number
    elif number==1:
        number='ʷ����'
        return number
    elif number==2:
        number='ֽ'
        return number
    elif number==3:
        number='����'
        return number
    elif number==4:
        number='����'
        return number


def rpsls(player_choice):

    print('-------------------')
    print('���ѡ��Ϊ��' + player_choice)
    player_choice_number = name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print('�������ѡ��Ϊ��' + number_to_name(comp_number))
    if player_choice_number==comp_choice:
        print('�����ͼ��������һ���ء�')
    elif ((comp_choice == (player_choice_number - 1)) and (player_choice_number >= 1)
         ) or ((comp_choice == 4) and (player_choice_number <= 1)
         ) or ((comp_choice == 3) and (player_choice_number == 0)):
        print('��Ӯ��')
    else:
        print('�����Ӯ��')

    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


