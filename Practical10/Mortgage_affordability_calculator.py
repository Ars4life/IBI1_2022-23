def Mortage_affodability_cal(value, salary):
    if value > 5*salary:
        return 'no'
    else:
        return 'yes'

print(Mortage_affodability_cal(10000, 30),
      Mortage_affodability_cal(2222222222, 1111111111),
      Mortage_affodability_cal(50, 30))
