# Konteyner (Container)

Hem `docker` hem de `podman` konteynerleştirme araçlarıdır. Docker imajı (image) şurada barındırılmaktadır:
[https://hub.docker.com/r/curlimages/curl](https://hub.docker.com/r/curlimages/curl)

Aşağıdaki komutla curl'ün en son sürümünü çalıştırabilirsiniz:

`docker` için komut:

    docker run -it --rm docker.io/curlimages/curl www.example.com

`podman` için komut:

    podman run -it --rm docker.io/curlimages/curl www.example.com

## Konteynerde curl'ü sorunsuz çalıştırma

curl'ü, ana bilgisayar (host) işletim sisteminde yüklü yerel bir uygulamaymış gibi bir konteyner içinde sorunsuz bir şekilde çalıştırmak için bir takma ad (alias) oluşturmak mümkündür.

Bash, ZSH, Fish kabuğunda (shell) curl'ü konteynerleştirme aracınız için bir takma ad olarak tanımlama komutu:

### Bash veya zsh

`docker` ile curl çağırın:

    alias curl='docker run -it --rm docker.io/curlimages/curl'

`podman` ile curl çağırın:

    alias curl='podman run -it --rm docker.io/curlimages/curl'

### Fish

`docker` ile curl çağırın:

    alias -s curl='docker run -it --rm docker.io/curlimages/curl'

`podman` ile curl çağırın:

    alias -s curl='podman run -it --rm docker.io/curlimages/curl'

Bir istekte bulunmak için sadece `curl www.example.com` komutunu çağırın

## kubernetes içinde curl çalıştırma

Bazen tıpkı bunun gibi k8s ağ sorunlarını curl ile gidermek yararlı olabilir:

    kubectl run -i --tty curl --image=curlimages/curl --restart=Never \
      -- "-m 5" www.example.com
