#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <pthread.h>

#define THREAD_POOL_SIZE 100
#define SCAN_TIMEOUT 100


void *scan_port(void *arg);

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: %s target\n", argv[0]);
        exit(1);
    }

    char *target = argv[1];

    // Create a TCP socket
    int sock = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);

    // Enable IP_HDRINCL option to allow us to build our own TCP packets
    int enable = 1;
    setsockopt(sock, IPPROTO_IP, IP_HDRINCL, &enable, sizeof(enable));

    // Use non-blocking I/O
    fcntl(sock, F_SETFL, O_NONBLOCK);

    // Prepare the TCP packet header
    struct tcphdr tcp_header;
    memset(&tcp_header, 0, sizeof(struct tcphdr));
    tcp_header.source = htons(1234);
    tcp_header.dest = htons(80);
    tcp_header.seq = random();
    tcp_header.doff = 5;
    tcp_header.fin = 0;
    tcp_header.syn = 1;
    tcp_header.rst = 0;
    tcp_header.psh = 0;
    tcp_header.ack = 0;
    tcp_header.urg = 0;
    tcp_header.window = htons(8192);
    tcp_header.check = 0;
    tcp_header.urg_ptr = 0;

    // Create a thread pool to limit the number of threads
    pthread_t thread_pool[THREAD_POOL_SIZE];
    int thread_pool_index = 0;

    // Track open ports
    int open_ports[65536];
    int num_open_ports = 0;

    // Scan all 65,535 ports
    for (int i = 1; i <= 65535; i++) {
        // Prepare the TCP packet
        struct iphdr ip_header;
        memset(&ip_header, 0, sizeof(struct iphdr));
        ip_header.ihl = 5;
        ip_header.version = 4;
        ip_header.tos = 0;
        ip_header.tot_len = sizeof(struct iphdr) + sizeof(struct tcphdr);
        ip_header.id = htonl(random());
        ip_header.frag_off = 0;
        ip_header.ttl = 255;
        ip_header.protocol = IPPROTO_TCP;
        ip_header.saddr = inet_addr("127.0.0.1");
        ip_header.daddr = inet_addr(target);
        ip_header.check = 0;

        char packet[sizeof(struct iphdr) + sizeof(struct tcphdr)];
        memcpy(packet, &ip_header, sizeof(struct iphdr));
        memcpy(packet + sizeof(struct iphdr), &tcp_header, sizeof(struct tcphdr));

        // Calculate the TCP checksum
        tcp_header.check = 0;
        tcp_header.check = htons(~htons(0 - htons(ip_header.protocol + sizeof(struct tcphdr))) & 0xFFFF);

        // Send the packet
        sendto(sock, packet, sizeof(packet), 0, (struct sockaddr *)&ip_header.daddr, sizeof(struct sockaddr_in));

        // Check if the socket is ready for I/O
        fd_set fdset;
        FD_ZERO(&fdset);
        FD_SET(sock, &fdset);

            struct timeval timeout;
    timeout.tv_sec = SCAN_TIMEOUT / 1000;
    timeout.tv_usec = (SCAN_TIMEOUT % 1000) * 1000;

    int ready = select(sock + 1, &fdset, NULL, NULL, &timeout);

    if (ready > 0) {
        // Receive the packet
        char buffer[65535];
        memset(buffer, 0, sizeof(buffer));
        struct sockaddr_in src_addr;
        socklen_t src_addr_len = sizeof(src_addr);
        int recv_len = recvfrom(sock, buffer, sizeof(buffer), 0, (struct sockaddr *)&src_addr, &src_addr_len);

        // Parse the packet to get the source port
        struct iphdr *ip_hdr = (struct iphdr *)buffer;
        struct tcphdr *tcp_hdr = (struct tcphdr *)(buffer + sizeof(struct iphdr));
        if (ip_hdr->protocol == IPPROTO_TCP && tcp_hdr->syn == 1 && tcp_hdr->ack == 1 && ntohs(tcp_hdr->ack_seq) == tcp_header.seq + 1) {
            int src_port = ntohs(tcp_hdr->source);

            // Add the open port to the list
            open_ports[num_open_ports++] = src_port;
        }
    }

    // Create a new thread to scan the next port if the thread pool is not full
    if (thread_pool_index < THREAD_POOL_SIZE) {
        pthread_create(&thread_pool[thread_pool_index++], NULL, scan_port, (void *)&tcp_header.dest);
    }

    // Wait for any thread to finish if the thread pool is full
    if (thread_pool_index == THREAD_POOL_SIZE) {
        pthread_join(thread_pool[--thread_pool_index], NULL);
    }
}

// Wait for all threads to finish
while (thread_pool_index > 0) {
    pthread_join(thread_pool[--thread_pool_index], NULL);
}

// Print the open ports
for (int i = 0; i < num_open_ports; i++) {
    printf("Port %d is open\n", open_ports[i]);
}

// Close the socket
close(sock);

return 0;
}

void *scan_port(void *arg) {
int port = *((int *)arg);

// Create a TCP socket
int sock = socket(AF_INET, SOCK_STREAM, 0);

// Use non-blocking I/O
fcntl(sock, F_SETFL, O_NONBLOCK);

// Connect to the port
struct sockaddr_in addr;
addr.sin_family = AF_INET;
addr.sin_port = htons(port);
addr.sin_addr.s_addr = inet_addr("127.0.0.1");
connect(sock, (struct sockaddr *)&addr, sizeof(addr));

// Check if the socket is ready for I/O
fd_set fdset;
FD_ZERO(&fdset);
FD_SET(sock, &fdset);

struct timeval timeout;
timeout.tv_sec = SCAN_TIMEOUT / 1000;
timeout.tv_usec = (SCAN_TIMEOUT % 1000) * 1000;

int ready = select(sock + 1, NULL, &fdset, NULL, &timeout);

if (ready > 0) {
    close(sock);
} else {
    close(sock);
}

return NULL;
}

