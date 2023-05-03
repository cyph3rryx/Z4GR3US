# TCP Port Scanner
This is a simple TCP port scanner implemented in C. It scans a range of ports on a specified IP address to determine which ports are open and which are closed.

## Features
    
    1/ Scans a range of ports on a specified IP address
    2/ Determines which ports are open and which are closed
    3/ Uses a thread pool to limit the number of threads and improve performance
    4/ Uses non-blocking I/O to avoid blocking the main thread while waiting for a connection
    5/ Includes error handling to handle cases where the socket or connection fails

## Requirements

    C compiler (tested with GCC)
 
    POSIX threads library (libpthread)

## Usage

To use the TCP port scanner, run the following command:

``` php
./port_scanner <ip address> <start port> <end port>
```

Where <ip address> is the IP address to scan, <start port> is the first port to scan, and <end port> is the last port to scan.

For example, to scan ports `1-1024` on the local machine:

``` bash
./port_scanner 127.0.0.1 1 1024
```
  
## Performance
The performance of the port scanner can be improved by increasing the thread pool size. This can be done by changing the THREAD_POOL_SIZE constant in the code. However, increasing the thread pool size may also increase the risk of network congestion or other performance issues.

## License
This code is released under the MIT License. See LICENSE for details.
