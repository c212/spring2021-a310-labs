from AVL import *

nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
a = AVL(nums[0])
print("-------------starting with", nums[0])
a.display()
for num in nums[1:]:
  print("-------------after we add", num)
  a.insert(AVL(num))
  a = a.adjust()
  a.display()

# ======== RESTART: C:\Users\dgerman\Desktop\march-08-lecture\tests-AVL.py ========
# 
# -------------starting with 10
# 10
# -------------after we add 1
#  10
# /  
# 1  
# -------------after we add 9
#  9_ 
# /  \
# 1 10
# -------------after we add 2
#  _9_ 
# /   \
# 1  10
#  \   
#  2   
# -------------after we add 8
#   _9_ 
#  /   \
#  2  10
# / \   
# 1 8   
# -------------after we add 3
#   _8   
#  /  \  
#  2  9_ 
# / \   \
# 1 3  10
# -------------after we add 7
#   __8   
#  /   \  
#  2   9_ 
# / \    \
# 1 3   10
#    \    
#    7    
# -------------after we add 4
#   ___8   
#  /    \  
#  2_   9_ 
# /  \    \
# 1  4   10
#   / \    
#   3 7    
# -------------after we add 6
#     __8   
#    /   \  
#   _4_  9_ 
#  /   \   \
#  2   7  10
# / \ /     
# 1 3 6     
# -------------after we add 5
#     ___8   
#    /    \  
#   _4_   9_ 
#  /   \    \
#  2   6   10
# / \ / \    
# 1 3 5 7    
# >>> 
#
# ===== COMPARE @ https://www.cs.usfca.edu/~galles/visualization/AVLtree.html =====
