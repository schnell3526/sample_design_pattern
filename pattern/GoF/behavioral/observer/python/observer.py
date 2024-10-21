from __future__ import annotations
from typing import Any
from abc import ABC, abstractmethod


class InventoryObserver(ABC):
    @abstractmethod
    def update(self, state: dict[str, Any]):
        """subject からの通知を受け取る処理"""
        ...

class SalesDepartment(InventoryObserver):
    """販売部門"""
    def __init__(self, name: str):
        self.name = name

    def update(self,  state: dict[str, Any]):
        print(f"{self.name} - 在庫更新通知: {state['name']}の在庫: {state['stock']}")

class PurchasingDepartment(InventoryObserver):
    """購買部門"""
    def __init__(self, name: str):
        self.name = name

    def update(self, state: dict[str, Any]):
        for item, quantity in state["stock"].items():
           if quantity < 10:
               print(f"{self.name} - 発注通知: {state['name']}の{item}の在庫が少なくなっています。")

class InventorySubject(ABC):
    @abstractmethod
    def attach(self, observer: InventoryObserver):
        ...
    @abstractmethod
    def detach(self, observer: InventoryObserver):
        ...
    @abstractmethod
    def notify(self):
        ...


class GeneralWarehouse(InventorySubject):
    def __init__(self, name: str):
        self.name = name
        self.observers: list[InventoryObserver] = []
        self.stock: dict[str, int] = {}

    def attach(self, observer: InventoryObserver):
        self.observers.append(observer)

    def detach(self, observer: InventoryObserver):
        self.observers.remove(observer)

    def notify(self):
        state = self.get_state()
        for observer in self.observers:
            observer.update(state)

    def set_stock(self, item: str, quantity: int):
        self.stock[item] = quantity
        self.notify()

    def get_stock(self) -> dict[str, int]:
        return self.stock

    def get_state(self) -> dict[str, Any]:
        return {"name": self.name, "stock": self.stock}

class RefrigeratedWarehouse(InventorySubject):
    def __init__(self, name: str):
        self.name = name
        self.observers: list[InventoryObserver] = []
        self.stock: dict[str, int] = {}
        self.temperature: float | None = None

    def attach(self, observer: InventoryObserver):
        self.observers.append(observer)

    def detach(self, observer: InventoryObserver):
        self.observers.remove(observer)

    def notify(self):
        state = self.get_state()
        for observer in self.observers:
            observer.update(state)

    def set_stock(self, item: str, quantity: int):
        self.stock[item] = quantity
        self.notify()

    def get_stock(self) -> dict[str, int]:
        return self.stock

    def set_temperature(self, temp: float):
       self.temperature = temp
       self.notify()

    def get_temperature(self) -> float | None:
        return self.temperature

    def get_state(self) -> dict[str, Any]:
        return {"name": self.name, "stock": self.stock, "temperature": self.temperature}

if __name__ == "__main__":
   # Subjects の作成
   general_warehouse = GeneralWarehouse("一般倉庫A")
   refrigerated_warehouse = RefrigeratedWarehouse("冷蔵倉庫B")
   # Observers の作成
   sales_dept = SalesDepartment("販売部門")
   purchasing_dept = PurchasingDepartment("購買部門")
   # Observer の登録
   general_warehouse.attach(sales_dept)
   general_warehouse.attach(purchasing_dept)
   refrigerated_warehouse.attach(sales_dept)
   refrigerated_warehouse.attach(purchasing_dept)
   # 在庫の更新
   general_warehouse.set_stock("商品A", 100)
   general_warehouse.set_stock("商品B", 5)
   refrigerated_warehouse.set_stock("商品C", 50)
   refrigerated_warehouse.set_temperature(-5)
   # Observer の削除
   general_warehouse.detach(purchasing_dept)
   # 再度在庫の更新
   general_warehouse.set_stock("商品A", 80)
