class User(models.Model):
	first_name=models.Charfield(max_length=50)
	last_name=models.Charfield(max_length=50)
	address=models.ForeignKey(Address,related_name="users_address")
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	def __repr__(self):
		return "<User Object: {} {}>".format(self.first_name,self.last_name)

class Address(models.Model):
	address_line1=models.Charfield(max_length=60)
	address_line2=models.Charfield(max_length=60)
	city=models.Charfield(max_length=30)
	state=models.Charfield(max_length=30)
	pincode=models.Charfield(max_length=10)
	def __repr(self):
		return "<Address Object:{} {} {} {} {}>".format(self.address_line1,self.address_line2,self.city,self.state,self.pincode)

class Supplier(models.Model):
	supplier_name=models.Charfield(max_length=50)
	users=models.ManyToManyField(User,related_name="suppliers")
	address=models.ForeignKey(Address,related_name="suppliers_address")
	def __repr(self):
		return "<Supplier Object:{}>".format(self.supplier_name)

class Shelter(models.Model):
	shelter_name=models.Charfield(max_length=50)
	meals_required=models.IntegerField()
	users=models.ManyToManyField(User,related_name="shelters")
	address=models.ForeignKey(Address,related_name="shelters_address")
	def __repr__(self):
		return "<Shelter Object:{} {}>".format(self.shelter_name,self.meals_required)

class InventoryMap(models.Model):
	meals_available=models.IntegerField()
	cooked_at=models.DateTimeField()
	use_by=models.DateTimeField()
	shelter=models.ForeignKey(Shelter,related_name="inventory")
	supplier=models.ForeignKey(Supplier,related_name"supplier")
	def __repr__(self):
		return "<InventoryMap Object: {} {} {} >".format(self.meals_available,self.cooked_at,self.use_by)