class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"
    
    def __format__(self, format_spec):
        if format_spec == "long":
            return f"{self.day} {self.month_name()} {self.year}"
        elif format_spec == "short":
            return f"{self.day:02d}/{self.month:02d}/{str(self.year)[-2:]}"
        else:
            return str(self)
        
    def month_name(self):
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        return months[self.month - 1]

if __name__ == "__main__":
    date = Date(5, 7, 2021)
    print(date)  # Default format
    print(f"{date:long}")  # Long format
    print(f"{date:short}")  # Short format