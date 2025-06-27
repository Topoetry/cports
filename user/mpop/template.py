pkgname = "mpop"
pkgver = "1.4.21"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
]
makedepends = [
    "gnutls-devel",
    "libidn2-devel",
    "libsecret-devel",
]
checkdepends = ["bash"]
pkgdesc = "Retrieve mail from POP3 mailboxes"
license = "GPL-3.0-or-later"
url = "https://marlam.de/mpop"
source = f"{url}/releases/mpop-{pkgver}.tar.xz"
sha256 = "4ca0d1e0d01366fe3e0cf490d88d154df511278fb595638713be3ca675665855"
hardening = ["vis", "cfi"]
