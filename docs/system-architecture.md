# System Architecture

```
[ ESP32 Firmware ] --(HTTP POST / Scans)--> [ Django Backend ]
                                                 |
                                         (Hashing / OP_RETURN)
                                                 v
                                       [ Bitcoin Cash (BCH) ]
                                                 ^
                                         (Verify / Query)
                                                 |
[ Vue 3 Frontend ] <--(REST API)-----------------+
```
