# Windows

Windows üzerinde curl'ü birkaç farklı yolla derleyebilirsiniz. Microsoft'un MSVC derleyicisini veya ücretsiz ve açık kaynaklı mingw derleyicisini kullanmanızı öneririz. Ancak derleme süreci bunlarla sınırlı değildir.

Mingw kullanıyorsanız, [autotools](autotools.md) derleme sistemini kullanmak isteyebilirsiniz.

## Visual C++ proje dosyaları

[CMake](cmake.md) kullanarak bir dizi Visual Studio proje dosyası oluşturabilirsiniz:

    cmake -B build -G 'Visual Studio 17 2022'

Oluşturulduktan sonra bunları içe aktarır ve normal şekilde Visual Studio ile derlersiniz.

Bunları 32-bit Windows için bile oluşturabilirsiniz:

    cmake -B build -G 'Visual Studio 17 2022' \
    -DCMAKE_GENERATOR_PLATFORM=x86

## Mingw

curl'ü mingw derleyici paketi ile derleyebilirsiniz. Sizin için Makefile setini oluşturmak üzere [CMake](cmake.md) kullanın:

    cmake -B build -G "MinGW Makefiles"
