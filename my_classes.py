# Создать абстрактный класс Документ.
# На его основе реализовать классы Квитанция, Накладная, Счет.

from abc import ABC, abstractmethod
from datetime import date

class Document(ABC):

    @abstractmethod
    def __init__(self, is_electronic, language, author, style):
        # self.set_text(text)
        self.set_is_electronic(is_electronic)
        self.set_language(language)
        self.set_author(author)
        self.set_style(style)

    def set_is_electronic(self, is_electronic):
        self.__is_electronic = bool(is_electronic)

    def get_is_electronic(self):
        return self.__is_electronic

    def set_language(self, language):
        self.__language = language

    def get_language(self):
        return self.__language

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_style(self, style):
        self.__style = style

    def get_style(self):
        return self.__style

class Receipt(Document):
    def __init__(self, is_electronic, language, author, recipient, amount_of_money, services_list, date = date.today(), is_signed = False, style = 'Official' ):
        super().__init__(is_electronic, language, author, style)
        self.set_recipient(recipient)
        # self.set_for_what(for_what)
        self.set_amount_of_money(amount_of_money)
        self.set_services_list(services_list)
        self.set_date(date)
        self.set_is_signed(is_signed)

    def set_recipient(self, recipient):
        self.__recipient = recipient

    def get_recipient(self):
        return self.__recipient

    # def set_for_what(self, for_what):
    #     self.__for_what = for_what
    #
    # def get_for_what(self):
    #     return self.__for_what

    def set_amount_of_money(self, amount_of_money):
        self.__amount_of_money = amount_of_money

    def get_amount_of_money(self):
        return self.__amount_of_money

    def set_services_list(self, services_list):
        self.__services_list = list(services_list)

    def get_services_list(self):
        return self.__services_list

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_is_signed(self, is_signed):
        self.__is_signed = is_signed

    def get_is_signed(self):
        return self.__is_signed

class Waybill(Document):
    def __init__(self, is_electronic, language, author, products_dict, amount_of_money, is_signed = False, style = 'Official'):
        super().__init__(is_electronic, language, author, style)
        NDS = amount_of_money / 100 * 5
        self.set_products_dict(products_dict)
        # self.set_for_what(for_what)
        self.set_amount_of_money(amount_of_money)
        self.set_is_signed(is_signed)

    def set_products_dict(self, products_dict):
        self.__products_dict = dict(products_dict)

    def get_products_dict(self):
        return self.__products_dict

    def set_amount_of_money(self, amount_of_money):
        self.__amount_of_money = amount_of_money

    def get_amount_of_money(self):
        return self.__amount_of_money

    def set_NDS(self, NDS):
        self.__NDS = NDS

    def get_NDS(self):
        return self.__NDS

    def set_is_signed(self, is_signed):
        self.__is_signed = is_signed

    def get_is_signed(self):
        return self.__is_signed

class Account(Document):
    def __init__(self, is_electronic, language, author, shopping_list, amount_of_money, date = date.today(), style = 'Official'):
        super().__init__(is_electronic, language, author, style)
        self.set_shopping_list(shopping_list)
        self.set_amount_of_money(amount_of_money)
        self.set_date(date)

    def set_shopping_list(self,_shopping_list):
        self.__shopping_list =_shopping_list

    def get_shopping_list(self):
        return self.__shopping_list

    def set_amount_of_money(self, amount_of_money):
        self.__amount_of_money = amount_of_money

    def get_amount_of_money(self):
        return self.__amount_of_money

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

# ----------------- Ввожу дополнительные классы для расширения функционала,
# ----------------- потому что сомневаюсь, что у бумаги могут быть методы...

class Worker(ABC):
    @abstractmethod
    def __init__(self, full_name, company_name, age, experience, salary):
        self.set_full_name(full_name)
        self.set_company_name(company_name)
        self.set_age(age)
        self.set_experience(experience)
        self.set_salary(salary)

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_full_name(self):
        return self.__full_name

    def set_company_name(self, company_name):
        self.__company_name = company_name

    def get_company_name(self):
        return self.__company_name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_experience(self, experience):
        self.__experience = experience

    def get_experience(self):
        return self.__experience

    @abstractmethod
    def work(self):
        pass

class Accountant(Worker):
    def __init__(self, full_name, company_name, age, experience, salary ,legal_education):
        super().__init__(full_name, company_name, age,experience,salary)
        self.set_legal_education(legal_education)

    def set_legal_education(self, _legal_education):
        self.__legal_education = bool(_legal_education)

    def get_legal_education(self):
        return self.__legal_education

    def __sign_document(self, document):

        try:
            document.set_is_signed(True)
            return True
        except AttributeError:
            return False

    def work(self, document):
        if self.__sign_document(document):
            print('{} document from {} signed!'.format(document.get_style(), document.get_author()))
        else:
            print('{} document from {} does not need a signature!'.format(document.get_style(), document.get_author()))

