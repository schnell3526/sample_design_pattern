#[derive(Clone, Copy)]
enum PricingStrategy {
    Regular,
    Student,
    Senior,
    Vip,
}

impl PricingStrategy {
    fn calculate_price(&self, base_price: f64) -> f64 {
        match self {
            PricingStrategy::Regular => base_price,
            PricingStrategy::Student => base_price * 0.8,
            PricingStrategy::Senior => base_price * 0.7,
            PricingStrategy::Vip => base_price * 1.2,
        }
    }
}

struct TravelPackage {
    name: String,
    base_price: f64,
    pricing_strategy: PricingStrategy,
}

impl TravelPackage {
    fn new(name: String, base_price: f64, pricing_strategy: PricingStrategy) -> Self {
        TravelPackage {
            name,
            base_price,
            pricing_strategy,
        }
    }

    fn get_price(&self) -> f64 {
        self.pricing_strategy.calculate_price(self.base_price)
    }

    fn set_pricing_strategy(&mut self, pricing_strategy: PricingStrategy) {
        self.pricing_strategy = pricing_strategy;
    }
}

fn main() {
    let mut tokyo_package = TravelPackage::new(
        String::from("Tokyo Adventure"),
        1000.0,
        PricingStrategy::Regular,
    );
    println!("Package: {}", tokyo_package.name);

    println!("Regular price: ${:.2}", tokyo_package.get_price());

    tokyo_package.set_pricing_strategy(PricingStrategy::Student);
    println!("Student price: ${:.2}", tokyo_package.get_price());

    tokyo_package.set_pricing_strategy(PricingStrategy::Senior);
    println!("Senior price: ${:.2}", tokyo_package.get_price());

    tokyo_package.set_pricing_strategy(PricingStrategy::Vip);
    println!("VIP price: ${:.2}", tokyo_package.get_price());
}
