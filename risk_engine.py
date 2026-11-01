class RiskEngine:
    def __init__(self, config: dict):
        self.max_exposure = config.get("max_exposure_usd", 5000)
        self.max_drawdown = config.get("max_drawdown_pct", 5.0)
        self.current_exposure = 0.0

    def check_order(self, order_value: float) -> bool:
        """Returns True if order is within limits, False otherwise."""
        if self.current_exposure + order_value > self.max_exposure:
            print("Risk Warning: Order exceeds max exposure limit.")
            return False
        return True

    def update_exposure(self, value: float):
        self.current_exposure += value
        
    def reset_limits(self):
        self.current_exposure = 0.0