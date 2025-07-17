# ===== String Methods =====
# x="90"
# import string
# print(str.upper("sundar"))
# print(str.lower("sundar"))
# print(str.isnumeric(x))
# print(str.strip("  sundar i"))
# print(str.split("sundar"))
# print
# print(bool({}))

# ===== Class and Method =====
# class class_name():
#     def myfunc( self):
#         return True
# obj=class_name()
# print(obj.myfunc())

# ===== Function and Input Check =====
# def fun():
#     x=input("enter a valuse :")
#     return x
# if fun():
#     print("yes there is a text")
# else:
#     print("No there is no text or some else ")

# ===== List Basics and Slicing =====
# thislist=["sakthi","Kavya","sundar","hari","siva","deepa"]
# print(thislist)
# for i in thislist:
#     print(i)
# print(thislist[1])
# print(thislist[1:])
# print(thislist[-1])

# ===== List Append and Slicing Variations =====
# thislist.append("surya")
# print(thislist)
# print(thislist[::-1])
# print(thislist[:4])
# print(thislist[2::2])
# print(thislist[-3::])

# ===== List Search and Indexing =====
# if "Kavya" in thislist:
#     print(thislist.index("Kavya"))
# else:
#     print("No there is no name like this")

# ===== List Update and Insert =====
# thislist[0]="karthi"
# print(thislist)
# thislist[1:4]=["naveen","lokesh"]
# print(thislist)
# print(thislist.insert(2,"sakthi"))
# print(thislist)

# ===== List Extend and Concatenation =====
# secondlist=["apple","bannana","orange"]
# third=thislist.extend(secondlist)
# thirdlist=thislist+secondlist
# print(thirdlist)

# ===== List Concatenation and Removal =====
# fruits=["apple","orange","grapes"]
# fruits1=["lichi","kiwi","pineaple"]
# fruits3=fruits+fruits1
# print(fruits3)
# fruits3.remove("grapes")
# print(fruits3)
# print(fruits3.pop(2))

# ===== Delete List and Looping =====
# del fruits1/
# print(fruits1)
# for i in fruits3:
#     print(i)
# i=0 
# while(i<len(fruits3)):
#     print(fruits3[i])
#     i+=1

# ===== List Comprehension and Indexing =====
# [print(i) for i in fruits]
# [print(fruits3.index(i)) for i in fruits3 if "kiwi" == i]

# ===== List Copy and Sorting =====
# print("HELLO WORLD")
# fruits4=[]
# [fruits4.append(i) for i in fruits]
# print(fruits4)
# fruits4.sort(reverse=True)
# print(fruits4)

# ===== List Insert and Custom Sort =====
# fruits.insert(1,"papaya")
# fruits.insert(1,"Lemon")
# print(fruits)
# fruits.sort(key = str.upper)
# fruits.reverse()
# print(fruits)

# ===== List Copy Methods =====
# fruits5= fruits.copy()
# print(fruits5)
# fruits6=fruits[:]
# print(fruits6)
# fruits7=list(fruits)
# print(fruits7)

# ===== List Copy Examples =====
# thislist=["red","yellow","blue","orange"]
# secondlist=thislist.copy()
# print(secondlist)
# thirdlist=list(thislist)
# print(thirdlist)
# fourthlist=thislist[:]
# print(fourthlist)

# ===== List Append from Another List =====
# second =["black","green","pink"]
# # print(thislist+second)/
# for i in second:
#     thislist.append(i)
# print(thislist)
# thislist.sort(reverse=True)
# print(thislist)
# print(thislist.count("black"))
# second.reverse()
# print(second)

# ===== Tuple Update and Unpacking =====
# tup=("yellow","orange")
# #update
# l=list(tup)
# l[1]="black"
# print(l)
# tup=tuple(l)
# print(tup)
# y=("green",)
# tup += y
# print(tup)
# (red,white,blue)=tup
# print(red)

# ===== Tuple Update Repeated =====
# tup=("yellow","orange")
# #update
# l=list(tup)
# l[1]="black"
# print(l)
# tup=tuple(l)
# print(tup)
# y=("green",)
# tup += y
# print(tup)
# (red,white,blue)=tup
# print(red)

# ===== Set Operations =====
# thisset={1,2,3,0,True,"syundara","arun"}
# print(thisset)
# print(len(thisset))
# for i in thisset:
#     if i=="arun":
#         print("yes !!! ,He is here ...")
# print(thisset)
# y={4,5,6}
# thisset.update(y)
# print(thisset)
# thisset.add("sundar")
# print(thisset)
# thisset.remove("arun")
# print(thisset)
# thisset.discard("syundara")
# print(thisset)
# # thisset.clear()
# print(thisset)
# thisset.pop()
# print(thisset)

# ===== Set Union and Difference =====
# thisset={"sundar","ram","kavya","sakthi"}
# secondset={1,2,4,5,6}
# set3=thisset.union(secondset)
# print(set3)
# set4=thisset|secondset
# print(set4)
# set5=thisset.difference(secondset)
# print(set5)

# ===== Dictionary Basics =====
# dictionary={
#     "name":"sundar",
#     "mobile":6726833833,
#     "city":"salem"
# }
# for i in dictionary:
#     print(dictionary[i])
# print(dictionary.values())
# dictionary["name"]="mouli"
# print(dictionary["name"])
# dictionary.update({"city":"erode"})
# print(dictionary["city"])
# for i,j in dictionary.items():
#     print(i,":",j)

# ===== Nested Dictionary =====
# child={
#     "child1":{"name":"sundar",
#             "city":"salem",
#             "phone":"6374070014"
#     },
#     "child2":{"name":"mouli",
#         "city":"erode",
#         "phone":"9360225803"
#     },
#     "child3":{"name":"deva",
#         "city":"mettur",
#         "phone":"6382107087"
#     }
# }
# print(child["child1"]["name"],)
# print(child["child2"]["name"])
# print(child["child3"]["name"])

# ===== Dictionary Iteration =====
# d={"name":"sundar","city":"salem"}
# for x,y in d.items():
#     print(x,y)

# ===== Input Type Checker =====
# this condition check whether given input is str, number,or special or mix of all .

# import string
a = input("enter a valuse: ")
b=input("enter a valuse : ")
if (a.isnumeric())and(b.isnumeric()):
    print("both inputs are number")
# 657899
elif(a.isalpha()) and (b.isalpha()):
    print("both are strings")
elif(a.isalpha()) and (b.isnumeric()):
    print("a is string but  b is number")
elif (b.isalpha()) and (a.isnumeric()):
    print("a is number and b is string")
else:
    a_res=[]
    b_res=[]
    for i in a :
        if (i.isalpha()):
            a_res.append("alphabetic")
        elif(i.isnumeric()):
            a_res.append("number")
        elif((not(i.isalnum()))):
            a_res.append("special character")
    # print(a_res)
    for i in b :
        if (i.isalpha()):
            b_res.append("alphabetic")
        elif(i.isnumeric()):
            b_res.append("number")
        elif((not(i.isalnum()))):
            b_res.append("special character")
    # print(set(b_res))
    setA=set(a_res)
    setB=set(b_res)
    listA=list(setA)
    listB=list(setB)
    if (len(listA)==1) and (len(listB)==1) and (listA[0]=="special character") and(listB[0]=="special character"):
        print("both are special character only")
    else:
        print("In this string contains mix of {}".format(listA[:]))

# ===== Match Case (Switch Equivalent) =====
# day=int(input("enter a day :"))
# match day:
#     case 1:
#         print("today is monday")
#     case 2 :
#         print("today is tuesday")
#     case 3 :
#         print("today is wednesday")
#
