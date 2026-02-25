---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-asset-printer-industrial-001-expense-001"
ontological_class: "FixedAssetDepreciationExpense"
gist_equivalent: "gist:Magnitude"
value: 20000.0
hypercube_context:
  primary_hypercube: "StatementOfComprehensiveIncome"
  arrangement_pattern: "RollUp"
edges:
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-asset-printer-industrial-001-expense"
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
content_hash: "1e6aae15729d9dc93d8bf05ad7d974cdc66fa2442314af96bf5065cbdcbae0b5"
---
# Industrial 3D Printer (Depreciation Expense)
Method: Diminishing Value
Rate: 0.25
