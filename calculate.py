def Min_cost(cost,discount_per_person,min_group_num):
    min_cost=cost*(((100-discount_per_person)/100)**min_group_num)
    return min_cost

def Max_cost(cost,discount_per_person,max_group_num):
    max_cost=cost*(((100-discount_per_person)/100)**max_group_num)
    return max_cost