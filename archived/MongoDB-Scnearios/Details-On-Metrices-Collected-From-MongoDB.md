### Connections:
---
- **current:** The current number of active client connections to the MongoDB server.
- **available:** The number of available connections that can be created by the server.
- **totalCreated:** Total connections created by the server since its start.
- **rejected:** The count of connections rejected due to reaching server capacity.
- **active:** The number of currently active connections handling operations.
- **threaded:** The count of threads used for managing connections.
- **exhaustIsMaster:** The number of times isMaster responses were exhausted.
- **exhaustHello:** The count of times "hello" responses were exhausted.
- **awaitingTopologyChanges:** The number of connections awaiting topology changes.

### Network Traffic:
---
- **bytesIn:** Total bytes received by the MongoDB server.
- **bytesOut:** Total bytes sent from the MongoDB server.
- **physicalBytesIn:** Bytes received on the physical network interface.
- **physicalBytesOut:** Bytes sent on the physical network interface.
- **numRequests:** The total count of requests processed by the server.
- **tcpFastOpen:** Details about TCP Fast Open support.
- **compression:** Information about different compression methods and their usage.
- **serviceExecutors:** Details about service executors handling client requests.
- **listenerProcessingTime:** Duration of processing listener operations.

### Memory Usage:
---
- **bits:** Architecture bit version (e.g., 64-bit).
- **resident:** Amount of resident memory used by the MongoDB process.
- **virtual:** Total virtual memory used by the MongoDB process.
- **supported:** Indicates if memory size reporting is supported.

### Locks:
---
- Various lock types and their acquisition counts (e.g., Global, Database, Collection locks).

### Opcounters:
---
- Counts of different database operations executed (insert, query, update, delete, getmore, command).

### Collection Statistics:
---
- **ns:** Namespace of the collection.
- **size:** Total size of the collection in bytes.
- **count:** Total count of documents in the collection.
- **numOrphanDocs:** Number of orphaned documents.
- **storageSize:** The amount of space allocated for storage.
- **totalSize:** Total size of the collection and its indexes.
- **nindexes:** The count of indexes on the collection.
- **totalIndexSize:** Total size of all indexes.

### Index Usage:
---
- Details about index usage. (Absent in the provided data)
