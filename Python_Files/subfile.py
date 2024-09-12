def add(list):
    total = 0
    try: 
        for arguements in list:
            total += arguements
        return total
    except Exception:
        print("Your values must be an integer")

# def sub(*args):
#     total = args[0]
#     try: 
#         for arg in args[1:]:
#             total -= arg
#         return total
#     except Exception:
#         print("Your values must be an integer")
        
# def multiply(*args):
#     total = args[0]
#     try: 
#         for arg in args[1:]:
#             total *= arg
#         return total
#     except Exception:
#         print("Your values must be an integer")
# def div(*args):
#     num = args[0]
#     for arg in args[1:]:
#         num /= arg
#     return num
    


    