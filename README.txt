CARA MENJALANKAN PROGRAM,
python server.py
silahkan menunggu

Client akan mengirimkan payload text berisi “!echo <PHRASE>” di mana phrase merupakan 1 atau lebih kata. Server harus mereply dengan sebuah payload text berisi phrase tersebut. Note : phrase bisa lebih panjang dari limit data pada 1 frame. Phrase bersifat case sensitive.
Client akan mengirimkan payload text berisi “!submission”. Server harus mereply dengan payload binary dari berkas zip berisi source code + readme. Test case ini akan dilakukan sebelum test case 3.
Client akan mengirimkan payload binary berisi file submission kalian. Server harus mereply dengan payload text “1” atau “0”, dengan “1” berarti md5 checksum yang dikirim sama dengan md5 berkas anda dan “0” apabila sebaliknya. Lakukan komparasi hash secara case insensitive.
