# Kitabı derleyin (Build the book)

## Gereksinimler

[mdBook](https://github.com/rust-lang/mdBook)'u indirin ve kurun.

## Kurulum

Boş bir dizinde, `book` adında bir alt dizin oluşturun veya kitabı oluşturmak (render) istediğiniz hedef dizini gösteren `book` adında bir sembolik bağlantı (symlink) yapın. Hedef dizin, yerel bir web sunucusu için kök dizin olarak gayet iyi çalışır.

Kitabın kaynak dizinini işaret eden `src` adında bir sembolik bağlantı oluşturun.

Aşağıda gösterilen içeriğe sahip `book.toml` adında bir dosya oluşturun.

## Derleyin

`mdbook build`

Bu, kitabın HTML, PDF ve ePUB formatlarındaki tam sürümünü oluşturur. Hedef dizin güncellenir.

## `book.toml`

~~~
[book]
authors = ["Daniel Stenberg"]
language = "en"
multilingual = false
src = "src"
title = "everything curl"

[output.html.fold]
enable = true     # whether or not to enable section folding
level = 0         # the depth to start folding
~~~
