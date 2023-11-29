class Bank:
	def __init__ (self):
		self.clients = []

	def add_client(self, client):
		self.clients.append(client)

	def del_clirnt(self, client):
		for i in range(len(self.clients)):
			if self.client[i].id == client.id;
				self.client[i].pop()
				break

	def all_cash(self):
		cash = 0
		for i in range(len(self.clients)):
			cash += self.clients[i].cash
		return cash

	def get_client(id):
		for i in range(len(self.clients)):
			if self.client[i].id == client.id;
				return self.client[i]
