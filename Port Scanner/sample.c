#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <IP address>\n", argv[0]);
        return 1;
    }

    char *target = argv[1];

    int sock;
    struct sockaddr_in target_addr;

    // Create a TCP socket
    sock = socket(AF_INET, SOCK_STREAM, 0);

    // Set target address and port
    target_addr.sin_family = AF_INET;
    target_addr.sin_port = htons(1); // Start with port 1
    inet_aton(target, &target_addr.sin_addr);

    // Try to connect to each port from 1 to 65535
    while (target_addr.sin_port < htons(65535)) {
        if (connect(sock, (struct sockaddr *)&target_addr, sizeof(target_addr)) == 0) {
            printf("Port %d is open\n", ntohs(target_addr.sin_port));
        }

        // Move to the next port
        target_addr.sin_port = htons(ntohs(target_addr.sin_port) + 1);
    }

    // Close the socket
    close(sock);

    return 0;
}
