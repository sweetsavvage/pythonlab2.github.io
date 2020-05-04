from my_classes import *

def main():
    print('Creating receipt...')
    receipt = Receipt(False, 'Ru', 'Some author', 'Some recipient', 1500, ['service 1',' service 2','service 3'])
    print('Receipt author: ', receipt.get_author())
    print('Receipt style: ', receipt.get_style())
    print('Receipt recipient: ', receipt.get_recipient())
    print('Receipt services list: ', receipt.get_services_list())
    print('Is signed: ', receipt.get_is_signed())

    print('Creating waybill...')
    waybill = Waybill(False, "Ru", 'Some author 2', {'pr1':3, 'pr2':4 , 'pr3':5}, 1890)
    print('Waybill author: ', waybill.get_author())
    print('Waybill style: ', waybill.get_style())
    print('Waybill products dict: ', waybill.get_products_dict())
    print('Is signed: ', waybill.get_is_signed())

    print('Creating account...')
    account = Account(True, 'Ru', 'Some author 3', ['pr1', 'pr2', 'pr3'], 1900)
    print('Account author: ', account.get_author())
    print('Account style: ', account.get_style())
    print('Account shopping list: ', account.get_shopping_list())

    print('Creating accountant...')
    accountant = Accountant('Viktor Vikrorovich', 'Company name', 30, 5, 15000,True)

    accountant.work(receipt)
    accountant.work(waybill)
    accountant.work(account)

    print('Is signed: ', receipt.get_is_signed())
    print('Is signed: ', waybill.get_is_signed())

if __name__ == '__main__':
    main()

