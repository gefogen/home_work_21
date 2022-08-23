from classes.request import Request, check_request
from classes.shop import Shop
from classes.store import Store
from classes.exceptions import *
from classes.settings import *



def main():
    print(START_TEXT)
    
    input()
    
    store = Store()
    store.add("печеньки", 4)
    store.add("йогурт", 1)
    store.add("хлеб", 6)
    
    shop = Shop()
    shop.add("колбаса", 3)
    shop.add("холодильник", 2)
    shop.add("огурцы", 5)
    
    while True:
        user_input = input(">>> ").lower().strip()
        
        if user_input in ['exit', 'выход']:
            print("выход")
            quit()
        
        request = Request(user_input)
        
        error = check_request(request)
        if error is not None:
            print(error)
            continue
        
        try:
            store.remove(request.product, request.amount)
        except NotFoundItem:
            print("[!] Такого товара нет")
        except NotEnoughItems:
            print("[!] Не хватает товара на складе")
        else:
            try:
                shop.add(request.product, request.amount)
            except NotEnoughSpaceForUniqueItems:
                print("[!] В магазине не хватает места > 5 уникальных товаров")
            except NotEnoughSpace:
                print("[!] В магазине не хватает места > 20 штук")
            else:
                print(COURIER_ACTIONS_TEXT.format(amount=request.amount,
                                                  product=request.product,
                                                  from_=request.from_,
                                                  to=request.to))
                
                print("\nНа складе хранится:\n")
                for title, count in store.get_items().items():
                    print(count, title)
                
                print("\nВ магазине хранится:\n")
                for title, count in shop.get_items().items():
                    print(count, title)


if __name__ == "__main__":
    main()