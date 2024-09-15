# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
        


# sol = Solution()

# nums = [3, 2, 4]
# target = 6

# result = sol.twoSum(nums, target)
# print(result)

# class Cat:
#     breed = 'pets'
#     def hello(*args):
#         print("hello world from kitty", args)
    
#     def show_breed(instance):
#         print(f'my breed is {instance.breed}')

#     def show_name(instance):
#         if hasattr(instance, 'name'):
#             print(f'my name is {instance.name}')
#         else:
#             print('nothing')

#     def set_value(koshka, value, age):
#         koshka.name = value
#         koshka.age = age 


# bobby = Cat()

# print(bobby.show_name())



# class Cat:

#     def __init__(self, name, breed = 'pers', age = 1 , color = 'white'):   
#         print('hello new object is ', self, name, breed, age, color)
#         self.name = name 
#         self.age = age
#         self.breed = breed
#         self.color = color

# # Cat('miras', 'siam', 50, 'black')

# walt = Cat('sala', 'siam', 5 , 'black')
# print(walt.age)
# from math import sqrt


# class Point:
#     def __init__(self, coor_x = 0 , coor_y = 0 ):
#         self.move_to(coor_x, coor_y)

#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y

#     def go_home(self):
#         self.move_to(0, 0)   

#     def print_point(self):
#         print(f"point with coordinates ({self.x},{self.y})")    

#     def calc_distance(self, another_point):
#         if not isinstance(another_point, Point):
#             raise ValueError("argument must get class Point")
        
#         return sqrt((self.x - another_point.x)**2 +(self.y - another_point.y)**2)  

# p1 = Point(6, 2)
# print(p1.__dict__)

# p2 = Point(4, 8)

# print(p2.__dict__)

# print(p1.calc_distance(p2))
# 

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        str_x = str(x)
        
        if str_x == str_x[::-1]:
            return True
        else:
            return False

p1 = Solution()

print(p1.isPalindrome(123))


            

