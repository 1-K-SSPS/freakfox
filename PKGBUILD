pkgname=freakfox
pkgver=1.0
pkgrel=1
pkgdesc="Mega Freaky web browser"
url="http://spatula.net/software/sex/"
license=('freakyGPL')
depends=(python
    'python-pip'
    'python-virtualenv'
    'python-pyqt5'
    'python-pyqt5-webengine'
    'python-pygame'
)
arch=('any')
makedepends=()
source=("git+https://github.com/1-K-SSPS/freakfox")
md5sums=(SKIP)

package() {
    cd "${srcdir}/${pkgname}/src"
    cat > freakfox << EOL
#!/bin/sh
(cd /usr/share/freakfox/ && ./browser.py)
EOL
    install -Dm755 freakfox "$pkgdir/usr/bin/freakfox"
    install -Dm755 browser.py "$pkgdir/usr/share/freakfox/browser.py"
    install -Dm644 *.png "$pkgdir/usr/share/freakfox/"
    install -Dm644 *.jpg "$pkgdir/usr/share/freakfox/"
    install -Dm644 *.mp3 "$pkgdir/usr/share/freakfox/"
    install -Dm644 index.html "$pkgdir/usr/share/freakfox/index.html"
    install -Dm644 style.css "$pkgdir/usr/share/freakfox/style.css"
    install -Dm644 balance.txt "$pkgdir/usr/share/freakfox/balance.txt"
}
