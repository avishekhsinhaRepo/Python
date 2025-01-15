import numpy as np

mylist = [1, 2, 3, 4, 5]
my_array = np.array(mylist)
print(type(my_array), my_array)
print(type(mylist),mylist)

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

my_np_matrix = np.array(my_matrix)

print(my_np_matrix)

print(np.arange(0, 10, 2, dtype=float))

print(np.ones((2,3), dtype=int))

print(np.random.randint(20, size=(3, 2)))

# Set the seed
np.random.seed(42)

# Generate a random number
print(np.random.rand(5))

#Reset the seed
np.random.seed(42)

 # Generate another random number
print("Random Number with same seed", np.random.rand(5))

ud_rand = np.random.rand(6)
print(ud_rand)

print(np.reshape(ud_rand,(2,3)))

print(ud_rand.reshape((2,-1)))

ran_10 = np.random.randint(10, size=20)
print(ran_10)



print("Maximum Value =", ran_10.max())
print("Index of Maximum Value =",ran_10.argmax())
print("Minimum Value =",ran_10.min())
print("Index of Minimum Value =",ran_10.argmin())


ran_one_d = np.random.randint(10, size=20)
print(ran_one_d)
print(ran_one_d.shape)
ran_two_d = ran_one_d.reshape(4,5)
print(ran_two_d)
print(ran_two_d.shape)


arr_index = np.arange(0, 11)
print(arr_index)

# Selection of elements on given index
print(arr_index[8])

print(arr_index[1:5])

print(arr_index[0:5])

print(arr_index[:5])

print(arr_index[5:])

print(arr_index[:-3])



arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)

print(arr_2d.shape)

print(arr_2d[0])
print(arr_2d[2])

print(arr_2d[1][1])
print(arr_2d[1,1])


arr_10 = np.arange(0, 11)
print(arr_10)

add_5_to_arr = arr_10 + 5
print(add_5_to_arr)


sub_2_to_arr = arr_10 - 2
print(sub_2_to_arr)


add_arr = arr_10 + arr_10
print(add_arr)

mul_arr = arr_10 * arr_10
print(mul_arr)

sub_arr = arr_10 - arr_10
print(sub_arr)

div_arr = arr_10 / arr_10
print(div_arr)

div_arr_scaler = 1/arr_10
print(div_arr_scaler)

arr_square = np.square(arr_10)
print(arr_square)

arr_sqrt = np.sqrt(arr_10)
print(arr_sqrt)

arr_non_zeros = np.arange(1, 11)
arr_log = np.log(arr_non_zeros)
print(arr_log)

arr_sum = arr_10.sum()
print(arr_sum)

arr_mean = arr_10.mean()
print(arr_mean)

arr_max = arr_10.max()
print(arr_max)

arr_variance = arr_10.var()
print(arr_variance)

arr_std = arr_10.std()
print(arr_std)


arr_sum = np.arange(1, 21)
print(arr_sum)

arr_sum_1_d = arr_sum.sum()
print(arr_sum_1_d)

arr_2_d = arr_sum.reshape(4,5)
print(arr_2_d)

arr_2_d_add_by_row = arr_2_d.sum(axis=1)
print(arr_2_d_add_by_row)

A = np.array([1, 2, 3])   # A is of shape (3,)
B = 2                     # B is a scalar, or shape ()
C = B * A                 # This is possible due to broadcasting

print(C)

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)

print("*"*20)

print(arr_2d[0])

#print specific column
print(arr_2d[:2,1:])

print(arr_2d[1:,1])

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

bool_arr= arr > 5

print(bool_arr)

print(arr[bool_arr])

dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])

total_rolls_over_two = dice_rolls[dice_rolls > 2]
print(len(total_rolls_over_two))



