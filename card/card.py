'''
卡片函数记录卡片名称等基本属性
'''
import time


class Card:
    def __init__(self):
        self.card_id = ""
        self.card_time = ""
        self.cart_question = ""
        self.card_answer = ""

    def create_card(self, card_id, card_question, card_answer):
        self.card_id = card_id
        self.card_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.card_answer = card_answer
        self.cart_question = card_question

    def delete_card(self):
        pass

    def update_card(self, card_type, card_content):
        if card_type == "card_question":
            self.cart_question = card_content
        elif card_type == "card_answer":
            self.card_answer = card_content
        else:
            raise Exception("wrong card type")

    def select_card(self):
        pass
