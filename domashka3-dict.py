dict1 = {'����': [12, 1, 2], '�����': [3, 4, 5], '����': [6, 7, 8], '�����': [9, 10, 11]}
month = int(input("������� ����� ������ �� 1 �� 12: "))
if month in dict1.get("����"):
    print("����")
elif month in dict1.get('�����'):
    print("�����")
elif month in dict1.get('����'):
    print("����")
elif month in dict1.get('�����'):
    print("�����")
    