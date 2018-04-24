classDiagram
MutableMapping <|-- MapBase
MapBase <|-- UnsortedTableMap
MapBase <|-- HashMapBase
MapBase <|-- SortedTableMap
MapBase <|-- TreeMap
HashMapBase <|-- ChainHashMap
HashMapBase <|-- ProbeHashMap 