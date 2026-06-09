


def cal_pet_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15

    elif human_years == 2:
        cat_years = 24
        dog_years = 24

    elif human_years == 10 :
        cat_years = 24 + (8*4) 
        dog_years = 24 + (8*5)

    return cat_years, dog_years


print("human_years = 1  =", cal_pet_years(1))
print("human_years = 2  =", cal_pet_years(2))
print("human_years = 10 =", cal_pet_years(10))