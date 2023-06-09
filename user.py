class User:
    def _init_(self, name, phone, address, tax):
        self.name = name
        self.phone = phone
        self.address = address
        self.tax = tax


    def set_user_enabled(self, enabled):
        self.enabled = true

    def change_enabled_status(self):
        if self.stock > 0:
            return True
        else:
            return False