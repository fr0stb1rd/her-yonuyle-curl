# CMake

CMake, Windows dahil çoğu modern platformda çalışan alternatif bir derleme yöntemidir. Bu yöntemi kullanarak önce derleme makinenizde cmake kurulu olması gerekir, derleme dosyalarını oluşturmak için cmake'i çağırın ve ardından derleyin. cmake'in `-G` bayrağıyla, dosyaların hangi derleme sistemi için oluşturulacağını seçersiniz. cmake kurulumunuzun desteklediği "oluşturucuların" (generators) listesi için `cmake --help` komutuna bakın.

Cmake komut satırında, ilk argüman cmake kaynak dosyalarının nerede bulunacağını belirtir; aynı dizindeyse bu `.` (tek bir nokta) olur.

Linux'ta aynı dizindeki CMakeLists.txt ile düz make kullanarak derlemek için şunları yapabilirsiniz:

    cmake -G "Unix Makefiles" .
    make

Veya orada unix makefile'larının varsayılan olduğu gerçeğine güvenebilirsiniz:

    cmake .
    make

Derleme için bir alt dizin oluşturmak ve orada make çalıştırmak için:

    mkdir build
    cd build
    cmake ..
    make
