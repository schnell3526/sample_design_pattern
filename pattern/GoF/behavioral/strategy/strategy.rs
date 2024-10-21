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

struct VIPPricing;
impl PricingStrategy for VIPPricing {
    fn calculate_price(&self, base_price: f64) -> f64 {
        base_price * 1.2
    }
}

struct TravelPackage {
    name: String,
    base_price: f64,
    // dynamic dispatch を行うため Box<dyn PricingStrategy> として定義
    pricing_strategy: Box<dyn PricingStrategy>,
}

impl TravelPackage {
    fn new(name: String, base_price: f64, pricing_strategy: Box<dyn PricingStrategy>) -> Self {
        Self {
            name,
            base_price,
            pricing_strategy,
        }
    }

    fn get_price(&self) -> f64 {
        self.pricing_strategy.calculate_price(self.base_price)
    }

    fn set_pricing_strategy(&mut self, pricing_strategy: Box<dyn PricingStrategy>) {
        self.pricing_strategy = pricing_strategy;
    }
}

fn main() {
    let mut tokyo_package = TravelPackage::new(
        String::from("Tokyo Adventure"),
        1000.0,
        Box::new(RegularPricing),
    );
    println!("Package: {}", tokyo_package.name);

    println!("Regular price: ${:.2}", tokyo_package.get_price());

    tokyo_package.set_pricing_strategy(Box::new(StudentPricing));
    println!("Student price: ${:.2}", tokyo_package.get_price());

    tokyo_package.set_pricing_strategy(Box::new(SeniorPricing));
    println!("Senior price: ${:.2}", tokyo_package.get_price());

    tokyo_package.set_pricing_strategy(Box::new(VIPPricing));
    println!("VIP price: ${:.2}", tokyo_package.get_price());
}
