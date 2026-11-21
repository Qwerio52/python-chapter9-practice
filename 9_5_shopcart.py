# 9.5 购物车管理系统
class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShopCart:
    def __init__(self):
        self.goods_list = []

    def add_goods(self, goods):
        self.goods_list.append(goods)
        print(f"添加商品：{goods.name}")

    def del_goods(self, goods_name):
        for g in self.goods_list:
            if g.name == goods_name:
                self.goods_list.remove(g)
                print(f"删除商品：{goods_name}")
                return
        print("未找到该商品")

    def get_total(self, discount=1.0):
        total = sum(g.price for g in self.goods_list) * discount
        print(f"购物车总价（折扣{discount}）：{total:.2f}")
        return total


if __name__ == "__main__":
    cart = ShopCart()
    g1 = Goods("水杯", 25)
    g2 = Goods("笔记本", 15)
    cart.add_goods(g1)
    cart.add_goods(g2)
    cart.get_total(0.9)
    cart.del_goods("水杯")
    cart.get_total()