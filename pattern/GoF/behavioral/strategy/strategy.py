from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, base_price: float) -> float:
        pass

class RegularPricing(PricingStrategy):
    def calculate_price(self, base_price: float) -> float:
        return base_price

class StudentPricing(PricingStrategy):
    def calculate_price(self, base_price: float) -> float:
        return base_price * 0.8

class SeniorPricing(PricingStrategy):
    def calculate_price(self, base_price: float) -> float:
        return base_price * 0.7

class VIPPricing(PricingStrategy):
    def calculate_price(self, base_price: float) -> float:
        return base_price * 1.2

class TravelPackage:
    def __init__(self, *, name: str, base_price: float, pricing_strategy: PricingStrategy):
        self.name = name
        self.base_price = base_price
        self.pricing_strategy = pricing_strategy

    def get_price(self):
        return self.pricing_strategy.calculate_price(self.base_price)

    def set_pricing_strategy(self, pricing_strategy: PricingStrategy):
        self.pricing_strategy = pricing_strategy


if __name__ == "__main__":
    regular_pricing = RegularPricing()
    student_pricing = StudentPricing()
    senior_pricing = SeniorPricing()
    vip_pricing = VIPPricing()

    tokyo_package = TravelPackage(name="Tokyo Adventure", base_price=1000, pricing_strategy=regular_pricing)

    print(f"Regular price: {tokyo_package.get_price()}")

    tokyo_package.set_pricing_strategy(student_pricing)
    print(f"Student price: {tokyo_package.get_price()}")

    tokyo_package.set_pricing_strategy(senior_pricing)
    print(f"Senior price: {tokyo_package.get_price()}")

    tokyo_package.set_pricing_strategy(vip_pricing)
    print(f"VIP price: {tokyo_package.get_price()}")

