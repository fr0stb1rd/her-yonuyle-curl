# Testleri derleme (Build tests)

Herhangi bir testi çalıştırmadan önce sadece curl'ü değil, aynı zamanda test paketini ve ilgili araçlarını ve sunucularını da derlemeniz gerekir.

En kolayı, derleme dizini kökünde `make test` komutunu vererek hepsini derleyip çalıştırabilirsiniz, ancak testler üzerinde daha fazla çalışmak veya belki bir tanesinde hata ayıklamak istiyorsanız, `tests` dizinine atlayıp oradan çalışmak isteyebilirsiniz. Hepsini derleyin ve test `144`'ü şu şekilde çalıştırın:

    cd tests
    make
    ./runtests.pl 144
