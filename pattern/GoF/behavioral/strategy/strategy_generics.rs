trait PricingStrategy {
    fn calculate_price(&self, base_price: f64) -> f64;
}

struct RegularPricing;
impl PricingStrategy for RegularPricing {
    fn calculate_price(&self, base_price: f64) -> f64 {
        base_price
    }
}

struct StudentPricing;
impl PricingStrategy for StudentPricing {
    fn calculate_price(&self, base_price: f64) -> f64 {
        base_price * 0.8
    }
}

struct SeniorPricing;
impl PricingStrategy for SeniorPricing {
    fn calculate_price(&self, base_price: f64) -> f64 {
        base_price * 0.7
    }
}

struct VipPricing;
impl PricingStrategy for VipPricing {
    fn calculate_price(&self, base_price: f64) -> f64 {
        base_price * 1.2
    }
}

// ジェネリックな旅行パッケージ構造体
struct TravelPackage<T: PricingStrategy> {
    name: String,
    base_price: f64,
    pricing_strategy: T,
}

impl<T: PricingStrategy> TravelPackage<T> {
    fn new(name: String, base_price: f64, pricing_strategy: T) -> Self {
        TravelPackage {
            name,
            base_price,
            pricing_strategy,
        }
    }

    fn get_price(&self) -> f64 {
        self.pricing_strategy.calculate_price(self.base_price)
    }

    // 戦略を変更するメソッド（型が変わるため新しいインスタンスを返す）
    fn with_new_strategy<U: PricingStrategy>(self, new_strategy: U) -> TravelPackage<U> {
        TravelPackage {
            name: self.name,
            base_price: self.base_price,
            pricing_strategy: new_strategy,
        }
    }
}

fn main() {
    let tokyo_package = TravelPackage::new(
        String::from("Tokyo Adventure"),
        1000.0,
        RegularPricing,
    );
    println!("Package: {}", tokyo_package.name);

    println!("Regular price: ${:.2}", tokyo_package.get_price());

    let student_package = tokyo_package.with_new_strategy(StudentPricing);
    println!("Student price: ${:.2}", student_package.get_price());

    let senior_package = student_package.with_new_strategy(SeniorPricing);
    println!("Senior price: ${:.2}", senior_package.get_price());

    let vip_package = senior_package.with_new_strategy(VipPricing);
    println!("VIP price: ${:.2}", vip_package.get_price());
}
