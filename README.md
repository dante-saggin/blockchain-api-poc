# blockchain-api-poc
This is just a study project, there is nothing special about it.

#Start API 
python flaskApp.py

#Test 
python -m unittest -v testBlockChainMethods.py

#Mine
curl -X GET http://localhost:8080/mine

#New Transaction
curl -X POST -H "Content-Type: application/json" -d '{
	"sender": "d4ee26eee15148ee92c6cd394edd974e",
	"recipient": "123456",
	"amount": 5
}' "http://localhost:8080/transactions/new"

# 

