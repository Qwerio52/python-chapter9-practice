# 9.3 简易计算器 @classmethod
class Calc:
    @classmethod
    def calculate(cls, expr: str):
        try:
            res = eval(expr)
            print(f"表达式 {expr} = {res}")
            return res
        except Exception as e:
            print("表达式错误！", e)
            return None


if __name__ == "__main__":
    Calc.calculate("10+2*5")
    Calc.calculate("(100-20)/4")