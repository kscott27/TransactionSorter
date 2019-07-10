from APIData import TransactionData
from Transaction import CompletedTransaction
from Transaction import PlannedTransaction

class TransactionFactory():

  def __init__(self):
    self.completedTransactionIndex = 0


  def createTransaction(self, data):
    transaction = PlannedTransaction(data.name)
    transaction.initialize(date=data.date, category=data.category, amount=data.amount,
                           idKeywords=data.idKeywords, recurring=data.recurring, 
                           rateOfRecurrence=data.rateOfRecurrence)
    return transaction

  def createCompletedTransaction(self, data):
    transaction = CompletedTransaction(location=data.location, amount=data.amount, 
                                       referenceNumber=self.completedTransactionIndex, 
                                       date=data.date)
    self.completedTransactionIndex += 1
    return transaction
