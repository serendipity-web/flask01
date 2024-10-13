import pytest
from card.card import Card

class Test_Card:
    def test_update_card_with_question(self):
        # 测试更新问题卡片
        card = Card()
        card_content = "What is the capital of France?"
        card.update_card("card_question", card_content)
        assert card.cart_question == card_content

    def test_update_card_with_answer(self):
        # 测试更新答案卡片
        card = Card()
        card_content = "Paris"
        card.update_card("card_answer", card_content)
        assert card.card_answer == card_content

    def test_update_card_with_wrong_type(self):
        # 测试错误的卡片类型
        card = Card()
        card_type = "wrong_card_type"
        card_content = "Some content"
        with pytest.raises(Exception) as exc_info:
            res = card.update_card(card_type, card_content)
            print(res)
        assert "wrong card type" in str(exc_info.value)
