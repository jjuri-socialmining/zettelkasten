# Run example

```
Building the Examples:
=====================
amalgamated - build the examples using the amalgamated driver
clean       - remove examples dir in build-output and example program
xmlrpc      - build the XML-RPC package used to communicate with Inphi Explorer

To connect to the EVB directly using InphiOlympus.dll in Cygwin64:
  make target=olympus legacy

To connect to the EVB through XML-RPC via Inphi Explorer:
  make target=xmlrpc legacy

Running the Examples:
=====================
    ./example 10.101.17.4 50000 version
```

Make and run c example connect directly Chip via Olympus
with olympus, need input MB_ID corresponse to CHIP
```
cd example
make target=olympus amalgamated
./example.exe 1 2015 testcase_name
./example.exe <abcd> MB_ID version
```
