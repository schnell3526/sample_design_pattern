package main

import "fmt"

type PricingStrategy interface {
	CalculatePrice(basePrice float64) float64
}

type RegularPricing struct{}

func (rp RegularPricing) CalculatePrice(basePrice float64) float64 {
	return basePrice
}

type StudentPricing struct{}

func (sp StudentPricing) CalculatePrice(basePrice float64) float64 {
	return basePrice * 0.8
}

type SeniorPricing struct{}

func (sp SeniorPricing) CalculatePrice(basePrice float64) float64 {
	return basePrice * 0.7
}

type VIPPricing struct{}

func (vp VIPPricing) CalculatePrice(basePrice float64) float64 {
	return basePrice * 1.2
}

type TravelPackage struct {
	name            string
	basePrice       float64
	pricingStrategy PricingStrategy
}

func NewTravelPackage(name string, basePrice float64, pricingStrategy PricingStrategy) *TravelPackage {
	return &TravelPackage{name: name, basePrice: basePrice, pricingStrategy: pricingStrategy}
}

func (tp TravelPackage) GetPrice() float64 {
	return tp.pricingStrategy.CalculatePrice(tp.basePrice)
}

func (tp *TravelPackage) SetPricingStrategy(ps PricingStrategy) {
	tp.pricingStrategy = ps
}

func main() {
	regularPricing := RegularPricing{}
	studentPricing := StudentPricing{}
	seniorPricing := SeniorPricing{}
	vipPricing := VIPPricing{}

	tokyoPackage := NewTravelPackage("Tokyo Adventure", 1000, regularPricing)

	fmt.Println("Regular price:", tokyoPackage.GetPrice())

	tokyoPackage.SetPricingStrategy(studentPricing)
	fmt.Println("Student price:", tokyoPackage.GetPrice())

	tokyoPackage.SetPricingStrategy(seniorPricing)
	fmt.Println("Senior price:", tokyoPackage.GetPrice())

	tokyoPackage.SetPricingStrategy(vipPricing)
	fmt.Println("VIP price:", tokyoPackage.GetPrice())
}
