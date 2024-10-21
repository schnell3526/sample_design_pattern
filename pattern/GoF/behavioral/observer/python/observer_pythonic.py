from __future__ import annotations
from typing import Any, Protocol
from dataclasses import dataclass
from abc import ABC, abstractmethod


class Observer(Protocol):
    def update(self, state: dict[str, Any]) -> None:
        ...

@dataclass
class SalesDepartment:
    """販売部門"""
    name: str

    def update(self, state: dict[str, Any]) -> None:
        print(f"{self.name} - 在庫更新通知: {state['name']}の在庫: {state['stock']}")

@dataclass
class PurchasingDepartment:
    """購買部門"""
    name: str

    def update(self, state: dict[str, Any]) -> None:
        for item, quantity in state["stock"].items():
            if quantity < 10:
                print(f"{self.name} - 発注通知: {state['name']}の{item}の在庫が少なくなっています。")


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        ...

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        ...

    @abstractmethod
    def notify(self) -> None:
        ...

class InventorySubject(Subject):
    __slots__ = ("name", "_stock", "_observers", "_warehouse_type")

    def __init__(self, *, name: str, _warehouse_type: str) -> None:
        self.name = name
        self._warehouse_type = _warehouse_type
        self._stock: dict[str, Any] = {}
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        state = self.get_state()
        for observer in self._observers:
            observer.update(state)

    @property
    def stock(self) -> dict[str, int]:
        return self._stock.copy()

    def set_stock(self, item: str, quantity: int) -> None:
        self._stock[item] = quantity
        self.notify()

    @abstractmethod
    def get_state(self) -> dict[str, Any]:
        ...

class RegularWarehouse(InventorySubject):
    __slots__ = ()

    def __init__(self, *, name: str = "一般倉庫") -> None:
        super().__init__(name=name, _warehouse_type="一般倉庫")

    def get_state(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "stock": self.stock,
            "warehouse_type": "一般倉庫"
        }

class RefrigeratedWarehouse(InventorySubject):
    __slots__ = ("_temperature",)

    def __init__(self, *, name: str = "冷蔵倉庫") -> None:
        super().__init__(name=name, _warehouse_type="冷蔵倉庫")
        self._temperature: float = 0.0

    @property
    def temperature(self) -> float | None:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        self._temperature = value
        self.notify()

    def get_state(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "stock": self.stock,
            "warehouse_type": "冷蔵倉庫",
            "temperature": self.temperature
        }



if __name__ == "__main__":
    # 倉庫の作成
    regular_warehouse = RegularWarehouse(name="一般倉庫A")
    refrigerated_warehouse = RefrigeratedWarehouse(name="冷蔵倉庫B")

    # オブザーバーの作成
    sales_dept = SalesDepartment("販売部門")
    purchasing_dept = PurchasingDepartment("購買部門")

    # オブザーバーの登録
    regular_warehouse.attach(sales_dept)
    regular_warehouse.attach(purchasing_dept)
    refrigerated_warehouse.attach(sales_dept)
    refrigerated_warehouse.attach(purchasing_dept)

    # 一般倉庫の在庫更新
    regular_warehouse.set_stock("商品A", 100)
    regular_warehouse.set_stock("商品B", 5)  # 発注通知が出力される

    # 冷蔵倉庫の在庫更新と温度設定
    refrigerated_warehouse.set_stock("商品C", 50)
    refrigerated_warehouse.temperature = -5

    # オブザーバーの削除テスト
    regular_warehouse.detach(purchasing_dept)
    regular_warehouse.set_stock("商品A", 80)
